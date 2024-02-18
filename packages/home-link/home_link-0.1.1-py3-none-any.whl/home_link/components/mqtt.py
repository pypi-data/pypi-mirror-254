import logging
import re
import paho.mqtt.client as mqtt
from home_link.components.abstract_component import AbstractComponent
from home_link.models import Device


class Mqtt(AbstractComponent):
    def __init__(self, device: Device):
        super().__init__(device)
        self.interval = None
        self.topic = device.topic

    async def connect(self):
        client = mqtt.Client()
        client.on_connect = self._on_connect
        client.on_message = self._on_message
        client.connect(self.host, self.port, 60)
        client.loop_start()

    def _on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            logging.info("mqtt broker subscribe topic: %s device: %s", self.topic, self.name)
            client.subscribe(f"{self.topic}/#")
        else:
            logging.error("error connect to mqtt broker host: %s port: %s", self.host, self.port)

    def _on_message(self, client, userdata, msg):
        logging.info("mqtt message received! topic: %s device: %s value: %s", msg.topic, self.name, msg.payload)
        entity_name: str = msg.topic.replace(self.topic, "")
        if re.match("/", entity_name):
            paths = filter(lambda n : len(n) > 0, entity_name.split("/"))
            entity_name = ".".join(paths)
        data = msg.payload
        if isinstance(data, bytes):
            data = data.decode()
        new_entity = self.decode_entity(entity_name, data)
        self.publish_entity(new_entity)
