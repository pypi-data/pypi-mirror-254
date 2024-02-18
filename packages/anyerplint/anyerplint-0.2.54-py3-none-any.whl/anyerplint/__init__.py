from pathlib import Path

if Path(__file__).parent.joinpath("version.txt").exists():
    __version__ = (
        Path(__file__).parent.joinpath("version.txt").read_text(encoding="utf-8")
    )
else:
    __version__ = "0.0.0"
