import os
import pandas as pd

from src.parser import extract_text_from_pdf, extract_questions


def build_dataset():

    data = []

    folder = "data/raw/enade"

    for file in os.listdir(folder):

        if file.endswith(".pdf"):

            year = int(file.replace(".pdf", ""))
            pdf_path = os.path.join(folder, file)

            print(f"Processing {year}...")

            text = extract_text_from_pdf(pdf_path)
            questions = extract_questions(text)

            for q in questions:

                data.append({
                    "year": year,
                    "question_number": q["question_number"],
                    "question_type": q["question_type"],
                    "text": q["text"]
                })

    df = pd.DataFrame(data)

    df = df.sort_values(["year", "question_number"])

    output = "data/processed/enade_dataset.csv"

    df.to_csv(output, index=False)

    print("\nDataset generated successfully")
    print("Total questions:", len(df))
    print("Saved to:", output)


if __name__ == "__main__":
    build_dataset()