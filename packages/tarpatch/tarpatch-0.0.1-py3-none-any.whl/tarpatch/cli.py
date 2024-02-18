import argparse
import logging
import sys
from time import perf_counter

import tarpatch

logger = logging.getLogger(__name__)

TAR_SUFFIXES = ', '.join(
    [tarpatch.TAR_SUFFIX]
    + [tarpatch.TAR_SUFFIX + suffix for suffix in tarpatch.COMPRESSION_SUFFIXES]
)

HELP = dict(
    version='print package version and exit',
    debug='enable debugging mode',
    diff='print a summary of the differences between two tarballs',
    create='create a patch from two tarballs',
    apply='reconstruct a tarball using a tarball and a patch',
    src_path=f'path to the source tarball ({TAR_SUFFIXES})',
    dst_path=f'path to the destination tarball ({TAR_SUFFIXES})',
    patch_path=f'path to the patch file ({tarpatch.PATCH_SUFFIX})',
)


def main(args=None):
    # default to --help
    if args is None:
        args = sys.argv[1:] or ['--help']

    # parse command line arguments
    options = _get_parser().parse_args(args=args)

    # show version
    if options.version or options.debug:
        print(f'tarpatch version: {tarpatch.__version__}')
        if options.version:
            exit(0)

    # enable debugging
    if options.debug:
        tarpatch.DEBUG = True
        logging.basicConfig(level=logging.DEBUG, stream=sys.stdout, force=True)

    # process command
    try:
        options.func(options)
    except Exception:  # noqa
        logger.exception(f'Failed to process command: {args}')


def _get_parser() -> argparse.ArgumentParser:
    """
    define parsers

    https://docs.python.org/3/library/argparse.html#sub-commands
    """
    # add basic options, e.g. version, debug (these are handled in main())
    parser = argparse.ArgumentParser(description='Binary patches for tarballs.')
    parser.add_argument(
        '-v', '--version', action='store_true', required=False, help=HELP.get('version')
    )
    parser.add_argument(
        '-d', '--debug', action='store_true', required=False, help=HELP.get('debug')
    )
    # subparsers are used because the required arguments differ per command
    subparsers = parser.add_subparsers()
    # diff
    subparser_diff = subparsers.add_parser('diff', help=HELP.get('diff'))
    subparser_diff.set_defaults(func=_cmd_diff)
    subparser_diff.add_argument('src_path', action='store', help=HELP.get('src_path'))
    subparser_diff.add_argument('dst_path', action='store', help=HELP.get('dst_path'))
    # create
    subparser_create = subparsers.add_parser('create', help=HELP.get('create'))
    subparser_create.set_defaults(func=_cmd_create)
    subparser_create.add_argument('src_path', action='store', help=HELP.get('src_path'))
    subparser_create.add_argument('dst_path', action='store', help=HELP.get('dst_path'))
    subparser_create.add_argument(
        '--patch-path', action='store', required=False, help=HELP.get('patch_path')
    )
    # apply
    subparser_apply = subparsers.add_parser('apply', help=HELP.get('apply'))
    subparser_apply.set_defaults(func=_cmd_apply)
    subparser_apply.add_argument('src_path', action='store', help=HELP.get('src_path'))
    subparser_apply.add_argument(
        'patch_path', action='store', help=HELP.get('patch_path')
    )
    subparser_apply.add_argument(
        '--dst-path', action='store', required=False, help=HELP.get('dst_path')
    )
    return parser


def _cmd_diff(options: argparse.Namespace):
    logger.debug(f'command diff: {vars(options)}')
    with SimpleTiming():
        print('generating diff...')
        tarpatch.TarDiff(old=options.src_path, new=options.dst_path).report(show=True)
        print('\ndone.')


def _cmd_create(options: argparse.Namespace):
    logger.debug(f'command create: {vars(options)}')
    with SimpleTiming():
        print('creating patch...')
        patch_path = tarpatch.create_patch(
            src_path=options.src_path,
            dst_path=options.dst_path,
            patch_path=options.patch_path,
        )
        print(f'patch created: {patch_path}')


def _cmd_apply(options: argparse.Namespace):
    logger.debug(f'command apply: {vars(options)}')
    with SimpleTiming():
        print('applying patch...')
        dst_path = tarpatch.apply_patch(
            src_path=options.src_path,
            dst_path=options.dst_path,
            patch_path=options.patch_path,
        )
        print(f'patch applied: {dst_path}')


class SimpleTiming(object):
    """a context manager that prints the time elapsed"""
    def __enter__(self):
        self.seconds_start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.seconds_elapsed = perf_counter() - self.seconds_start
        print(f'time elapsed: {self.seconds_elapsed:.1f} seconds')
