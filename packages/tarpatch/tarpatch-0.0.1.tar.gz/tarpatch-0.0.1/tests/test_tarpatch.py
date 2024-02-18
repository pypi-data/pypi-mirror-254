import filecmp
import gzip
import io
import json
import logging
import pathlib
import random
import tarfile
from unittest import TestCase

from tarpatch import (
    apply_patch,
    CMP_CHUNK_SIZE,
    compare_bytes,
    COMPRESSION_SUFFIXES,
    create_patch,
    DEFAULT_HASH_ALGORITHM,
    PatchJSON,
    PatchMember,
    TarDiff,
    TAR_FORMAT,
    write_mode,
)
from tests import TempDirTestCase
from tests.helpers import make_file

# for notational convenience
ADDED = TarDiff.ADDED
DELETED = TarDiff.DELETED
MODIFIED = TarDiff.MODIFIED
RENAMED = TarDiff.RENAMED
UNTOUCHED = TarDiff.UNTOUCHED

# define dummy file tree and data for the 'before' and 'after' cases
DATA = {
    UNTOUCHED: {
        './subdir/file3.binary': b'more binary data',
    },
    MODIFIED: {
        './file1.binary': (b'x' * 20, b'y' * 20),  # equal size
        './subdir/file2.txt': ('original text', 'changed text, different size'),
        './file6.txt': ('content untouched', 'content untouched'),  # header change only
    },
    ADDED: {
        './new-file.binary': b'whatever',
        './new-file.txt': 'brand new content',
        './subdir/file5.md': 'moved content',
    },
    DELETED: {
        './file0.txt': 'not interesting enough to keep around',
        './subdir/subsubdir/file4.txt': 'something else we can do without',
        './file5.txt': 'moved content',
    },
}
# flatten nested dicts into single dict
ALL = {key: value for dct in DATA.values() for key, value in dct.items()}
# determine unique subdirs (including '.')
SUBDIRS = set(
    f'./{parent}' if str(parent) != '.' else '.'
    for key in ALL.keys()
    for parent in pathlib.Path(key).parents
)
# expected members
ALL_MEMBERS = sorted(list(ALL) + list(SUBDIRS))
RENAMED_MEMBERS = [('./file5.txt', './subdir/file5.md')]  # content must be identical
COMMON_MEMBERS = sorted(list(DATA[UNTOUCHED].keys()) + list(DATA[MODIFIED].keys()))


def filter_factory(name):
    """
    create a filter that modifies the tarinfo with specified name

    see e.g. https://docs.python.org/3/library/tarfile.html#examples
    """

    def tar_filter(tarinfo):
        if tarinfo.name == name:
            tarinfo.mtime = 0  # just an arbitrary modification
        return tarinfo

    return tar_filter


class TarTestCase(TempDirTestCase):
    def setUp(self):
        # the TempDirTestCase sets a temporary directory that is removed automatically
        super().setUp()
        # define temporary before/after directories
        self.before = self.temp_dir_path / 'before'
        self.after = self.temp_dir_path / 'after'
        # create file tree content
        for name, data in DATA[UNTOUCHED].items():
            for root in [self.before, self.after]:
                make_file(root=root, name=name, data=data)
        header_modified_name = None
        for name, (data_before, data_after) in DATA[MODIFIED].items():
            if data_before == data_after:
                # note: actual header modification is done using a filter below
                header_modified_name = name
            for root, data in zip([self.before, self.after], (data_before, data_after)):
                make_file(root=root, name=name, data=data)
        for status, root in [(ADDED, self.after), (DELETED, self.before)]:
            # this also creates the 'renamed' files
            for name, data in DATA[status].items():
                make_file(root=root, name=name, data=data)
        for name, data in DATA[DELETED].items():
            make_file(root=self.before, name=name, data=data)
        # create tarballs
        trees = dict(old=self.before, new=self.after)
        self.tarballs = dict()
        mod_filter = None
        for key, src_path in trees.items():
            if key == 'new':
                # only modify the header in the new archive for member matching name
                mod_filter = filter_factory(name=header_modified_name)
            # write gzip-compressed tar archives (.tar.gz)
            suffix = '.tar.gz'
            tarball_path = (self.temp_dir_path / src_path.name).with_suffix(suffix)
            with tarfile.open(
                tarball_path, mode=write_mode(tarball_path), format=TAR_FORMAT
            ) as tar:
                tar.add(
                    name=src_path,
                    arcname=src_path.relative_to(src_path),
                    recursive=True,
                    filter=mod_filter,
                )
            self.tarballs[key] = tarball_path


