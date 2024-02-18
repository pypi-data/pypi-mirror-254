from base64 import b64decode, b64encode
from dataclasses import dataclass
from functools import cached_property
import hashlib
import io
import json
import logging
import os
import pathlib
import sys
import tarfile
from typing import ClassVar, Optional, Union

import bsdiff4

# https://packaging.python.org/en/latest/guides/single-sourcing-package-version/
# https://semver.org/
__version__ = '0.0.1'

logger = logging.getLogger(__name__)

BASE_DIR = pathlib.Path(__file__).resolve().parent

DEBUG = 'DEBUG' in os.environ or 'unittest' in sys.modules

DEFAULT_HASH_ALGORITHM = 'sha256'
CMP_CHUNK_SIZE = 8 * 1024
TAR_SUFFIX = '.tar'
COMPRESSION_SUFFIXES = ['.gz', '.bz2', '.xz']  # todo: .bz2 and .xz need tests
PATCH_SUFFIX = '.json'

# tarfile uses this value but does not define a constant for it
DEFAULT_ERRORS = 'surrogateescape'
# specify tar format for writing (from docs: "When reading, format will be
# automatically detected, even if different formats are present in a single archive.")
TAR_FORMAT = tarfile.GNU_FORMAT


class TarDiff(object):
    """
    The TarDiff class provides methods that compare two tar archives (tarballs) on a
    file level. For each member of the `old` and `new` archives, it indicates whether
    the member was added, deleted, modified, or untouched.

    todo: compare file headers as well, using e.g. TarInfo.get_info()
    """

    ADDED = 'added'
    DELETED = 'deleted'
    MODIFIED = 'modified'
    RENAMED = 'renamed'
    UNTOUCHED = 'untouched'  # or 'identical'?
    # order is important: renamed must follow added an deleted
    STATUS_PROPS = [ADDED, DELETED, MODIFIED, RENAMED, UNTOUCHED]

    def __init__(self, old: Union[pathlib.Path, str], new: Union[pathlib.Path, str]):
        # enforce paths
        self.paths = dict(old=pathlib.Path(old), new=pathlib.Path(new))
        # get all archive members
        self.members = dict()
        for key, path in self.paths.items():
            with tarfile.open(path, mode='r') as tar:
                self.members[key] = {tarinfo.name: tarinfo for tarinfo in tar}

    @cached_property
    def equal(self):
        """return True if both tar archives are considered equal"""
        return self.all == self.untouched

    def _compare_names(self, operation: str, reverse: bool = False) -> list:
        """use set operations to compare names of tar items"""
        # todo: compare entire TarInfo objects (or get_info dicts)?
        keys = ['old', 'new']
        if reverse:
            keys.reverse()
        a, b = [set(self.members[k].keys()) for k in keys]
        ops = dict(union=a.union, intersection=a.intersection, difference=a.difference)
        return sorted(ops.get(operation)(b))

    @cached_property
    def all(self) -> list:
        return self._compare_names(operation='union')

    @cached_property
    def added(self) -> list:
        """items in `new` that are not in `old` (includes renamed items)"""
        return self._compare_names(operation='difference', reverse=True)

    @cached_property
    def deleted(self) -> list:
        """items in `old` that are not in `new` (includes renamed items)"""
        return self._compare_names(operation='difference', reverse=False)

    @cached_property
    def renamed(self) -> list[tuple]:
        """items in `added` with file content identical to an item in `deleted`"""
        renamed_ = []
        with (
            tarfile.open(self.paths['old'], mode='r') as old_tar,
            tarfile.open(self.paths['new'], mode='r') as new_tar,
        ):
            for new_name in self.added:
                new_member = new_tar.getmember(new_name)
                if not new_member.isfile():
                    continue
                for old_name in self.deleted:
                    old_member = old_tar.getmember(old_name)
                    if not old_member.isfile():
                        continue
                    with (
                        old_tar.extractfile(old_member) as old_obj,
                        new_tar.extractfile(new_member) as new_obj,
                    ):
                        if compare_bytes(old_obj, new_obj):
                            renamed_.append((old_name, new_name))
        return renamed_

    @cached_property
    def common(self) -> list:
        """items common to `old` and `new` (but may have changed)"""
        return self._compare_names(operation='intersection')

    @cached_property
    def modified(self) -> list[tuple]:
        """
        For comparing pairs of files byte-by-byte comparison should be more efficient
        than hash comparison. Hash comparison is better when comparing a file with
        many other files. See e.g. [1]

        [1]: https://stackoverflow.com/questions/1072569#comment885379_1072576
        """
        modified_ = []
        with (
            tarfile.open(self.paths['old'], mode='r') as old_tar,
            tarfile.open(self.paths['new'], mode='r') as new_tar,
        ):
            for key in self.common:
                # typically, a change in content will also change the header, but,
                # depending on the tar configuration, it is also possible for the
                # header to change while content remains the same, or vice versa (if
                # content *length* remains the same)
                modified_items = []
                old_member = old_tar.getmember(key)
                new_member = new_tar.getmember(key)
                # compare headers (chksum should be sufficient, but this is not
                # always calculated in python...)
                if old_member.get_info() != new_member.get_info():
                    modified_items.append('header')
                # compare file contents
                if old_member.isfile() and new_member.isfile():
                    with (
                        old_tar.extractfile(old_member) as old_obj,
                        new_tar.extractfile(new_member) as new_obj,
                    ):
                        if old_obj and new_obj:
                            # byte-by-byte comparison of new vs old
                            #
                            # NOTE: we would use filecmp.cmp(..., shallow=False)
                            # here, but that expects file paths, not file objects,
                            # so we just copy the logic from filecmp._do_cmp for now
                            if not compare_bytes(old_obj, new_obj):
                                modified_items.append('content')
                        else:
                            logger.debug('something is wrong...')  # TEMP
                if modified_items:
                    modified_.append((key, tuple(modified_items)))
        return modified_

    @cached_property
    def untouched(self) -> list:
        return sorted(set(self.common) - set(key for key, __ in self.modified))

    def report(self, show=False) -> dict:
        """
        return a dict with all tar items and their status, where status is 'added',
        'deleted', 'renamed', 'untouched', or 'modified'
        """
        report_ = dict()
        for key in self.all:
            # note that the order of items in STATUS_PROPS is important, because e.g.
            # 'renamed' overrides 'added' and 'deleted', so 'renamed' must be
            # evaluated last
            for prop_name in self.STATUS_PROPS:
                # prop_value can be a key or a tuple (key, ...)
                prop_value = getattr(self, prop_name)
                if prop_name == self.RENAMED:
                    # flatten list of tuples
                    keys = [item for tpl in prop_value for item in tpl]
                elif prop_name == self.MODIFIED:
                    # extract keys from list of tuples
                    keys = [tpl[0] for tpl in prop_value]
                else:
                    keys = prop_value
                if key in keys:
                    report_[key] = prop_name
        if show:
            print('\ntardiff report:')
            for key, value in report_.items():
                print(f'{key}: {value}')
            print('\nsummary:')
            print(f'\ttotal members (including directories): {len(report_)}')
            renamed = int(list(report_.values()).count(self.RENAMED) / 2)
            for prop_name in self.STATUS_PROPS:
                note = ''
                if prop_name in [self.ADDED, self.DELETED]:
                    note = f'({renamed} renamed)'
                if prop_name != self.RENAMED:
                    count = list(report_.values()).count(prop_name)
                    print(f'\tfiles {prop_name}: {count} {note}')
        return report_


