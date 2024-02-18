import argparse
import os
from pathlib import Path

FILE_CONT = """
{
  // See https://go.microsoft.com/fwlink/?LinkId=733558
  // for the documentation about the tasks.json format
  "version": "2.0.0",
  "tasks": [
    {
      "label": "AnyErpLint",
      "type": "process",
      "command": "python",
      "args": [
        "-m",
        "anyerplint",
        "check",
        "${file}"
      ],
      "group": "test",
      "presentation": {
        "reveal": "always",
        "panel": "dedicated"
      }
    }
  ]
}
"""

emit = print


def handle_init(args: argparse.Namespace) -> None:
    init_vscode()


def init_parser(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    """Declare arguments you need here."""
    parser.set_defaults(func=handle_init)
    return parser


def get_vscode_user_tasks_file() -> Path | None:
    appdata = os.getenv("APPDATA")
    if appdata:
        return Path(appdata) / "Code/User/tasks.json"
    return None


def init_vscode() -> None:
    user_tasks = get_vscode_user_tasks_file()
    if not user_tasks:
        emit("Error: Cannot find Visual Studio Code user data folder")
        return
    if user_tasks.exists():
        emit("Error:", user_tasks, "already exists, aborting")
        return

    target = user_tasks
    emit(
        "This command will allow running AnyErpLint check tasks under current directory."
    )
    emit("Press ENTER to create AnyErpLint vscode task at", target)
    input()
    target.parent.mkdir(exist_ok=True)
    target.write_text(FILE_CONT)
    emit(
        "Done! Now run ctrl+shift+P 'Run task' and select AnyErpLint while editing a file."
    )
