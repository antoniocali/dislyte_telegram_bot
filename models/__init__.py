from dataclasses import dataclass
from typing import List, Dict
import enum
import operator
from collections import Counter


class EsperClass(enum.IntEnum):
    OFFENSIVO = 1
    CONTROLLO = 2
    DIFENSIVO = 3
    SUPPORTO = 4


@dataclass(frozen=True, eq=True)
class Esper:
    name: str
    alternative: str
    story: int
    cube: int
    kronos: int
    apep: int
    fafnir: int
    war_def: int
    war_atk: int
    esper_class: EsperClass


class Stats:
    def __init__(self, espers: List[Esper]):
        self.espers: List[Esper] = espers
        self.story: int = sum([esper.story for esper in espers])
        self.cube: int = sum([esper.cube for esper in espers])
        self.kronos: int = sum([esper.kronos for esper in espers])
        self.apep: int = sum([esper.apep for esper in espers])
        self.fafnir: int = sum([esper.fafnir for esper in espers])
        self.war_def: int = sum([esper.war_def for esper in espers])
        self.war_atk: int = sum([esper.war_atk for esper in espers])
        self.classes: List[str] = [esper.esper_class.name for esper in espers]

    def get_worse(self, attribute: str) -> Esper:
        worst = sorted(self.espers, key=operator.attrgetter(attribute))
        return worst[0]

    def get_classes(self) -> Dict[str, int]:
        counter = Counter(self.classes)
        return dict(counter)