@dataclass
class PatchMember(object):
    # field attributes
    name: str
    status: str
    status_extra: Optional[str] = None  # stores extra information w.r.t. the status
    hash: Optional[list[str, str]] = None  # hash algorithm, e.g. 'sha256', and value
    diff: Optional[bytes] = None
    tarinfo: Optional[tarfile.TarInfo] = None
    # non-field attributes
    binary_fields: ClassVar = ['diff']  # this is simpler than introspection

    def set_hash(self, content: bytes, algorithm: str = DEFAULT_HASH_ALGORITHM):
        """calculate hash of content"""
        # todo: use hashlib.file_digest from python 3.11 (when <=3.10 support dropped)
        hash_obj = getattr(hashlib, algorithm)()
        hash_obj.update(content)
        # hexdigest returns digest as string
        self.hash = [algorithm, hash_obj.hexdigest()]  # noqa

    def verify_hash(self, content: bytes):
        """compare content hash with expected hash"""
        if not self.hash:
            raise ValueError('PatchMember.hash has not been set')
        algorithm, expected_hash = self.hash
        hash_obj = getattr(hashlib, algorithm)()
        hash_obj.update(content)
        if expected_hash != hash_obj.hexdigest():
            raise ValueError(f'{algorithm} hash mismatch for {self.name}')


