from src.parser import extract_text_from_pdf

pdf_path = "data/raw/enade/2019.pdf"

text = extract_text_from_pdf(pdf_path)

print(text[:1000])