import time
from unittest import TestCase

from tarpatch.cli import _get_parser, SimpleTiming  # noqa


class ParserTests(TestCase):
    def test_get_parser(self):
        """test some basic command line examples"""
        parser = _get_parser()
        for case in [
            '--version',
            '--debug',
            'diff a.tar b.tar',
            'diff a.tar b.tar',
            'create a.tar b.tar',
            'create a.tar b.tar --patch-path c.json',
            'apply a.tar c.json',
            'apply a.tar c.json --dst-path b.tar',
        ]:
            with self.subTest(msg=case):
                args = case.split()
                cmd = args[0]
                options = parser.parse_args(args)

                if cmd.startswith('-'):
                    self.assertTrue(getattr(options, cmd.lstrip('-')))
                else:
                    expected_function_name = '_cmd_' + cmd
                    self.assertEqual(expected_function_name, options.func.__name__)


class SimpleTimingTests(TestCase):
    def test_simple_timing(self):
        sleep_seconds = 0.3
        with SimpleTiming() as t:
            time.sleep(sleep_seconds)
        self.assertAlmostEqual(sleep_seconds, t.seconds_elapsed, delta=0.1)
