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

    Parameters
    ----------
    pdf_path : str
        Path to the PDF file.

    Returns
    -------
    str
        Full extracted text from the document.
    """

    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
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

    # regex robusto para capturar QUESTÃO até o número
    pattern = r"QUESTÃO[\s\S]{0,25}?\d+"

    matches = list(re.finditer(pattern, text, re.IGNORECASE))

    questions = []
    seen_numbers = set()

    for i in range(len(matches)):

        header = matches[i].group()

        number_match = re.search(r"\d+", header)

        if not number_match:
            continue

        number = int(number_match.group())

        # evita duplicações como "QUESTÃO 01 QUESTÃO 06"
        if number in seen_numbers:
            continue

        seen_numbers.add(number)

        start = matches[i].start()

        if i < len(matches) - 1:
            end = matches[i + 1].start()
        else:
            end = len(text)

        question_text = text[start:end].strip()

        # identificar tipo
        if re.search(r"discursiva", header, re.IGNORECASE):
            qtype = "DISCURSIVE"
        else:
            qtype = "OBJECTIVE"

        questions.append({
            "question_number": number,
            "question_type": qtype,
            "text": question_text
        })

    # ordenar para garantir sequência correta
    questions = sorted(questions, key=lambda x: x["question_number"])

    return questions