from abc import ABC, abstractmethod

from logger_local.MetaLogger import ABCMetaLogger


class Item(ABC, metaclass=ABCMetaLogger):
    @abstractmethod
    def get_id(self):
        pass
