import requests
from home_link.components.abstract_component import AbstractComponent
from home_link.models import Device


class Http(AbstractComponent):
    def __init__(self, device: Device):
        super().__init__(device)

    async def connect(self):
        pass
