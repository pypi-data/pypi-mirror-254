from typing import Callable, Optional, Union
import multiprocessing
from multiprocessing.managers import ListProxy, DictProxy

import time

from .worker_messages.mongo_update import MongoUpdate
from .worker_messages.mongo_query import MongoQuery, MongoQueryResponse

from .worker_messages.worker_stats import (
    StepChangeStats,
    WorkerFinishedStats,
    WorkerMetadataInputEndStats,
    WorkerMetadataInputErrorStats,
    WorkerMetadataInputStartStats,
    WorkerStats,
)


class WorkerAbstract(multiprocessing.Process):
    def __init__(
        self,
        config_dict: DictProxy,
        message_list_to_listener: ListProxy,
        message_list_from_worker: ListProxy,
        message_list_to_worker: ListProxy,
        mongo_queue: ListProxy,
        message_mongo_results: DictProxy,
        output_list: ListProxy,
        worker_number: Optional[int] = None,
        handler: Optional[Callable] = None,
        mongo_delay: float = 0.5,
        job_delay: float = 0.1,
    ):
        super().__init__()
        self.config_dict = config_dict
        self.current_step = 0
        self.message_list_from_worker = message_list_from_worker
        self.message_list_to_listener = (
            message_list_to_listener  # This is just used to pass down to new managers
        )
        self.message_list_to_worker = message_list_to_worker
        self.mongo_queue = mongo_queue
        self.message_mongo_results = message_mongo_results
        self.worker_number = worker_number
        self._handler = handler
        self._mongo_delay = mongo_delay
        self._job_delay = job_delay
        self._output_list = output_list

    def set_step_stats(self, step_description: str):
        self.send_stats(StepChangeStats(self.current_step, step_description))
        self.current_step += 1

    def reset_current_step(self):
        self.current_step = 0
        self.set_step_stats("")

    def send_stats(self, stats: WorkerStats) -> None:
        stats.set_worker_number(self.worker_number)
        self.message_list_from_worker.append(stats)

    def query_mongo(self, mongo_query: MongoQuery) -> MongoQueryResponse:
        self.mongo_queue.append(mongo_query)
        return self.get_and_remove_mongo_message(mongo_query)

    def update_mongo(self, mongo_update: MongoUpdate):
        self.mongo_queue.append(mongo_update)

    def wait_for_mongo_update(self, mongo_update: MongoUpdate):
        self.update_mongo(mongo_update)
        self.get_and_remove_mongo_message(mongo_update)

    def send_finished_message(self):
        self.send_stats(WorkerFinishedStats())

    def on_input_start(self):
        self.send_stats(WorkerMetadataInputStartStats())

    def on_input_end(self):
        self.send_stats(WorkerMetadataInputEndStats())

    def on_input_error(self):
        self.send_stats(WorkerMetadataInputErrorStats())

    def get_and_remove_mongo_message(
        self, mongo_update: Union[MongoUpdate, MongoQuery]
    ):
        finish_confirmation_key = mongo_update.finish_confirmation_key
        while True:
            if finish_confirmation_key in self.message_mongo_results:
                results = self.message_mongo_results[finish_confirmation_key]
                del self.message_mongo_results[finish_confirmation_key]
                return results
            time.sleep(self._mongo_delay)

    def get_and_remove_message(self):
        while True:
            if len(self.message_list_to_worker) > 0:
                yield self.message_list_to_worker.pop(0)
            return None

    def run(self):
        while True:
            if (
                "ABORT_IMMEDIATELY" in self.config_dict
                or "WORKERS_FINISHED" in self.config_dict
            ):
                return

            successful_run: bool = self.run_for_job()
            if not successful_run:
                return

    def run_for_job(self) -> bool:
        return True

    def handle_input(self, _input):
        if self._handler is not None:
            return self._handler(_input)

    def handle_output(self, output):
        self._output_list.append(output)


class Worker(WorkerAbstract):
    def __init__(self, job_queue: multiprocessing.Queue, **kwargs):
        self._job_queue = job_queue
        super().__init__(**kwargs)

    # TODO: Rewrite so we can use super().run()
    def run_for_job(self):
        time.sleep(self._job_delay)
        self.reset_current_step()

        _input = self._job_queue.get()
        # self.stats.add_stat(1)
        if _input is None:
            self.send_finished_message()
            return False

        try:
            self.on_input_start()
            output = self.handle_input(_input)
            self.handle_output(output)
            self.on_input_end()
            return True
        except Exception as e:
            try:
                self.handle_error(_input, e)
                self.on_input_error()
            except Exception as e2:
                print("Cannot store exception information", str(e))
                print(str(e2))
                return True

    def handle_error(self, _input, e: Exception):
        pass


class SingleInputWorker(WorkerAbstract):
    def run_for_job(self) -> bool:
        return self.run_continuous()

    def run_continuous(self) -> bool:
        return True
