"""
ENADE Intelligence
PDF Parser
"""

import pdfplumber


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract raw text from a PDF file.
    """

    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text

import re


def extract_questions(text: str):
    """
    Extract individual questions from ENADE text.
    Handles patterns like:
    QUESTÃO 01
    QUESTÃO Discursiva 03
    """

    pattern = r"QUESTÃO\s+(?:Discursiva\s+)?\d+"

    matches = list(re.finditer(pattern, text, re.IGNORECASE))

    questions = []

    for i in range(len(matches)):
        start = matches[i].start()

        if i < len(matches) - 1:
            end = matches[i + 1].start()
        else:
            end = len(text)

        question_text = text[start:end]

        number = re.search(r"\d+", matches[i].group()).group()

        questions.append({
            "question_number": int(number),
            "text": question_text.strip()
        })

    return questions