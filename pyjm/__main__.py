"""
PYJM

Main class __main__.py

@author mattmusc
"""
import argparse
import os
import sys

from pyjm.json_toolbox import JsonToolbox
from .settings import __version__, __progname__


def build_args_parser():
    """Sets up the arguments parser"""
    description = f"{__progname__} - Python JSON toolbox"

    args_parser = argparse.ArgumentParser(prog=__progname__, description=description)

    args_parser.add_argument("-f", "--file",
                             dest="file", type=str,
                             help="A JSON file.")

    args_parser.add_argument("--stdin",
                             dest="stdin", action="store_true", required=False,
                             help="Read JSON from stdin")

    args_parser.add_argument("-k", "--keep",
                             dest="keep",
                             help="List of keys to select from the json - comma separated.")

    args_parser.add_argument("-v", "--version",
                             dest="version",
                             action="store_true",
                             help=f"Print \"{__progname__}\" version.")

    return args_parser


def parse_args_exit(parser):
    args = parser.parse_args()

    if len(sys.argv) < 1:
        parser.print_help()
        sys.exit(1)

    if args.version:
        parser.exit(0, f"{__progname__} {__version__}\n")


def parse_args(parser):
    toolbox = JsonToolbox([], [])

    args = parser.parse_args()
    if args.keep:
        toolbox = JsonToolbox(args.keep.split(","), [])

    if args.stdin:
        processed = toolbox.process_json_string(sys.stdin)
    else:
        filepath = os.path.abspath(args.file)
        processed = toolbox.process_json_file(filepath)

    print(processed)


def main():
    """ Main method """
    parser = build_args_parser()

    parse_args_exit(parser)
    parse_args(parser)


if __name__ == "__main__":
    main()
