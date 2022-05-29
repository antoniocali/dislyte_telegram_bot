from dataclasses import dataclass
import enum


class EsperClass(enum.IntEnum):
    OFFENSIVO = 1
    CONTROLLO = 2
    DIFENSIVO = 3
    SUPPORTO = 4


@dataclass
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
