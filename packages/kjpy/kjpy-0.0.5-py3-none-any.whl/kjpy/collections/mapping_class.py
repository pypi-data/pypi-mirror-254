from typing import (
    Dict,
    Generic,
    Optional,
    TypeVar,
    ItemsView,
    KeysView,
    ValuesView,
)


Key = TypeVar("Key")
V = TypeVar("V")
MAPPING_TYPE = Dict[Key, V]


class MappingAbstract(Generic[Key, V]):
    def __init__(self, items: Optional[MAPPING_TYPE] = None) -> None:
        self._items: MAPPING_TYPE = items or {}

    # Overwrite this method to handle duplicates
    def _handle_duplicate_key(self, index: Key, value: V):
        self._items[index] = value

    def __setitem__(self, index: Key, value: V):
        if index in self._items:
            self._handle_duplicate_key(index, value)
            return

        self._items[index] = value

    def __getitem__(self, index: Key) -> V:
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def sort_keys(self):
        sorted_items = {}
        sorted_keys = sorted(self._items.keys())
        for key in sorted_keys:
            sorted_items[key] = self._items[key]
        self._items = sorted_items

    def get(self, index: Key) -> Optional[V]:
        if not index in self._items:
            return None
        return self[index]

    def keys(self) -> KeysView[Key]:
        return self._items.keys()

    def items(self) -> ItemsView[Key, V]:
        return self._items.items()

    def values(self) -> ValuesView[V]:
        return self._items.values()

    def __contains__(self, index: Key) -> bool:
        return index in self._items
