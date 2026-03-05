"""
ENADE Intelligence
Question Classification Engine
"""

from src.taxonomy import MACRO_AREAS
from src.bloom import BLOOM_LEVELS


def classify_macro_area(text: str):

    text = text.lower()

    for area, topics in MACRO_AREAS.items():
        for topic in topics:
            if topic.lower() in text:
                return area

    return "Unknown"


def classify_bloom(text: str):

    text = text.lower()

    for level, data in BLOOM_LEVELS.items():
        for keyword in data["examples"]:
            if keyword in text:
                return level

    return "Unknown"


def classify_question(question_text: str):

    return {
        "macro_area": classify_macro_area(question_text),
        "bloom_level": classify_bloom(question_text)
    }