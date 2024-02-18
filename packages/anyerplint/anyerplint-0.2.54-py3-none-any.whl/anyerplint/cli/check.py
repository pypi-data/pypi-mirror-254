import argparse
import sys

from anyerplint import business_logic


def handle_check(args: argparse.Namespace) -> None:
    """Implement argument handling here.

    Don't put business logic here. Only parse the arguments and pass forward.
    """
    errors = business_logic.do_check(args.lib, args.target, args.teach)
    if errors:
        sys.exit(1)


def init_parser(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    """Declare arguments you need here."""
    parser.add_argument(
        "-l",
        "--lib",
        action="append",
        default=[],
        help="Library path containing variable declarations",
    )

    parser.add_argument("target", nargs="+", help="Target file or directory to check")

    parser.add_argument(
        "--teach",
        action="store_true",
        help="Run in teaching mode (update function list)",
    )

    parser.set_defaults(func=handle_check)
    return parser
