import re
import string


class TextPreprocessor:

    def __init__(self):
        self.punctuation_table = str.maketrans(
            "",
            "",
            string.punctuation
        )

    def clean_text(self, text):

        if not isinstance(text, str):
            raise TypeError("Input must be a string.")

        # Convert to lowercase
        text = text.lower()

        # Remove URLs
        text = re.sub(r"https?://\S+|www\.\S+", "", text)

        # Remove punctuation
        text = text.translate(self.punctuation_table)

        # Remove extra whitespace
        text = re.sub(r"\s+", " ", text).strip()

        return text


if __name__ == "__main__":

    processor = TextPreprocessor()

    test_questions = [
        "WHAT IS CYBERSECURITY???",
        "What is Malware?",
        "Explain   Network Security!!",
        "WHAT IS PHISHING???",
        "Visit https://example.com for information"
    ]

    print("\nTEXT PREPROCESSING RESULTS\n")

    for question in test_questions:

        cleaned = processor.clean_text(question)

        print("Original:", question)
        print("Cleaned :", cleaned)
        print("-" * 50)