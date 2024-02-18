from abc import ABC, abstractmethod
import json
import pathlib
import pickle

from bs4 import BeautifulSoup
from bson import json_util

from overrides import overrides

from ..decorators.beautiful_soup_decorators import (
    ensure_soup,
)


def _get_file_extension(filepath):
    return pathlib.Path(filepath).suffix


class _IoHandlerAbstract(ABC):
    def __init__(self, filepath) -> None:
        self.filepath = filepath

    def load_raw(self):
        with open(self.filepath, "r") as f:
            return f.read()

    @abstractmethod
    def to_string(self, data) -> str:
        pass

    @abstractmethod
    def load(self):
        pass

    def save(self, data):
        with open(self.filepath, "w") as f:
            f.write(self.to_string(data))


class _IoHandlerText(_IoHandlerAbstract):
    @overrides
    def to_string(self, data) -> str:
        return str(data)

    @overrides
    def load(self):
        with open(self.filepath, "r") as f:
            return f.read()


class _IoHandlerJson(_IoHandlerAbstract):
    @overrides
    def to_string(self, data) -> str:
        return json.dumps(data, indent=2)

    @overrides
    def load(self):
        with open(self.filepath, "r") as f:
            return json.load(f)


class _IoHandlerHtml(_IoHandlerText):
    pass


class _IoHandlerSoupHtml(_IoHandlerText):
    @ensure_soup
    @overrides
    def load(self):
        with open(self.filepath, "r") as f:
            return BeautifulSoup(f.read(), "html.parser")


class _IoHandlerCsv(_IoHandlerText):
    pass


class _IoHandlerBson(_IoHandlerAbstract):
    @overrides
    def to_string(self, data) -> str:
        return json_util.dumps(data, indent=2)

    @overrides
    def load(self):
        with open(self.filepath, "r") as f:
            return json_util.loads(f.read())


class _IoHandlerPickle(_IoHandlerAbstract):
    @overrides
    def to_string(self, data) -> str:
        return str(pickle.dumps(data))

    @overrides
    def load(self):
        with open(self.filepath, "rb") as f:
            return pickle.load(f)


def get_io_handler(filepath):
    file_extension = _get_file_extension(filepath)
    if file_extension == ".json":
        return _IoHandlerJson(filepath)
    if file_extension == ".bson":
        return _IoHandlerBson(filepath)
    if file_extension == ".html":
        if ".soup.html" in filepath:
            return _IoHandlerSoupHtml(filepath)
        return _IoHandlerHtml(filepath)
    if file_extension == ".csv":
        return _IoHandlerCsv(filepath)
    if file_extension == ".pkl":
        return _IoHandlerPickle(filepath)

    raise Exception(f"Unknown file extension {file_extension}")
