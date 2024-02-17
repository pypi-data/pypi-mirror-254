# import unittest
# from typing import Any

# from kjpy.collections.serializable_class import Serializable
# from kjpy.collections.sequence_class import SequenceAbstract
# from kjpy.collections.mapping_class import MappingAbstract


# class SerializableAnyAccess(Serializable):
#     def __delattr__(self, __name: str) -> None:
#         del self.__dict__[__name]

#     def __setattr__(self, __name: str, __value: Any) -> None:
#         if not isinstance(self, MappingAbstract) or __name[0] == "_":
#             super().__setattr__(__name, __value)
#             return

#         self._items[__name] = __value

#     def __getattr__(self, __name: str) -> Any:
#         value = self.__dict__.get(__name)
#         if value is None:
#             value = self.__class__()
#             self.__setattr__(__name, value)
#         return value


# class TestSerializableAnyAccess(unittest.TestCase):
#     def test_random_access_object(self):
#         obj = SerializableAnyAccess()
#         obj.test = True
#         obj.name = "bob"
#         obj.people.jo = "person"
#         del obj.test
#         self.assertEqual(obj.serialize(), {"name": "bob", "people": {"jo": "person"}})
