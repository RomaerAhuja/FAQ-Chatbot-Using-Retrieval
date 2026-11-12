import json
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

CSV_PATH = BASE_DIR / "data" / "cybersecurity_faq_dataset.csv"
JSON_PATH = BASE_DIR / "data" / "cybersecurity_faq_dataset.json"

REQUIRED_COLUMNS = [
    "id",
    "question",
    "answer",
    "category",
    "keywords",
    "source"
]


def load_faq_data(file_type="csv"):

    if file_type == "csv":

        if not CSV_PATH.exists():
            raise FileNotFoundError("CSV dataset not found.")

        data = pd.read_csv(CSV_PATH)

    elif file_type == "json":

        if not JSON_PATH.exists():
            raise FileNotFoundError("JSON dataset not found.")

        with open(JSON_PATH, "r", encoding="utf-8") as file:
            records = json.load(file)

        data = pd.DataFrame(records)

    else:
        raise ValueError("Unsupported file format.")

    for column in REQUIRED_COLUMNS:

        if column not in data.columns:
            raise ValueError(
                f"Missing required column: {column}"
            )

    if data.empty:
        raise ValueError("Dataset is empty.")

    data = data.copy()

    for column in ["question", "answer", "category"]:
        data[column] = data[column].fillna("").astype(str)

    if data["question"].str.strip().eq("").any():
        raise ValueError("Dataset contains empty questions.")

    if data["answer"].str.strip().eq("").any():
        raise ValueError("Dataset contains empty answers.")

    return data


if __name__ == "__main__":

    faqs = load_faq_data()

    print("FAQ DATASET LOADED SUCCESSFULLY")
    print("Total FAQs:", len(faqs))

    print("\nCategories:")
    print(faqs["category"].value_counts())

    print("\nSample records:")
    print(faqs[["question", "answer"]].head())