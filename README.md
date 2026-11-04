# Cybersecurity FAQ Knowledge Base

## Project overview

This dataset is the FAQ knowledge base for the **FAQ Chatbot Using Retrieval** college team project. It contains 30 cybersecurity questions and concise answers. The chatbot's retrieval pipeline can compare a user's question with the stored FAQ questions and return the answer associated with the best match.

## Dataset files

- `cybersecurity_faq_dataset.csv` — spreadsheet-friendly version.
- `cybersecurity_faq_dataset.json` — JSON version for application integration.

Both files contain the same 30 FAQ records.

## Dataset schema

| Field | Data type | Description |
|---|---|---|
| `id` | Integer | Unique identifier for each FAQ record. |
| `question` | String | The FAQ question that the retrieval system matches against a user's query. |
| `answer` | String | The prepared answer returned when the FAQ is selected. |
| `category` | String | Topic grouping for the FAQ. |
| `keywords` | String | Comma-separated related terms that may support searching, filtering, or future retrieval improvements. |
| `source` | String (URL) | Reference link used when preparing the answer. |

## Categories

The 30 records are organised into these categories:

| Category | Number of FAQs |
|---|---:|
| Fundamentals | 5 |
| Threats | 7 |
| Network Security | 4 |
| Account Security | 3 |
| Defensive Security | 4 |
| Web Application Security | 4 |
| Incident Response | 2 |
| Security Testing | 1 |
| **Total** | **30** |

## Data quality checks

The prepared dataset was checked for:

- 30 records in each file.
- Unique FAQ IDs.
- No empty values in the six dataset fields.
- Consistent field names and record structure across CSV and JSON.
- A source URL recorded for each FAQ.

The source links are references for further reading. Before final academic submission, the team should open and verify each source, confirm that it supports the corresponding answer, and record an access date if required by the instructor.

## Loading the files with Python

### Read the CSV file

```python
import pandas as pd

faqs = pd.read_csv("cybersecurity_faq_dataset.csv")
print(faqs.head())
print("Number of FAQs:", len(faqs))
```

### Read the JSON file

```python
import json

with open("cybersecurity_faq_dataset.json", "r", encoding="utf-8") as file:
    faqs = json.load(file)

print(faqs[0])
print("Number of FAQs:", len(faqs))
```

## How the dataset fits into the chatbot

1. The user submits a question through the chatbot interface.
2. The text-preprocessing module normalises the question.
3. The retrieval module compares the user's question with FAQ questions in this dataset.
4. The similarity-ranking module selects the best candidate.
5. The application returns the answer associated with that FAQ.
6. If the match score is below the agreed confidence threshold, the chatbot should display a fallback response rather than present an uncertain answer as correct.

The preprocessing, TF-IDF/vectorisation, similarity scoring, confidence threshold, and Streamlit interface are implemented by the relevant team members; this dataset supplies the FAQ content for those modules.

## Limitations

- This is a starter knowledge base containing 30 FAQs, not a complete cybersecurity reference.
- Answers are short educational summaries and should not be treated as incident-response, legal, or professional security advice.
- Similarity-based retrieval can return an incorrect match. The team should test relevant, ambiguous, and out-of-scope questions and configure a suitable fallback threshold.
- The FAQ content and source links should be reviewed by the team before final release.

## References used

The dataset includes source URLs in the `source` field of every record. The references include public cybersecurity guidance and terminology resources, such as:

- NIST Computer Security Resource Center: https://csrc.nist.gov/
- NIST SP 800-63-4 glossary: https://pages.nist.gov/800-63-4/sp800-63/glossary/
- OWASP: https://owasp.org/
- UK National Cyber Security Centre guidance: https://www.ncsc.gov.uk/section/advice-guidance/all-topics

Use the individual `source` URL in each FAQ record as the first reference when reviewing that answer.

## Ownership and contribution

**Module:** M2 — FAQ Dataset & Knowledge Base  
**Contributor:** Govind Tiwari  
**Deliverables:** `cybersecurity_faq_dataset.csv`, `cybersecurity_faq_dataset.json`, and this README.

---

Prepared for the college team project **FAQ Chatbot Using Retrieval**.