def create_patch(
    src_path: Union[pathlib.Path, str],
    dst_path: Union[pathlib.Path, str],
    patch_path: Union[pathlib.Path, str, None] = None,
    hash_algorithm: str = DEFAULT_HASH_ALGORITHM,
) -> pathlib.Path:
    """
    A tar patch contains a JSON array of objects representing all members from both
    the source (`src`) and destination (`dst`) tarballs.

    Each object represents a PatchMember, containing relevant information from the
    tar archive member (i.e. from the TarInfo), together with the actual file diff,
    where applicable. In JSON representation this looks like:

    [
        {
            "name": "./some.file",
            "status": "modified",
            "status_extra": ["header", "content"],
            "hash": ["sha256", <hash string>],
            "diff": <base64 encoded string>,
            "tarinfo": <output of TarInfo.get_info()>
        },
        {
            "name": "./some_dir",
            "status": "untouched",
            "status_extra": null,
            "hash": null,
            "diff": null,
            "tarinfo": <output of TarInfo.get_info()>
        },
        ...
    ]

    `status` can be one of the following: `added`, `deleted`, `modified`,
    `untouched`, or `renamed`

    `diff` is only relevant if `status` is `added` or `modified`

    We use binary differences, regardless of whether the actual file content can be
    considered text or pure binary. To include binary data in JSON, we encode using
    base64/ascii. Text-based diffs could be useful, where possible, but automatically
    detecting text requires heuristics and is not worth the trouble.

    JSON may not be the most efficient format, but it was chosen to simplify
    inspection of the patch. An obvious alternative would be to build a tarball that
    includes only the patch data, but that is quite a bit more opaque.

    todo: Depending on the size of real archives and diffs, and memory constraints,
     it may be necessary to use an iterative JSON parser like ijson [2], or even
     revert to tar.

    Note that JSON preserves the order of the `patch` list [1]:

    >An array is an *ordered* sequence of zero or more values.

    [1]: https://www.rfc-editor.org/rfc/rfc7159.html#page-3
    [2]: https://github.com/ICRAR/ijson
    """
    # process inputs
    src_path = pathlib.Path(src_path)
    dst_path = pathlib.Path(dst_path)
    if patch_path is None:
        patch_path = dst_path.with_suffix(PATCH_SUFFIX)
    patch_path = pathlib.Path(patch_path)
    # produce diff of tarballs
    tar_diff = TarDiff(old=src_path, new=dst_path)
    # create patch
    patch = []
    with (
        tarfile.open(src_path, mode='r') as src,
        tarfile.open(dst_path, mode='r') as dst,
    ):
        print('\ncreating tar patch:')
        for key, value in tar_diff.report().items():
            print(f'{key}: {value}')
            if value == TarDiff.DELETED:
                patch_member = PatchMember(name=key, status=value)
            elif value == TarDiff.RENAMED:
                patch_member = None
                for old_name, new_name in tar_diff.renamed:
                    # there should be only one match...
                    kwargs = dict()
                    if key == new_name:
                        # include dst tarinfo and store name of corresponding src member
                        kwargs['status_extra'] = old_name
                        kwargs['tarinfo'] = dst.getmember(name=key)
                    patch_member = PatchMember(name=key, status=value, **kwargs)
            else:
                tar_member = dst.getmember(name=key)
                patch_member = PatchMember(name=key, status=value, tarinfo=tar_member)
                if value == TarDiff.ADDED:
                    # add the complete file content
                    if tar_member.isfile():
                        with dst.extractfile(tar_member) as file_obj:
                            patch_member.diff = file_obj.read()
                elif value == TarDiff.MODIFIED:
                    if tar_member.isfile():
                        with (
                            src.extractfile(key) as src_obj,
                            dst.extractfile(key) as dst_obj,
                        ):
                            dst_bytes = dst_obj.read()
                            # calculate hash of dst file
                            patch_member.set_hash(
                                content=dst_bytes, algorithm=hash_algorithm
                            )
                            # create binary diff from file content
                            patch_member.diff = bsdiff4.diff(
                                src_bytes=src_obj.read(), dst_bytes=dst_bytes
                            )
            patch.append(patch_member)
    # write to json file
    patch_path.write_text(
        json.dumps(patch, cls=PatchJSON, indent=2 if DEBUG else None, sort_keys=True)
    )
    return patch_path


