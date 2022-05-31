import json
from models import Esper
from utils import text_to_esper_class, normalize
from typing import Optional, List

class Config:
    def __init__(self, source: str):
        self.source = str
        conf = json.load(open(source))
        espers = conf["espers"]
        self.espers: List[Esper] = [Esper(
            name=elem["name"],
            alternative=elem["alternative"],
            story=elem["story"],
            cube=elem["cube"],
            kronos=elem["kronos"],
            apep=elem["apep"],
            fafnir=elem["fafnir"],
            war_def=elem["war_def"],
            war_atk=elem["war_atk"],
            esper_class=text_to_esper_class(elem["class"]),
        ) for elem in espers]
        t = [(elem.name, elem.alternative) for elem in self.espers]
        self.set_full = set([item for sublist in t for item in sublist])
        self.set = set([elem.name for elem in self.espers])

    def to_set_full(self):
        return list(map(lambda x: x.lower(), self.set_full))

    def to_set(self):
        return list(map(lambda x: x.lower(), self.set))

    def get_esper(self, name: str) -> Optional[Esper]:
        for elem in self.espers:
            if normalize(elem.name) == normalize(name) or normalize(elem.alternative) == normalize(name):
                return elem

        return None
