import abc
from typing import Any
from home_link.firebase import Firebase
from home_link.parsers import data_types
from home_link.models import Device, Entity
from home_link.parsers.abstract_parser import AbstractParser


class AbstractComponent(abc.ABC):
    def __init__(self, device: Device):
        self.host = device.host
        self.port = device.port
        self.name = device.name
        self.interval = device.interval
        self.entities = device.entities

        self.parser: AbstractParser = data_types().get(device.data_type)()

    @abc.abstractmethod
    async def connect(self):
        pass

    def decode_entity(self, entity_name: str, data: Any) -> Entity:
        return self.parser.parse(entity_name, data)

    def publish_entity(self, new_entity: Entity):
        firebase = Firebase.instance()
        if firebase.is_initialize:
            firebase.publish(self.name, new_entity)
