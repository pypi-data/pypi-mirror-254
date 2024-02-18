from typing import Dict, Optional
from .mongo_message_abstract import (
    MongoMessageAbstract,
    MongoResponseAbstract,
)


class MongoUpdate(MongoMessageAbstract):
    def __init__(
        self,
        # collection_name: str,
        query: Dict,
        update: Dict,
        upsert=False,
        update_many=False,
        # finish_confirmation_key: Optional[str] = None,
        **kwargs,
    ) -> None:
        # self.collection_name = collection_name
        self.query = query
        self.update = update
        self.upsert = upsert
        self.update_many = update_many
        # self.finish_confirmation_key = finish_confirmation_key
        super().__init__(**kwargs)


class MongoUpdateResponse(MongoResponseAbstract):
    def __init__(
        self,
        # success: bool,
        # error: Optional[str] = None,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
