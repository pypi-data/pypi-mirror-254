import argparse
import os
import shutil
import urllib.error
import urllib.request
from pathlib import Path

from anyerplint import util


def handle_import(args: argparse.Namespace) -> None:
    """Implement argument handling here.

    Don't put business logic here. Only parse the arguments and pass forward.
    """
    do_import(args.target)


def init_parser(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    """Declare arguments you need here."""
    parser.add_argument("target", nargs="+", help="Zip file to import definitions from")

    parser.set_defaults(func=handle_import)
    return parser


emit = print


def do_import(fnames: list[str]) -> None:
    target_dir = util.get_app_local_dir()
    if not os.path.isdir(target_dir):
        os.makedirs(target_dir)
    for f in fnames:
        if f.startswith("http"):
            lastpart = f.split("/")[-1]
            emit(lastpart)

            if not lastpart.endswith(".zip"):
                lastpart = "downloaded.zip"
            tfile = Path(target_dir) / lastpart
            emit("Fething:", f, "->", tfile)
            try:
                urllib.request.urlretrieve(f, tfile)
            except urllib.error.URLError:
                emit(
                    "Failed to download, ensure your VPN is operational and the target file exists!"
                )
        elif f.endswith(".zip"):
            emit("Copying:", f, "->", target_dir)
            shutil.copy(f, target_dir)
        else:
            emit("Not a zip file:", f)
