import abc
from typing import Any
from home_link.models import Entity


class AbstractParser(abc.ABC):

    @abc.abstractmethod
    def parse(self, entity_name: str, value: Any) -> Entity:
        pass
