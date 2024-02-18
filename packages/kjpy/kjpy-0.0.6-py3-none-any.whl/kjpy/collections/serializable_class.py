from typing import Any, Dict, Optional, Union, List
from .sequence_class import SequenceAbstract
from .mapping_class import MappingAbstract

_RAW_SERIALIZABLE_TYPES = set([int, float, str, bool])


def _is_visible_key(dict_key: str):
    return dict_key[0] != "_"


class Serializable:
    def _pre_serialize(self):
        pass

    def _serialize_items(self, items):
        return [self._serialize_item(item) for item in items]

    def _serialize_dict(self, item_dict):
        serialized_dict = {}
        for key, value in item_dict.items():
            if _is_visible_key(key):
                serialized_dict[key] = self._serialize_item(value)
        return serialized_dict

    # Overwrite
    def _serialize_special_item(self, item, item_type):
        raise Exception(f'Could not serialize item: "{item}" with type "{item_type}"')

    def _serialize_item(self, item):
        if item is None:
            return None
        item_type = type(item)

        if item_type in _RAW_SERIALIZABLE_TYPES:
            return item
        if isinstance(item, Serializable):
            return item.serialize()
        if item_type in (list, set):
            return self._serialize_items(item)
        if item_type == dict:
            return self._serialize_dict(item)

        return self._serialize_special_item(item, item_type)

    @property
    def _serializable_hidden_keys(self) -> Dict[str, Any]:
        return {}

    @property
    def _custom_serialized_fields(self) -> Optional[Dict[str, Any]]:
        return None

    @property
    def _serializable_dict(self):
        hidden_keys_map = self._serializable_hidden_keys
        serializable_dict = {}
        raw_dict = self.__dict__
        other_fields = self._custom_serialized_fields
        if other_fields is not None:
            raw_dict = {**raw_dict, **other_fields}
        for key in raw_dict.keys():
            if _is_visible_key(key):
                serializable_dict[key] = raw_dict[key]
            elif key in hidden_keys_map:
                new_key_name = hidden_keys_map[key]
                serializable_dict[new_key_name] = raw_dict[key]

        return serializable_dict

    # @property
    # def is_empty(self) -> bool:
    #     if isinstance(self, SequenceAbstract) or isinstance(self, MappingAbstract):
    #         return len(self) == 0
    #     return False

    # def __bool__(self):
    #     return not self.is_empty

    def serialize_mapping_items_only(self) -> Dict:
        if not isinstance(self, MappingAbstract):
            raise Exception("Can only serialize if class extends 'MappingAbstract'")
        return self._serialize_dict(self._items)

    def serializeMapping(self):
        # For MappingAbstract -> If neither _serializable_hidden_keys nor _custom_serialized_fields are overwritten, just the ._items are returned
        serializable_dict = self._serializable_dict
        if len(serializable_dict) == 0 and isinstance(self, MappingAbstract):
            # Flattened
            serializable_dict = self._items
        return self._serialize_dict(serializable_dict)

    def serialize(self) -> Union[Dict, List]:
        self._pre_serialize()
        if isinstance(self, SequenceAbstract):
            return self._serialize_items(self)
        if isinstance(self, MappingAbstract):
            return self.serializeMapping()
        return self._serialize_dict(self._serializable_dict)
