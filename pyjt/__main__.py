"""
PYJT

Main class __main__.py

@author mattmusc
"""
import argparse
import logging
import os
import sys

from pyjt.json_toolbox import JsonToolbox
from .settings import __version__, __progname__, LOGGING_LEVEL


def build_args_parser():
    """Sets up the arguments parser"""
    description = f"{__progname__} - Python JSON toolbox"

    args_parser = argparse.ArgumentParser(prog=__progname__, description=description)

    args_parser.add_argument("-f", "--file",
                             dest="file", type=str,
                             help="A JSON file.")

    args_parser.add_argument("-k", "--keep",
                             dest="keep",
                             help="List of keys to select from the json - comma separated.")

    args_parser.add_argument("-r", "--remove",
                             dest="remove",
                             help="List of keys to ignore from the json - comma separated.")

    args_parser.add_argument("-v", "--version",
                             dest="version",
                             action="store_true",
                             help=f"Print \"{__progname__}\" version.")

    return args_parser


def parse_args_exit(parser):
    """Parses direct exit arguments"""
    args = parser.parse_args()

    if len(sys.argv) < 1:
        parser.print_help()
        sys.exit(1)

    if args.version:
        parser.exit(0, f"{__progname__} {__version__}\n")


def parse_args(parser):
    """Parse program options"""
    toolbox = JsonToolbox([], [])

    args = parser.parse_args()
    if args.keep:
        toolbox.to_keep = args.keep.split(",")

    if args.remove:
        toolbox.to_remove = args.remove.split(",")

    if args.file:
        filepath = os.path.abspath(args.file)
        processed = toolbox.process_json_file(filepath)

    else:
        processed = toolbox.process_json_string(sys.stdin)

    print(processed)
    print()


def setup_logging():
    logging.basicConfig(format=("[%(levelname)s\033[0m] "
                                "\033[1;31m%(module)s\033[0m: "
                                "%(message)s"),
                        level=LOGGING_LEVEL,
                        stream=sys.stdout)
    logging.addLevelName(logging.ERROR, '\033[1;31mE')
    logging.addLevelName(logging.INFO, '\033[1;32mI')
    logging.addLevelName(logging.WARNING, '\033[1;33mW')


def main():
    """ Main method """
    setup_logging()

    parser = build_args_parser()

    parse_args_exit(parser)
    parse_args(parser)


if __name__ == "__main__":
    main()
