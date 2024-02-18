import os
import unittest

from .misc import ensure_directory_exists, UNIT_TEST_DATA_DIR

from .data_handler import get_io_handler, DataHandler


_test_directories_cache = {}


def _create_full_test_directory(test_directory):
    if test_directory in _test_directories_cache:
        return _test_directories_cache[test_directory]
    full_directory = os.path.join(UNIT_TEST_DATA_DIR, test_directory)
    ensure_directory_exists(full_directory)
    _test_directories_cache[test_directory] = full_directory
    return full_directory


class UnitTestWithTestData(unittest.TestCase):
    def setUp(self, debug: bool, test_directory: str) -> None:
        self.full_test_dir = _create_full_test_directory(test_directory)
        self._debug = debug
        return super().setUp()

    def _get_test_data_filepath(self, filename):
        return os.path.join(self.full_test_dir, filename)

    def load_test_data(self, filename):
        filepath = self._get_test_data_filepath(filename)
        return DataHandler(filepath=filepath).load()

    def assertEqualsTestData(self, data_results, filename):
        filepath = self._get_test_data_filepath(filename)

        data_handler = DataHandler(debug=self._debug, filepath=filepath)
        data_handler.save_if_debug(data_results)
        expected_response = data_handler.load()
        self.assertEqual(expected_response, data_results)

    def assertStringifyEqualsTestData(self, data_results, filename):
        filepath = self._get_test_data_filepath(filename)

        data_handler = DataHandler(debug=self._debug, filepath=filepath)
        data_handler.save_if_debug(data_results)
        expected_response = data_handler.load_raw()

        actual_response = data_handler.to_string(data_results)
        self.assertEqual(expected_response, actual_response)


def save_test_data(filepath, data):
    io_handler = get_io_handler(filepath)
    io_handler.save(data)
