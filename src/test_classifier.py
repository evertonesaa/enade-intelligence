from src.classifier import classify_question

question = """
Calculate the heat transfer coefficient for a tubular heat exchanger
considering convective heat transfer.
"""

result = classify_question(question)

print(result)