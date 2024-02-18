import argparse

from anyerplint import __version__
from anyerplint.cli import check, importcmd, initcmd, parsecmd


def main() -> None:
    main_parser = argparse.ArgumentParser(prog="anyerplint")
    main_parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"anyerplint {__version__}",
    )

    subparsers = main_parser.add_subparsers(
        dest="command",
        title="commands",
        help="Command",
    )
    subparsers.required = True

    check.init_parser(subparsers.add_parser("check", help="Check templates"))
    importcmd.init_parser(
        subparsers.add_parser("import", help="Import definitions from .zip file"),
    )

    initcmd.init_parser(
        subparsers.add_parser("init", help="Initialize vscode integration")
    )

    parsecmd.init_parser(
        subparsers.add_parser("parse", help="Parse and check expressions in templates")
    )

    args = main_parser.parse_args()
    args.func(args)