def apply_patch(
    src_path: Union[pathlib.Path, str],
    patch_path: Union[pathlib.Path, str],
    dst_path: Union[pathlib.Path, str, None] = None,
) -> pathlib.Path:
    """
    Note that the ultimate goal is byte-by-byte equality between the reconstructed
    *destination* tarball and the original *destination* tarball.

    File order and information contained in the header blocks need to be preserved,
    see standard [1] for details. However, the original tar archives must already be
    created reproducibly, as described in [2]. This implies:

    - set mtime to source date epoch, e.g. based on latest git log time [3]
    - sort files by name (locale independent)
    - owner and group must be set to 0
    - remove pax headers if any

    [1]: https://www.gnu.org/software/tar/manual/html_node/Standard.html
    [2]: https://reproducible-builds.org/docs/archives/#full-example
    [3]: https://reproducible-builds.org/docs/source-date-epoch/
    [4]: https://www.gnu.org/software/tar/manual/tar.html#All-Options
    [5]: https://www.gnu.org/software/tar/manual/tar.html#override
    """
    # process inputs
    src_path = pathlib.Path(src_path)
    patch_path = pathlib.Path(patch_path)
    if dst_path is None:
        dst_path = patch_path.with_suffix(TAR_SUFFIX)
    dst_path = pathlib.Path(dst_path)
    # load patch data and apply patch
    with (
        tarfile.open(src_path, mode='r') as src_tar,
        tarfile.open(dst_path, mode=write_mode(dst_path), format=TAR_FORMAT) as dst_tar,
    ):
        for patch_member in json.loads(
            patch_path.read_text(), object_hook=PatchJSON.object_hook
        ):
            if patch_member.status == TarDiff.DELETED:
                logger.debug(f'skipping {patch_member.name}: not part of new archive')
                continue
            dst_member = patch_member.tarinfo
            if patch_member.status == TarDiff.ADDED:
                # copy diff as new file into the tar archive
                dst_tar.addfile(
                    tarinfo=dst_member, fileobj=io.BytesIO(patch_member.diff)
                )
            else:
                if patch_member.status == TarDiff.RENAMED:
                    if patch_member.status_extra:
                        src_member = src_tar.getmember(name=patch_member.status_extra)
                    else:
                        logger.debug(f'skipping {patch_member.name}: renamed')
                        continue
                else:
                    src_member = src_tar.getmember(name=patch_member.name)
                if src_member.isfile():
                    with src_tar.extractfile(member=src_member) as src_file:
                        if patch_member.status in [TarDiff.UNTOUCHED, TarDiff.RENAMED]:
                            # copy the src_file directly into the tar archive
                            dst_tar.addfile(tarinfo=dst_member, fileobj=src_file)
                        elif patch_member.status == TarDiff.MODIFIED:
                            # reconstruct the dst_file from the src_file and diff
                            dst_bytes = bsdiff4.patch(
                                src_bytes=src_file.read(), patch_bytes=patch_member.diff
                            )
                            # verify hash of reconstructed file content
                            patch_member.verify_hash(content=dst_bytes)
                            # add to tar
                            dst_tar.addfile(
                                tarinfo=dst_member, fileobj=io.BytesIO(dst_bytes)
                            )
                else:
                    # if the member is not a file, there's nothing to extract
                    # https://stackoverflow.com/a/77887084
                    dst_tar.addfile(tarinfo=dst_member, fileobj=None)
    return dst_path


