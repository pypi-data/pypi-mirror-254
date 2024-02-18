from typing import TypeVar, Union

T = TypeVar("T")
RecursiveList = list[Union[T, "RecursiveList[T]"]]
