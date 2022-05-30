from models import EsperClass
from typing import Optional


def text_to_esper_class(text: str) -> Optional[EsperClass]:
    for elem in EsperClass:
        if text.upper() == elem.name:
            return elem

    return None


def normalize(text: str) -> str:
    return text.replace(" ", "").replace("'", "").lower()
