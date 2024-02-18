from typing import Dict, List, Union
from dateutil import parser
import re


def ensure_list(items) -> List[any]:
    if type(items) == list:
        return items
    return [items]


def to_date(value):
    if not value:
        return None
    return parser.parse(value)


def array_to_string(value):
    if not value:
        return None

    if type(value) == str:
        return value

    if type(value) == list:
        if len(value) != 1:
            raise Exception(
                f'Expected to find exactly one record but found {len(value)} with value: "{str(value)}"'
            )
        return str(value[0])

    raise Exception(f'Unknown type "{type(value)}" for value: {str(value)}')


def to_array(value, sep="\\s{2,}| & | and | \\/ | ,"):
    if not value:
        return []

    values = re.split(sep, value)
    return [value.strip() for value in values]


def to_string(value):
    if value is None:
        return None
    return str(value)


def handle_page_count(value):
    if not value:
        return None
    match = re.search("[0-9]+", value)
    if not match:
        return None

    return int(match.group())


def handle_go_collect_title(title):
    return re.sub("\\s+", " ", title).replace("Report", "").strip()


def expand_list_strings(items):
    if not items:
        return []
    all_items = []
    for item in items:
        sub_items = to_array(item, sep=",")
        for sub_item in sub_items:
            all_items.append(sub_item)
    return all_items


# Accesses an object at given keys (all keys except last), creates key if does not exist
def get_recursive_current_object(data, keys: List[str]):
    if len(keys) < 2:
        return data
    for key in keys[:-1]:
        if not key in data:
            data[key] = {}
        data = data[key]
    return data


def set_obj_from_key_map(data, key: str, value: Union[str, List]) -> None:
    if not key in data:
        data[key] = value
        return

    if type(data[key]) != list:
        data[key] = value
    else:
        if type(value) == str:
            data[key].append(value)
        elif type(value) == list:
            for subvalue in value:
                if not subvalue in data[key]:
                    data[key].append(subvalue)


def is_object_empty_recursive(data: Dict):
    for field_name in data:
        value = data[field_name]
        if type(value) == dict:
            if not is_object_empty_recursive(value):
                return False
        else:
            return False
    return True