class TarDiffTests(TarTestCase):
    def test_init(self):
        td = TarDiff(**self.tarballs)
        self.assertTrue(td.members)

    def test_equal(self):
        # tarballs are *not* the same
        self.assertFalse(TarDiff(**self.tarballs).equal)
        # tarballs are the same
        self.assertTrue(TarDiff(self.tarballs['old'], self.tarballs['old']).equal)

    def test_all(self):
        td = TarDiff(**self.tarballs)
        self.assertEqual(ALL_MEMBERS, td.all)

    def test_added(self):
        # beware, this includes renamed items
        td = TarDiff(**self.tarballs)
        self.assertEqual(sorted(DATA[ADDED].keys()), td.added)

    def test_deleted(self):
        # beware, this includes renamed items
        td = TarDiff(**self.tarballs)
        # ignore subdirs from result
        deleted = set(td.deleted).difference(SUBDIRS)
        self.assertEqual(set(DATA[DELETED].keys()), deleted)

    def test_renamed(self):
        td = TarDiff(**self.tarballs)
        self.assertEqual(RENAMED_MEMBERS, td.renamed)

    def test_common(self):
        td = TarDiff(**self.tarballs)
        # ignore subdirs from result
        common = set(td.common).difference(SUBDIRS)
        self.assertEqual(set(COMMON_MEMBERS), common)

    def test_modified(self):
        td = TarDiff(**self.tarballs)
        self.assertTrue(td.modified)
        expected = [
            (key, modified_items)
            for key, modified_items in zip(
                # this is a bit fragile... must match order of MODIFIED definition
                DATA[MODIFIED].keys(),
                [('content',), ('header', 'content'), ('header',)],
            )
        ]
        self.assertEqual(set(expected), set(td.modified))

    def test_untouched(self):
        td = TarDiff(**self.tarballs)
        self.assertTrue(td.untouched)
        # ignore subdirs from result
        untouched = set(td.untouched).difference(SUBDIRS)
        self.assertEqual(set(DATA[UNTOUCHED].keys()), untouched)

    def test_report(self):
        td = TarDiff(**self.tarballs)
        report = td.report(show=True)
        self.assertEqual(len(ALL_MEMBERS), len(report))

    def test_tarinfo_chksum(self):
        """
        show that completely different file content may lead to identical chksum
        values if the content has the same size and name

        according to the tar "standard" [1]:

        >The `chksum` field represents the simple sum of all bytes in the header block.

        >The `mtime` field represents the data modification time of the file at the
        time it was archived. It represents the integer number of seconds ...

        the standard also lists the fields included in the file header block

        the tarfile source [2] shows that all bytes from the header block are
        included in the chksum, including `mtime` and `name` (the struct format
        "148B8x356B" includes everything but sets the `chksum` field itself to spaces)

        [1]: https://www.gnu.org/software/tar/manual/html_node/Standard.html
        [2]: https://github.com/python/cpython/blob/07ef63fb6a0fb996d5f56c79f4ccd7a1887a6b2b/Lib/tarfile.py#L233
        """
        size = 1000
        some_file = self.temp_dir_path / 'some.file'
        tar_path = self.temp_dir_path / 'some.tar'
        checksums = []
        with tarfile.open(tar_path, mode='w') as tar:
            for __ in range(2):
                some_file.write_bytes(random.randbytes(size))
                tar_info = tar.gettarinfo(name=some_file)
                # todo: for some reason chksum values are both zero... how is this possible?
                checksums.append(tar_info.chksum)
        self.assertEqual(*checksums)


