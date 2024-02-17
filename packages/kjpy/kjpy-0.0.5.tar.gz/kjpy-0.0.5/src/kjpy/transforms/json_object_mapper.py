from typing import Callable, List, Optional, Union


def _ensure_list(items) -> List[str]:
    if type(items) == list:
        return items
    return [items]


def _split_keys(item: str) -> List[str]:
    return item.split(".")


class JsonObjectMapper:
    def __init__(
        self,
        return_field_names: Union[str, List[str]],
        clean_fn: Optional[Callable] = None,
        is_person_field=False,
        is_publisher_field=False,
        is_variations_field=False,
        is_variation_of_field=False,
    ):
        self.is_person_field = is_person_field
        self.is_publisher_field = is_publisher_field
        self.is_variations_field = is_variations_field
        self.is_variation_of_field = is_variation_of_field
        self.return_fields: List[str] = _ensure_list(return_field_names)
        self.return_fields_keys: List[List[str]] = [
            _split_keys(f) for f in self.return_fields
        ]
        self.clean_fn = clean_fn

    def get(self, value):
        if self.clean_fn:
            return self.clean_fn(value)

        return value
