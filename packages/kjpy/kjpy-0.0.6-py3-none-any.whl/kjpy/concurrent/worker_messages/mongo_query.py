from typing import Dict, List, Optional
from .mongo_message_abstract import (
    MongoMessageAbstract,
    MongoResponseAbstract,
)


class MongoQuery(MongoMessageAbstract):
    def __init__(
        self,
        # collection_name: str,
        finish_confirmation_key: str,
        query: Dict,
        project: Dict,
        limit: Optional[int] = 0,
        single=False,
        **kwargs,
    ) -> None:
        # self.collection_name = collection_name
        self.query = query
        self.project = project
        self.limit = limit
        self.single = single
        # self.finish_confirmation_key = finish_confirmation_key
        super().__init__(finish_confirmation_key=finish_confirmation_key, **kwargs)
        # super.__init__(collection_name=collection_name, finish_confirmation_key=finish_confirmation_key)


class MongoQueryResponse(MongoResponseAbstract):
    def __init__(
        self,
        result: Optional[Dict] = None,
        results: Optional[List[Dict]] = None,
        **kwargs,
    ) -> None:
        self.result = result
        self.results = results
        super().__init__(**kwargs)
