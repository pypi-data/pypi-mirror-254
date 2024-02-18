import glob
import itertools
import os
import re
from collections.abc import Iterable, Iterator
from pathlib import Path
from typing import IO, TypeVar
from xml.etree.ElementTree import Element

import chardet

T = TypeVar("T")


def count_trailing(source: str, chars: str) -> int:
    return len(source) - len(source.rstrip(chars))


def skip(iterable: Iterable[T], count: int) -> Iterator[T]:
    return itertools.islice(iterable, count, None)


def glob_plus(pattern: str, extension: str = "xml") -> list[Path]:
    if "*" in pattern:
        # Path.glob doesn't seem to support absolute paths
        return [Path(p) for p in glob.glob(pattern, recursive=True)]  # noqa: PTH207

    path = Path(pattern)
    if path.is_dir():
        return list(path.glob(f"**/*.{extension}"))

    return [path]


def open_text_file(file_path: str | Path) -> IO[str]:
    enc = guess_encoding(file_path)
    return open(file_path, encoding=enc)


def guess_encoding(file_path: str | Path, byte_count: int = 10000) -> str | None:
    with open(file_path, "rb") as file:
        data = file.read(byte_count)

    result = chardet.detect(data)
    encoding = result["encoding"]
    return "utf-8" if encoding == "ascii" else encoding


def format_xml_tag(elem: Element) -> str:
    if not elem.attrib:
        return f"<{elem.tag}>"
    attributes = " ".join(f'{name}="{value}"' for name, value in elem.attrib.items())
    return f"<{elem.tag} {attributes}>"


def get_app_local_dir() -> Path:
    local_app_data = os.getenv("LOCALAPPDATA")
    if local_app_data:
        return Path(local_app_data) / "anyerplint"
    msg = "Could not find LOCALAPPDATA"
    raise Exception(msg)


def add_linenumbers(cont: str, needles: list[str]) -> list[str]:
    hits: list[list[int]] = [[] for i in range(len(needles))]
    for linenum, line in enumerate(cont.splitlines(), 1):
        for _in, n in enumerate(needles):
            if n in line:
                hits[_in].append(linenum)

    return [
        n + " - line " + ", ".join(map(str, hits[idx]))
        for (idx, n) in enumerate(needles)
    ]


def _replace_with_empty(match: re.Match[str]) -> str:
    comment = match.group(0)
    return "\n" * comment.count("\n")


def replace_commented_xml_with_empty_lines(xml_string: str) -> str:
    comment_pattern = "<!--(.*?)-->"
    return re.sub(comment_pattern, _replace_with_empty, xml_string, flags=re.DOTALL)


def replace_cdata_with_empty_lines(xml_string: str) -> str:
    cdata_pattern = r"<!\[CDATA\[(.*?)\]\]>"
    return re.sub(cdata_pattern, _replace_with_empty, xml_string, flags=re.DOTALL)
