import pandas as pd
import json
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset paths
CSV_PATH = BASE_DIR / "data" / "cybersecurity_faq_dataset.csv"
JSON_PATH = BASE_DIR / "data" / "cybersecurity_faq_dataset.json"


def load_faq_data(file_type="csv"):

    """
    Load FAQ dataset from CSV or JSON.
    """

    if file_type == "csv":

        if not CSV_PATH.exists():
            raise FileNotFoundError("CSV dataset not found.")

        data = pd.read_csv(CSV_PATH)

    elif file_type == "json":

        if not JSON_PATH.exists():
            raise FileNotFoundError("JSON dataset not found.")

        with open(JSON_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)

        data = pd.DataFrame(data)

    else:

        raise ValueError("Unsupported file format.")

    # Validate required columns
    required_columns = [
        "id",
        "question",
        "answer",
        "category",
        "keywords",
        "source"
    ]

    for column in required_columns:

        if column not in data.columns:
            raise ValueError(f"Missing required column: {column}")

    return data


if __name__ == "__main__":

    faqs = load_faq_data()

    print("\nFAQ DATASET LOADED SUCCESSFULLY")

    print("Total FAQs:", len(faqs))

    print("\nAvailable Categories:")

    print(faqs["category"].unique())

    print("\nFirst Five FAQs:")

    print(faqs[["question", "answer"]].head())