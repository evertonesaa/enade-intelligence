from src.parser import extract_text_from_pdf, extract_questions

pdf_path = "data/raw/enade/2019.pdf"

text = extract_text_from_pdf(pdf_path)

questions = extract_questions(text)

print("Total questions:", len(questions))
print()

for q in questions[:5]:
    print(q["question_number"], q["question_type"])