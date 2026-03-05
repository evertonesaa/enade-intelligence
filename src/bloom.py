"""
ENADE Intelligence
Bloom Taxonomy Classifier
"""

import re


def classify_bloom(text: str) -> str:
    """
    Classify question according to Bloom's taxonomy using keyword heuristics.
    """

    text = text.lower()

    apply_keywords = [
        "calcule",
        "determine",
        "considere",
        "suponha",
        "resolva",
        "obtenha"
    ]

    analyze_keywords = [
        "analise",
        "compare",
        "explique",
        "discuta",
        "relacione"
    ]

    remember_keywords = [
        "defina",
        "identifique",
        "cite",
        "liste"
    ]

    for word in apply_keywords:
        if re.search(word, text):
            return "Apply"

    for word in analyze_keywords:
        if re.search(word, text):
            return "Analyze"

    for word in remember_keywords:
        if re.search(word, text):
            return "Remember"

    return "Understand"