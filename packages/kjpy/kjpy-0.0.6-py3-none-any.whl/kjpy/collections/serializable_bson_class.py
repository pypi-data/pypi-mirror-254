import datetime

from overrides import overrides

from .serializable_class import Serializable


class SerializableBson(Serializable):
    @overrides
    def _serialize_special_item(self, item, item_type):
        if item_type == datetime.datetime:
            return item
        return super()._serialize_special_item(item, item_type)