def compare_bytes(obj_1, obj_2):
    """
    adaptation of filecmp._do_cmp that handles file objects instead of paths [1]

    [1]: https://github.com/python/cpython/blob/6888cccac0776d965cc38a7240e1bdbacb952b91/Lib/filecmp.py#L75
    """
    counter = 0
    while True:
        counter += 1
        chunk_1 = obj_1.read(CMP_CHUNK_SIZE)
        chunk_2 = obj_2.read(CMP_CHUNK_SIZE)
        if chunk_1 != chunk_2:
            logger.debug(f'\nchunk {counter}\n\tobj_1: {chunk_1}\n\tobj_2: {chunk_2}')
            return False
        if not chunk_1:
            return True


class PatchJSON(json.JSONEncoder):
    def default(self, obj):
        """handle JSON encoding of unsupported types"""
        if isinstance(obj, bytes):
            # an alternative would be to use obj.decode('latin1'), which is also able
            # to handle arbitrary bytes
            return b64encode(obj).decode('ascii')
        elif isinstance(obj, PatchMember):
            obj_dict = vars(obj)
            obj_dict[self._class_hint(PatchMember)] = None
            return obj_dict
        elif isinstance(obj, tarfile.TarInfo):
            # beware: TarInfo.get_info() is actually undocumented...
            obj_dict = dict(obj.get_info())
            obj_dict[self._class_hint(tarfile.TarInfo)] = None
            return obj_dict
        return super().default(obj)

    @classmethod
    def object_hook(cls, dct: dict) -> Union[dict, PatchMember, tarfile.TarInfo]:
        """
        reconstruct python objects from json objects: instead of a dict, we get an
        actual instance of the class indicated by the class hint

        the object_hook is called only for JSON objects, i.e. {}, not for e.g. arrays []

        see examples in docs: https://docs.python.org/3/library/json.html
        """
        if cls._class_hint(PatchMember) in dct:
            dct.pop(cls._class_hint(PatchMember))
            # binary fields stored as text in JSON need to be decoded to bytes
            binary_values = dict()
            for key in PatchMember.binary_fields:
                string_value = dct.pop(key, None)
                binary_values[key] = None
                if string_value is not None:
                    # note b64decode accepts both bytes and strings, no need to encode
                    binary_values[key] = b64decode(string_value)  # noqa
            return PatchMember(**dct, **binary_values)
        elif cls._class_hint(tarfile.TarInfo) in dct:
            dct.pop(cls._class_hint(tarfile.TarInfo))
            # TarInfo only accepts a name arg
            tarinfo = tarfile.TarInfo(name=dct.pop('name'))
            for key, value in dct.items():
                if key == 'type':
                    value = b64decode(value)
                setattr(tarinfo, key, value)
            return tarinfo
        # return dict untouched
        return dct

    @staticmethod
    def _class_hint(obj_class):
        """
        class hint is used to restore instance in json object_hook

        see e.g. https://www.jsonrpc.org/specification_v1#a3.JSONClasshinting
        """
        return f'__{obj_class.__name__}__'


def write_mode(path: Union[pathlib.Path, str]) -> str:
    """
    Determine tarfile.open() write mode based on path suffix.

    This is only necessary for write mode, because "transparent read" mode 'r'
    handles both uncompressed and compressed archives automatically

    [1]: https://docs.python.org/3/library/tarfile.html#tarfile.open
    """
    path = pathlib.Path(path)
    mode = 'w'  # uncompressed
    if path.suffix in COMPRESSION_SUFFIXES:
        mode += path.suffix.replace('.', ':')
    return mode
