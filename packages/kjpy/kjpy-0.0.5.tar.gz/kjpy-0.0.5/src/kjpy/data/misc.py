import os


_DATA_DIR = os.path.join(".", "data")
_TEST_DATA_DIR = os.path.join(_DATA_DIR, "test_data")
# TODO: This should be configurable
UNIT_TEST_DATA_DIR = os.path.join(_TEST_DATA_DIR, "python", "unit_tests")

WORKER_METADATA_DIRECTORY = os.path.join(_DATA_DIR, "workers_metadata")


def ensure_directory_exists(dir):
    if not os.path.exists(dir):
        try:
            os.makedirs(dir)
        except FileExistsError:
            pass
