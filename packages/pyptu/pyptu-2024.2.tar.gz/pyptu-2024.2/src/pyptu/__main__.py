#!/usr/bin/env python3

'''
Command-line tool for parsing PTU files.
'''

import argparse
import logging
import pathlib
import sys


from pyptu import PTUParser


LOGGER = logging.getLogger(__name__)


def parse_args(args=None):
    '''
    Parse command-line arguments.

    Args:
        args:
            The arguments. If None, arguments are read from sys.argv.

    Returns:
        The parsed command-line arguments.
    '''
    parser = argparse.ArgumentParser(description='Extract PTU data to standard files.')
    parser.add_argument('path', type=pathlib.Path, help='A path to a PTU file.')
    parser.add_argument('dir', type=pathlib.Path, help='A path to an output directory.')
    parser.add_argument(
        '--encoding',
        help=f'''
            Specify the input filetype encoding. It must be an encoding type
            supported by Python. If not given, the following encodings will be
            tried, in order: {", ".join(PTUParser.ENCODINGS)}.
            '''
    )
    return parser.parse_args(args=args)


def main(args=None):
    '''
    Extract data from a PTU file to standard files.

    Args:
        args:
            Passed through to :py:func:`pyptu.__main__.parse_args`.
    '''
    pargs = parse_args(args=args)
    parser = PTUParser(pargs.path, encoding=pargs.encoding)
    parser.load()
    parser.save(pargs.dir)


def run_main(args=None):
    '''
    Wrapper around main() with logging configuration and basic error handling.
    '''
    logging.basicConfig(
        style='{',
        format='[{asctime}] {levelname} {message}',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.INFO
    )
    try:
        sys.exit(main(args=args))
    except KeyboardInterrupt:
        pass
    except IOError as err:
        sys.exit(str(err))


if __name__ == '__main__':
    run_main()
