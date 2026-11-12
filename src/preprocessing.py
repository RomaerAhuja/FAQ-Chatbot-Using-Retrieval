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

        text = text.lower()

        text = re.sub(
            r"https?://\S+|www\.\S+",
            "",
            text
        )

        text = text.translate(
            self.punctuation_table
        )

        text = re.sub(
            r"\s+",
            " ",
            text
        )

        return text.strip()


if __name__ == "__main__":

    processor = TextPreprocessor()

    examples = [
        "WHAT IS CYBERSECURITY???",
        "What is Malware?",
        "Explain Network Security!!",
        "Visit https://example.com"
    ]

    for example in examples:

        print("Original:", example)
        print("Processed:", processor.clean_text(example))
        print()