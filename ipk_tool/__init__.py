import argparse
import sys

from .extract_ipk import ExtractedIpkHandler

COMMANDS = {
    "extract"
    "build",
}


def parse_arguments(args):
    parser = argparse.ArgumentParser(
        prog="IPK tool",
        description="Manage IPK",
        epilog="Help me....")
    parser.add_argument("command",
                        help="build or extract",
                        choices=COMMANDS)
    return parser.parse_args(args)


def main(args=None):
    arguments = parse_arguments(args)
    if arguments.command == "extract":
        from .extract_ipk import main
    elif arguments.command == "build":
        from .build_ipk import main
    else:
        raise ValueError("Unknown command")
    main(args=sys.argv[2:])


if __name__ == "__main__":
    main()
