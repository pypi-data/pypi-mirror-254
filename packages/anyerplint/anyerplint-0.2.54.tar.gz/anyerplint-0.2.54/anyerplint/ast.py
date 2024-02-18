from dataclasses import dataclass
from typing import Union

Expression = Union[str, "FuncCall"]


@dataclass
class FuncCall:
    name: str
    args: list[Expression]
