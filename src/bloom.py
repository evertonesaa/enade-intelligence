"""
ENADE Intelligence
Bloom Taxonomy Module

Defines cognitive levels used to classify ENADE questions
according to Bloom's Taxonomy.
"""

from typing import Dict


BLOOM_LEVELS: Dict[str, dict] = {
    "Remember": {
        "description": "Recall basic concepts and facts.",
        "examples": [
            "define",
            "list",
            "identify",
            "name",
            "recall"
        ]
    },

    "Understand": {
        "description": "Explain ideas or concepts.",
        "examples": [
            "describe",
            "explain",
            "summarize",
            "interpret",
            "classify"
        ]
    },

    "Apply": {
        "description": "Use information in new situations.",
        "examples": [
            "calculate",
            "solve",
            "use",
            "demonstrate",
            "implement"
        ]
    },

    "Analyze": {
        "description": "Draw connections among ideas.",
        "examples": [
            "analyze",
            "compare",
            "differentiate",
            "organize",
            "examine"
        ]
    },

    "Evaluate": {
        "description": "Justify a decision or course of action.",
        "examples": [
            "evaluate",
            "justify",
            "critique",
            "defend",
            "assess"
        ]
    },

    "Create": {
        "description": "Produce new or original work.",
        "examples": [
            "design",
            "construct",
            "develop",
            "formulate",
            "propose"
        ]
    }
}