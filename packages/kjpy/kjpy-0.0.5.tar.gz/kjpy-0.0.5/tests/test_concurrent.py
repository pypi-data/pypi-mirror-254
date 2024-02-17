from src.kjpy.data.unit_test_handler import UnitTestWithTestData
from src.kjpy.concurrent.concurrent_manager import Manager
from src.kjpy.concurrent.workers import Worker


_TEST_DIRECTORY = "run_concurrent"
_DEBUG = True

_RUN_CONCURRENT_WITH_CLASS_RESULTS_FILEPATH = "run_concurrent_with_class_results.json"
_RUN_CONCURRENT_DIRECTLY_RESULTS_FILEPATH = "run_concurrent_directly_results.json"


class ExampleWorker(Worker):
    def handle_input(self, url):
        return url


def example_get_url(url):
    return url


def get_urls():
    return [f"https://google.com/{i}" for i in range(10)]


class TestRunConcurrent(UnitTestWithTestData):
    def setUp(self) -> None:
        return super().setUp(debug=_DEBUG, test_directory=_TEST_DIRECTORY)

    @property
    def shared_test_arguments(self):
        return dict(
            inputs=get_urls(),
            namespace="example_manager",
            num_workers=5,
            mongo_workers_to_create=0,
            mongo_delay=0,
            job_delay=0,
        )

    def test_run_concurrent_with_class(self):
        manager = Manager(WorkerClass=ExampleWorker, **self.shared_test_arguments)
        _output = sorted(manager.output_list)

        self.assertEqualsTestData(_output, _RUN_CONCURRENT_WITH_CLASS_RESULTS_FILEPATH)

    def test_run_concurrent_called_directly(self):
        _output = Manager.run(handler=example_get_url, **self.shared_test_arguments)
        _output = sorted(_output)

        self.assertEqualsTestData(_output, _RUN_CONCURRENT_DIRECTLY_RESULTS_FILEPATH)
