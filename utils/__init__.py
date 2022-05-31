from models import EsperClass
from typing import Optional


def text_to_esper_class(text: str) -> Optional[EsperClass]:
    for elem in EsperClass:
        if text.upper() == elem.name:
            return elem

    return None


def normalize(text: str) -> str:
    return text.replace(" ", "").replace("'", "").lower()


ESPER_MAPPING = {
    1: "D-",
    2: "D",
    3: "D+",
    4: "C-",
    5: "C",
    6: "C+",
    7: "B-",
    8: "B",
    9: "B+",
    10: "A-",
    11: "A",
    12: "A+",
    13: "S-",
    14: "S",
    15: "S+"
}
