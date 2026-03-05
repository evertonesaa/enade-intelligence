import joblib
import numpy as np

model = joblib.load("models/macro_classifier.pkl")


def classify_ml(text: str) -> str:

    probs = model.predict_proba([text])[0]

    max_prob = np.max(probs)

    prediction = model.classes_[np.argmax(probs)]

    # threshold equilibrado
    if max_prob < 0.55:
        return "Unknown"

    return prediction