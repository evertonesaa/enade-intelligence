from src.parser import extract_text_from_pdf, extract_questions

pdf_path = "data/raw/enade/2019.pdf"

text = extract_text_from_pdf(pdf_path)

questions = extract_questions(text)

print("Total questions found:", len(questions))
print()
print(questions[0]["text"][:500])