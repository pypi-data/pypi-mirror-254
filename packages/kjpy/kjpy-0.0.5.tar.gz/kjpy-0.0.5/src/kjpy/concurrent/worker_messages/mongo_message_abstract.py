from typing import Dict, Optional


class MongoMessageAbstract:
    def __init__(
        self,
        collection_name: str,
        finish_confirmation_key: str,
    ) -> None:
        self.collection_name = collection_name
        self.finish_confirmation_key = finish_confirmation_key


class MongoResponseAbstract:
    def __init__(
        self,
        success: bool,
        error: Optional[str] = None,
    ) -> None:
        self.success = success
        self.error = error
