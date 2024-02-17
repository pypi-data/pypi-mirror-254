from dateutil import parser
import re


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