class PatchTests(TarTestCase):
    def test_create_and_apply_patch(self):
        """
        For convenience we test the create_patch/apply_patch cycle in a single test.

        It would probably be better to test these functions independently, but that
        becomes a lot more complicated.
        """
        # create patch
        with self.subTest(msg='create_patch'):
            patch_path = create_patch(
                src_path=self.tarballs['old'], dst_path=self.tarballs['new']
            )
            self.assertTrue(patch_path.exists())
            # a hash object should be present for each modified file
            patch_text = patch_path.read_text()
            self.assertEqual(
                len(DATA[MODIFIED]), patch_text.count(DEFAULT_HASH_ALGORITHM)
            )
        # apply patch
        with self.subTest(msg='create_patch'):
            reconstructed_dst_path = self.temp_dir_path / 'reconstructed.tar'
            apply_patch(
                src_path=self.tarballs['old'],
                patch_path=patch_path,
                dst_path=reconstructed_dst_path,
            )
            self.assertTrue(reconstructed_dst_path.exists())
        # if the tarballs are compressed, we need to decompress them first, before
        # doing a byte-by-byte comparison, because gzip compressed files not
        # reproducible ( only their content is reproducible)
        file_paths = dict(f1=self.tarballs['new'], f2=reconstructed_dst_path)
        for key, path in file_paths.items():
            if path.suffix in COMPRESSION_SUFFIXES:
                decompressed_path = path.with_suffix('')
                with gzip.open(path, mode='rb') as gzfile:
                    decompressed_path.write_bytes(gzfile.read())  # or use shutil...
                file_paths[key] = decompressed_path
        # ensure the original dst tarball and the reconstructed dst tarball are
        # byte-by-byte identical (so use shallow=False)
        #
        # BEWARE: The tarballs are only guaranteed to be identical in these tests. In
        # real life, different tar implementations and configurations are likely to
        # introduce differences. We *can*, however, guarantee that the actual content
        # of the member files is identical. That's what the hashes are for.
        self.assertTrue(filecmp.cmp(**file_paths, shallow=False))

        # FOR DEBUGGING...
        TarDiff(self.tarballs['new'], reconstructed_dst_path).report(show=True)
        with (
            file_paths['f1'].open(mode='rb') as original,
            file_paths['f2'].open(mode='rb') as reconstructed,
        ):
            logging.basicConfig(level=logging.DEBUG)
            compare_bytes(obj_1=original, obj_2=reconstructed)


class PatchMemberTests(TestCase):
    def test_set_hash_verify_hash(self):
        content = b'something'
        member = PatchMember(name='whatever', status=TarDiff.MODIFIED)
        with self.assertRaises(ValueError):
            # hash has not been set
            member.verify_hash(content=content)
        with self.subTest(msg='set_hash'):
            member.set_hash(content=content, algorithm=DEFAULT_HASH_ALGORITHM)
            self.assertEqual(DEFAULT_HASH_ALGORITHM, member.hash[0])
        with self.subTest(msg='verify_hash'):
            try:
                member.verify_hash(content=content)
            except ValueError:
                self.fail(msg='ValueError raised unexpectedly')


class CompareBytesTests(TestCase):
    def test_compare_bytes(self):
        bytes_1 = random.randbytes(2 * CMP_CHUNK_SIZE)
        bytes_2 = random.randbytes(2 * CMP_CHUNK_SIZE)
        self.assertTrue(compare_bytes(io.BytesIO(bytes_1), io.BytesIO(bytes_1)))
        self.assertFalse(compare_bytes(io.BytesIO(bytes_1), io.BytesIO(bytes_2)))


class PatchJSONTests(TestCase):
    def setUp(self):
        header_info = {
            'chksum': 5400,
            'devmajor': 0,
            'devminor': 0,
            'gid': 1000,
            'gname': 'x',
            'linkname': '',
            'mode': 436,
            'mtime': 1706621956,
            'name': './my.file',
            'size': 21,
            'type': b'0',
            'uid': 1000,
            'uname': 'x',
        }
        name = header_info.pop('name')
        tarinfo = tarfile.TarInfo(name=name)
        for key, value in header_info.items():
            setattr(tarinfo, key, value)
        self.patch_member = PatchMember(
            name=name,
            status=TarDiff.MODIFIED,
            status_extra=None,
            diff=b'whatever',
            tarinfo=tarinfo,
        )
        self.patch_member.set_hash(content=b'something')

    def test_default_and_object_hook(self):
        with self.subTest(msg='default'):
            try:
                json_string = json.dumps(self.patch_member, cls=PatchJSON)
            except TypeError as e:
                self.fail(f'unexpected TypeError: {e}')
            self.assertIn('__PatchMember__', json_string)
            self.assertIn('__TarInfo__', json_string)
        with self.subTest(msg='object_hook'):
            obj = json.loads(json_string, object_hook=PatchJSON.object_hook)
            self.assertIsInstance(obj, PatchMember)
            self.assertIsInstance(obj.tarinfo, tarfile.TarInfo)


class WriteModeTests(TestCase):
    def test_write_mode(self):
        cases = [
            # (<path>, <expected mode>)
            (pathlib.Path('file.tar'), 'w'),
            ('file.tar', 'w'),
            ('file.tar.gz', 'w:gz'),
            ('file.tar.bz2', 'w:bz2'),
            ('file.tar.xz', 'w:xz'),
            ('file.unknown_suffix', 'w'),
        ]
        for path, expected_mode in cases:
            with self.subTest(msg=path):
                self.assertEqual(expected_mode, write_mode(path))
