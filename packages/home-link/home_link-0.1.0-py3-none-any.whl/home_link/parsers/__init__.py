from home_link.parsers.abstract_parser import AbstractParser
from home_link.parsers.json import Json
from home_link.parsers.shelly import Shelly
from home_link.parsers.value import Value


CLASS_PARSERS: list[AbstractParser] = [Value, Json, Shelly]


def data_types() -> dict[str, AbstractParser]:
    return {class_parser.__name__.lower(): class_parser for class_parser in CLASS_PARSERS}
