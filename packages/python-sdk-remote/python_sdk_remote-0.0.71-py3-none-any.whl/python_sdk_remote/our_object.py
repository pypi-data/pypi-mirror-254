import json
from abc import ABC, abstractmethod

from .mini_logger import MiniLogger


class OurObject(ABC):
    def __init__(self, **kwargs):
        INIT_METHOD_NAME = '__init__'
        MiniLogger.start(INIT_METHOD_NAME, object={'kwargs': kwargs})
        self.kwargs = kwargs
        MiniLogger.end(INIT_METHOD_NAME, object={'kwargs': kwargs})

    @abstractmethod
    def get_name(self):
        raise NotImplementedError(
            "Subclasses must implement the 'get_name' method.")

    def get(self, attr_name: str):
        GET_METHOD_NAME = 'get'
        MiniLogger.start(GET_METHOD_NAME, object={'attr_name': attr_name})
        arguments = getattr(self, 'kwargs', None)
        value = arguments.get(attr_name, None)
        MiniLogger.end(GET_METHOD_NAME, object={'attr_name': attr_name})
        return value

    def get_all_arguments(self):
        return getattr(self, 'kwargs', None)

    def to_json(self) -> str:
        return json.dumps(self.__dict__)

    def from_json(self, json_string: str) -> 'OurObject':
        FROM_JSON_METHOD_NAME = 'from_json'
        MiniLogger.start(FROM_JSON_METHOD_NAME,
                         object={'json_string': json_string})
        self.__dict__ = json.loads(json_string)
        MiniLogger.end(FROM_JSON_METHOD_NAME,
                       object={'json_dict': self.__dict__})
        return self

    def __eq__(self, other) -> bool:
        if not isinstance(other, OurObject):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)
