import easyocr
from typing import List

reader = easyocr.Reader(lang_list=["en", "it"])


def get_text(image_uri: str) -> List[str]:
    return reader.readtext(image_uri, detail=0)
