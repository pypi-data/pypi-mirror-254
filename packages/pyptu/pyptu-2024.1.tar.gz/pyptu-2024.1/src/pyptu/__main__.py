#!/usr/bin/env python3

'''
Command-line tool for parsing PTU files.
'''

import argparse
import json
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
        help='''
            Specify the input filetype encoding. It must be a an encoding type
            supported by Python. If not given, standard encodings will be tried.
            '''
    )
    return parser.parse_args(args=args)


def _try_encodings(path, first=None):
    '''
    Try different standard encodings until one succeeds or the last fails.

    Args:
        path:
            The input path.

        first:
            An optional user encoding to try first.

    Returns:
        The loaded parser on success, else None.
    '''
    encodings = ['utf-8', 'windows-1252']
    if first:
        first = first.strip().lower()
        if first not in encodings:
            encodings.insert(0, first)

    for encoding in encodings:
        try:
            parser = PTUParser(path, encoding=encoding)
            parser.load()
            return parser
        except LookupError as err:
            LOGGER.error('%s', err)
        except UnicodeDecodeError as err:
            LOGGER.error('Failed to load file using %s encoding: %s', encoding, err)
        # TODO
        # Determine which exceptions may be raised by other encodings.
        except Exception as err:
            LOGGER.error('Failed to load file using %s encoding: %s', encoding, err)

    return None


def main(args=None):
    '''
    Extract data from a PTU file to standard files.

    Args:
        args:
            Passed through to :py:func:`pyptu.__main__.parse_args`.
    '''
    pargs = parse_args(args=args)
    parser = _try_encodings(pargs.path, first=pargs.encoding)
    if parser is None:
        return f'Failed to load {pargs.path}'
    dpath = pargs.dir.resolve()
    dpath.mkdir(parents=True, exist_ok=True)

    with (dpath / 'headers.json').open('w', encoding='utf-8') as handle:
        json.dump(parser.header, handle, indent=True, sort_keys=True)

    parser.photons.to_csv(dpath / 'photons.csv', index=False)
    parser.markers.to_csv(dpath / 'markers.csv', index=False)
    parser.overflows.to_csv(dpath / 'overflows.csv', index=False)


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
