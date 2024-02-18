from typing import Any, Dict, List, Optional, Union
import time
import multiprocessing
from multiprocessing.managers import ListProxy, DictProxy

from pymongo import MongoClient
from ..worker_messages.mongo_update import (
    MongoUpdate,
    MongoUpdateResponse,
)
from ..worker_messages.mongo_query import MongoQuery, MongoQueryResponse


class MongoException(Exception):
    pass


class ExactlyOnResultNotFound(MongoException):
    def __init__(self, results_count) -> None:
        message = f"Expected exactly one result but found {results_count}"
        super().__init__(message)


_DB_NAME = "scrapeComics"


def connect_db():
    client = MongoClient(maxPoolSize=10000)
    db = client.get_database(_DB_NAME)
    return db


class DBListener(multiprocessing.Process):
    def __init__(
        self,
        listener_number: int,
        config_dict: DictProxy,
        message_list_to_listener: ListProxy,
        message_list_to_worker: ListProxy,
        mongo_queue: ListProxy,
        # mongo_query_queue: ListProxy,
        message_mongo_results: DictProxy,
        # message_mongo_query_results: DictProxy,
        num_workers: int,
    ) -> None:
        super().__init__()
        self.listener_number = listener_number
        self.config_dict = config_dict
        self.message_list_to_listener = message_list_to_listener
        self.message_list_to_worker = message_list_to_worker
        self.mongo_queue = mongo_queue
        # self.mongo_query_queue = mongo_query_queue
        self.message_mongo_results = message_mongo_results
        # self.message_mongo_query_results = message_mongo_query_results
        self.num_workers = num_workers
        self._db = None

    def connect_to_db(self):
        time_to_wait = self.num_workers / 10
        # print(f'Waiting {time_to_wait} seconds for other processes to warm up.')
        time.sleep(time_to_wait)
        self._db = connect_db()

        return self._db

    @property
    def db(self):
        if self._db is None:
            return self.connect_to_db()

        return self._db

    # TODO: Do we need this?
    def send_message(self, message: Any) -> None:
        self.message_list_to_worker.append(message)

    def send_mongo_finished(self, finish_confirmation_key: str) -> None:
        self.message_mongo_results[finish_confirmation_key] = MongoUpdateResponse(True)

    def send_mongo_results(
        self, finish_confirmation_key: str, results: MongoQueryResponse
    ) -> None:
        self.message_mongo_results[finish_confirmation_key] = results

    def get_query_mongo_results(self, message: MongoQuery) -> MongoQueryResponse:
        db_connection = self.db[message.collection_name]
        query = message.query
        project = message.project
        limit = message.limit
        single = message.single

        args = {}
        if query:
            args["filter"] = query
        if project:
            args["projection"] = project
        cursor = db_connection.find(**args)
        if limit:
            cursor = cursor.limit(limit)

        results = list(cursor)

        if single:
            try:
                if len(results) != 1:
                    raise ExactlyOnResultNotFound(len(results))
                return MongoQueryResponse(result=results[0], success=True)
            except MongoException as e:
                return MongoQueryResponse(error=str(e), success=False)

        return MongoQueryResponse(results=results, success=True)

    def query_mongo(self, message: MongoQuery):
        finish_confirmation_key = message.finish_confirmation_key
        try:
            mongo_response = self.get_query_mongo_results(message)
            # if finish_confirmation_key is not None:
            self.send_mongo_results(finish_confirmation_key, mongo_response)

        except MongoException as e:
            pass

    def update_mongo(self, message: MongoUpdate):
        update_args = {
            "filter": message.query,
            "update": message.update,
            "upsert": message.upsert,
        }

        db_connection = self.db[message.collection_name]

        if message.update_many:
            db_connection.update_many(**update_args)
        else:
            db_connection.update_one(**update_args)

        finish_confirmation_key = message.finish_confirmation_key
        if finish_confirmation_key is not None:
            self.send_mongo_finished(finish_confirmation_key)

    def write_messages_count(self):
        filepath = f"db_listener_messages_{self.listener_number}.txt"
        with open(filepath, "w") as f:
            f.write(str(len(self.mongo_queue)))

    def run_continuously(self):
        i = 0
        while True:
            if "ABORT_IMMEDIATELY" in self.config_dict:
                return
            if len(self.mongo_queue) > 0:
                i += 1
                if i % 10 == 0:
                    self.write_messages_count()

                # The queue may already be empty at this point
                try:
                    mongo_message = self.mongo_queue.pop(0)
                    if isinstance(mongo_message, MongoUpdate):
                        self.update_mongo(mongo_message)
                    elif isinstance(mongo_message, MongoQuery):
                        self.query_mongo(mongo_message)
                    else:
                        raise Exception("Unknown mongo_message")
                    # mongo_message = self.mongo_query_queue.pop(0)
                    # self.query_mongo(mongo_message)
                except IndexError:
                    # TODO: Log how many errors
                    pass
            # Only exit here once queue is empty
            elif "WORKERS_FINISHED" in self.config_dict:
                self.write_messages_count()
                return

            time.sleep(0.0001)

    def run(self):
        try:
            self.run_continuously()
        except Exception as e:
            with open("BOOO.txt", "w") as f:
                f.write(str(e))
            self.run()
