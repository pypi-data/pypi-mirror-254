from typing import Callable, List, Generic, Optional, TypeVar, Union
from abc import ABC, abstractmethod


V = TypeVar("V")


class SequenceAbstract(Generic[V]):
    def __init__(self, items: Optional[List[V]] = None) -> None:
        self._items: List[V] = items or []
        self._index = 0
        self.sort = self._items.sort

    def append(self, item: V):
        self._items.append(item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        self._index = 0
        return self

    def __getitem__(self, index: int) -> V:
        return self._items[index]

    @property
    def items(self):
        return self._items

    def __next__(self) -> V:
        items = self.items
        try:
            result = items[self._index]
        except IndexError:
            raise StopIteration
        self._index += 1
        return result


class UniqueSequenceAbstract(SequenceAbstract[V], ABC):
    @property
    def _unique_items(self) -> List[V]:
        items = super().items
        unique_keys = set()
        unique_items = []
        for item in items:
            unique_key = self._unique_key(item)
            if unique_key not in unique_keys:
                unique_items.append(item)
                unique_keys.add(unique_key)

        return self._preserialize(unique_items)
        return unique_items

    # Overwrite
    def _preserialize(self, items: List[V]):
        return items

    @abstractmethod
    def _unique_key(self, item) -> Union[str, int]:
        pass

    @property
    def items(self):
        return self._unique_items
