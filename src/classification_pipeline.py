"""
ENADE Intelligence
Question Classification Pipeline
"""

import pandas as pd

from src.classifier import classify_question
from src.bloom import classify_bloom
from src.parser import clean_question_text
from src.classifier_ml import classify_ml


def run_classification():

    df = pd.read_csv("data/processed/enade_dataset.csv")

    macro_areas = []
    blooms = []

    for text in df["text"]:

        clean_text = clean_question_text(text)

        macro = classify_question(clean_text)

        # fallback para ML se keyword não identificar
        if macro == "Unknown":
            macro = classify_ml(clean_text)

        bloom = classify_bloom(clean_text)

        macro_areas.append(macro)
        blooms.append(bloom)

    df["macro_area"] = macro_areas
    df["bloom_level"] = blooms

    output = "data/processed/enade_dataset_classified.csv"

    df.to_csv(output, index=False)

    print("Classification completed")
    print("Output:", output)


if __name__ == "__main__":
    run_classification()