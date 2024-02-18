from typing import Generic, TypeVar

T = TypeVar('T')


def only_truthy_items(array: list[T]) -> list[T]:
    return [x for x in array if x]
