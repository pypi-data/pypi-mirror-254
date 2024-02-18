from typing import Any, Callable, Dict, Generic, Optional, Set, TypeVar, Union

from .transform_field_helpers import (
    ensure_list,
    get_recursive_current_object,
    is_object_empty_recursive,
    set_obj_from_key_map,
)

from .json_object_mapper import JsonObjectMapper
from ..collections.serializable_bson_class import SerializableBson
from ..collections.mapping_class import MappingAbstract


class TransformedRecord(SerializableBson, MappingAbstract[Any, Any]):
    pass


TransformClass = TypeVar("TransformClass", bound=TransformedRecord)


class RecordHandler(Generic[TransformClass]):
    def __init__(
        self,
        record: Dict,
        fields_map: Dict[str, JsonObjectMapper],
        custom_handlers=None,
        fields_to_ignore: Optional[Set[str]] = [],
    ) -> None:
        self._response = None
        self.record = record
        self._transformed_record = self._create_transformed_record()
        self._customer_handlers = custom_handlers
        self.fields_to_ignore = fields_to_ignore
        self.fields_map = fields_map
        self._handle_object(self.record)

    @property
    def response(self):
        if self._response is None:
            self._response = self._transformed_record.serialize()
        return self._response

    def _create_transformed_record(self) -> TransformClass:
        return TransformedRecord()

    def _handle_custom_field(self, field_name: str, custom_handler, translated_value):
        self._customer_handlers[custom_handler](field_name, translated_value)

    def _handle_field(
        self, field_translation: JsonObjectMapper, field: str, value, data
    ):
        return_fields_keys = field_translation.return_fields_keys
        try:
            for field_keys in return_fields_keys:
                translated_value = field_translation.get(value)
                object_to_update = get_recursive_current_object(
                    self._transformed_record, field_keys
                )
                last_key = field_keys[-1]
                if field_translation.custom_handler is None:
                    set_obj_from_key_map(object_to_update, last_key, translated_value)
                else:
                    self._handle_custom_field(
                        last_key, field_translation.custom_handler, translated_value
                    )

            if field in data:
                del data[field]
        except Exception as e:
            print(f"Could not translate field {field} with value {value}")
            raise (e)

    def _handle_object(self, data, field_keys="", fields_map=None):
        if fields_map is None:
            fields_map = self.fields_map
        ignore_fields = self.fields_to_ignore
        field_names = list(data.keys())
        for field in field_names:
            if field_keys + field in ignore_fields:
                del data[field]
            else:
                if not field in fields_map:
                    raise Exception(f'Unknown field "{field}" from "{field_keys}"')
                value = data[field]
                field_translations = ensure_list(fields_map[field])
                for field_translation in field_translations:
                    # TODO: Check if is person
                    if type(value) == dict:
                        self._handle_object(
                            data=data[field],
                            field_keys=field_keys + field + ".",
                            fields_map=field_translation,
                        )
                    else:
                        self._handle_field(field_translation, field, value, data)

        if not is_object_empty_recursive(data):
            raise Exception("data not empty", data)
