from functools import wraps
from typing import Any, Callable

from bs4 import BeautifulSoup, Tag, NavigableString


def ensure_soup(func: Callable) -> Callable[..., Tag]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if not isinstance(response, Tag):
            raise Exception("Expected response to be a soup tag")
        return response

    return wrapper


def single_attribute(func: Callable) -> Callable[..., str]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if not response:
            return ""
        if type(response) == list:
            assert len(response) == 1
            return response[0]
        return response

    return wrapper
