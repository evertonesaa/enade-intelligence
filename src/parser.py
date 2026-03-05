"""
ENADE Intelligence
PDF Parser Module

Responsible for:
1. Extracting raw text from ENADE PDFs
2. Identifying and separating individual questions
3. Classifying question type (DISCURSIVE or OBJECTIVE)
"""

import re
import pdfplumber
from typing import List, Dict


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract raw text from an ENADE PDF.
    """

    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                page_text = clean_pdf_artifacts(page_text)
                text += page_text + "\n"

    return text


def extract_questions(text: str) -> List[Dict]:
    """
    Extract individual questions from ENADE text.

    Handles patterns such as:
    - QUESTÃO 01
    - QUESTÃO Discursiva 03
    - QUESTÃO\nDiscursiva 02

    Returns structured question objects.
    """

    pattern = r"QUESTÃO\s*(Discursiva\s*)?\d+"

    matches = list(re.finditer(pattern, text, re.IGNORECASE))

    questions = []
    seen_numbers = set()

    for i in range(len(matches)):

        header = matches[i].group()

        number_match = re.search(r"\d+", header)

        if not number_match:
            continue

        number = int(number_match.group())

        if number in seen_numbers:
            continue

        seen_numbers.add(number)

        start = matches[i].start()

        if i < len(matches) - 1:
            end = matches[i + 1].start()
        else:
            end = len(text)

        question_text = clean_question_text(text[start:end])

        if re.search(r"discursiva", header, re.IGNORECASE):
            qtype = "DISCURSIVE"
        else:
            qtype = "OBJECTIVE"

        questions.append({
            "question_number": number,
            "question_type": qtype,
            "text": question_text
        })

    questions = sorted(questions, key=lambda x: x["question_number"])

    return questions


def clean_question_text(text: str) -> str:
    """
    Clean question text by removing headers like:

    QUESTÃO 01
    QUESTÃO Discursiva 02
    """

    text = re.sub(r"QUESTÃO\s+(Discursiva\s+)?\d+", "", text, flags=re.IGNORECASE)

    text = re.sub(r"\(cid:\d+\)", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()

def clean_question_text(text: str) -> str:
    """
    Clean extracted ENADE question text.

    Removes headers like:
    QUESTÃO 10
    QUESTÃO Discursiva 2
    """

    text = re.sub(r"QUESTÃO\s+(Discursiva\s+)?\d+", "", text, flags=re.IGNORECASE)

    # remove espaços duplicados
    text = re.sub(r"\s+", " ", text)

    return text.strip()

def clean_pdf_artifacts(text: str) -> str:
    """
    Remove PDF artifacts like (cid:123)
    """

    text = re.sub(r"\(cid:\d+\)", " ", text)

    return text