import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

df = pd.read_csv("data/processed/enade_dataset_classified.csv")

# usar apenas linhas já classificadas
df = df[df["macro_area"] != "Unknown"]

X = df["text"]
y = df["macro_area"]

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(max_iter=1000))
])

model.fit(X, y)

joblib.dump(model, "models/macro_classifier.pkl")

print("Model trained and saved to models/macro_classifier.pkl")