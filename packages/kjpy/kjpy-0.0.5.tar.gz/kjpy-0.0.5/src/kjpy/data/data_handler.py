import inspect
import os

from .data_io_handler import get_io_handler
from .misc import ensure_directory_exists


def _get_directory_of_caller(stack_position=2):
    filepath = (inspect.stack()[stack_position])[1]
    abs_path_of_caller = os.path.abspath(filepath)
    directory_of_1py = os.path.dirname(abs_path_of_caller)
    return directory_of_1py


def _create_test_data_filepath(directory_of_caller: str, test_filename: str):
    test_data_dir = os.path.join(directory_of_caller, "test_data")
    ensure_directory_exists(test_data_dir)
    return os.path.join(test_data_dir, test_filename)


class DataHandler:
    def __init__(self, test_filename=None, debug=False, filepath=None) -> None:
        if filepath is None and type(test_filename) == str:
            directory_of_caller = _get_directory_of_caller()

            filepath = _create_test_data_filepath(directory_of_caller, test_filename)

        self.debug = debug
        self.io_handler = get_io_handler(filepath)

    def load(self):
        return self.io_handler.load()

    def load_raw(self):
        return self.io_handler.load_raw()

    def to_string(self, data):
        return self.io_handler.to_string(data)

    def save_if_debug(self, data):
        if self.debug:
            return self.io_handler.save(data)
