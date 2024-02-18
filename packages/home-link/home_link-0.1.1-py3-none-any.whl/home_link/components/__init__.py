from home_link.components.abstract_component import AbstractComponent
from home_link.components.http import Http
from home_link.components.mqtt import Mqtt

CLASS_COMPONENTS: list[AbstractComponent] = [Http, Mqtt]


def platforms() -> dict[str, AbstractComponent]:
    return {class_component.__name__.lower(): class_component for class_component in CLASS_COMPONENTS}
