import datetime
from typing import Any
from home_link.models import Entity
from home_link.parsers.abstract_parser import AbstractParser


class Shelly(AbstractParser):

    def parse(self, entity_name: str, value: Any) -> Entity:
        entity = Entity(name=entity_name, value=str(value), unit_of_measure=None, ts=datetime.datetime.now())

        if entity_name.startswith("emeter"):
            if entity_name.endswith("power") or entity_name.endswith("reactive_power"):
                entity.value = float(value)
                entity.unit_of_measure = "W"
            if entity_name.endswith("pf"):
                entity.value = float(value)
                entity.unit_of_measure = None
            if entity_name.endswith("voltage"):
                entity.value = float(value)
                entity.unit_of_measure = "V"
            if entity_name.endswith("total") or entity_name.endswith("total_returned"):
                entity.value = float(value)
                entity.unit_of_measure = "kWh"
            if entity_name.endswith("energy") or entity_name.endswith("returned_energy"):
                entity.value = float(value)
                entity.unit_of_measure = "kWh"
        elif entity_name.startswith("relay") or entity_name.startswith("input") or entity_name.startswith("online"):
            entity.value = value == "true" or value == "on"
            entity.unit_of_measure = None

        return entity
