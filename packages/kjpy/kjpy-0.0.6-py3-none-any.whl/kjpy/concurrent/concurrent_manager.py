from typing import Callable, Dict, List, Optional, Type, DefaultDict, TypeVar
import warnings
import multiprocessing
from multiprocessing import Manager as ProcessManager
from multiprocessing.managers import ListProxy, DictProxy

from .listeners.db_listener import DBListener
from .listeners.listener import Listener
from .listeners.listener_message_hub import ListenerMessageHub
from .workers import SingleInputWorker, Worker

warnings.simplefilter("ignore", UserWarning)
# warnings.simplefilter('ignore', InsecureRequestWarning)
WorkerSubclass = TypeVar("WorkerSubclass", bound=Worker)
SingleInputWorkerSubclass = TypeVar(
    "SingleInputWorkerSubclass", bound=SingleInputWorker
)


class DefaultWorker(Worker):
    pass


# class ManagerParams(DefaultDict):
#         namespace = str
#         inputs = List
#         WorkerClass = Type[WorkerSubclass]
#         num_workers = int
#         ListenerClass = Optional[Type[Listener]]
#         listener_class_kw_args=Dict
#         message_list_to_listener = Optional[ListProxy]
#         message_list_to_worker = Optional[ListProxy]
#         message_mongo_results = Optional[DictProxy]
#         continuous_workers = List[Type[SingleInputWorkerSubclass]]
#         mongo_workers_to_create = int
#         worker_kw_args = Dict
#         handler = Optional[Callable]
#         mongo_delay = float
#         job_delay = float
class Manager:
    # message_list = None
    def __init__(
        self,
        #     **kwargs: Unpack[ManagerParams]
        # ) -> None:
        namespace: str,
        inputs: List,
        WorkerClass: Type[WorkerSubclass] = DefaultWorker,
        num_workers: int = 0,
        ListenerClass: Optional[Type[Listener]] = None,
        listener_class_kw_args={},
        message_list_to_listener: Optional[ListProxy] = None,
        message_list_to_worker: Optional[ListProxy] = None,
        message_mongo_results: Optional[DictProxy] = None,
        continuous_workers: List[Type[SingleInputWorkerSubclass]] = [],
        mongo_workers_to_create: int = 1,
        worker_kw_args: Dict = {},
        handler: Optional[Callable] = None,
        mongo_delay: float = 0.5,
        job_delay: float = 0.1,
    ) -> None:
        self.namespace = namespace
        jobs = []
        continuous_jobs = []
        job_queue = multiprocessing.Queue()
        # https://docs.python.org/3/library/multiprocessing.html#proxy-objects
        self.manager = ProcessManager()
        if message_list_to_listener is None:
            message_list_to_listener = self.manager.list()
        if message_list_to_worker is None:
            message_list_to_worker = self.manager.list()
        if message_mongo_results is None:
            message_mongo_results = self.manager.dict()
        message_mongo_results["mongo_queue_finished"] = {}

        self._output = _output = self.manager.list()

        # TODO: Should this be an optional param?
        mongo_queue = self.manager.list()

        config_dict = self.manager.dict()

        message_lists_from_workers = []

        for continuous_worker in continuous_workers:
            message_list_from_worker = self.manager.list()
            message_lists_from_workers.append(message_list_from_worker)
            p = continuous_worker(
                message_list_to_listener=message_list_to_listener,
                message_list_from_worker=message_list_from_worker,
                config_dict=config_dict,
                message_list_to_worker=message_list_to_worker,
                mongo_queue=mongo_queue,
                message_mongo_results=message_mongo_results,
                output_list=_output,
                mongo_delay=mongo_delay,
                job_delay=job_delay,
            )
            continuous_jobs.append(p)
            p.start()

        for i in range(num_workers):
            message_list_from_worker = self.manager.list()
            message_lists_from_workers.append(message_list_from_worker)
            p = WorkerClass(
                job_queue=job_queue,
                handler=handler,
                config_dict=config_dict,
                message_list_from_worker=message_list_from_worker,
                message_list_to_listener=message_list_to_listener,
                message_list_to_worker=message_list_to_worker,
                mongo_queue=mongo_queue,
                message_mongo_results=message_mongo_results,
                worker_number=i,
                output_list=_output,
                mongo_delay=mongo_delay,
                job_delay=job_delay,
                **worker_kw_args,
            )
            jobs.append(p)
            p.start()
        if ListenerClass is not None:
            message_hub = ListenerMessageHub(
                config_dict=config_dict,
                message_list_to_listener=message_list_to_listener,
                message_lists_from_workers=message_lists_from_workers,
            )
            jobs.append(message_hub)
            message_hub.start()

            listener = ListenerClass(
                namespace=self.namespace,
                config_dict=config_dict,
                message_list_to_listener=message_list_to_listener,
                message_list_to_worker=message_list_to_worker,
                num_workers=num_workers,
                input_total_count=len(inputs),
                **listener_class_kw_args,
            )
            jobs.append(listener)
            listener.start()

        for i in range(mongo_workers_to_create):
            db_listener = DBListener(
                listener_number=i,
                config_dict=config_dict,
                message_list_to_listener=message_list_to_listener,
                message_list_to_worker=message_list_to_worker,
                mongo_queue=mongo_queue,
                message_mongo_results=message_mongo_results,
                num_workers=num_workers,
            )
            jobs.append(db_listener)
            db_listener.start()

        # Send None for each worker to check and quit.
        count = 0
        len_inputs = len(inputs)
        for _input in inputs:
            count += 1

            if count == len_inputs or (count % 10 == 0):
                with open("job_queue_items.txt", "w") as f:
                    f.write(f"{count} \t {len_inputs}")

            job_queue.put(_input)

        for j in jobs:
            job_queue.put(None)

        all_jobs = continuous_jobs + jobs
        for j in all_jobs:
            j.join()

    @staticmethod
    def run(*args, **kwargs):
        manager = Manager(*args, **kwargs)
        return manager.output_list

    @property
    def output_list(self):
        return list(self._output)
