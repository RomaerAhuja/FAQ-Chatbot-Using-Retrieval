# Project Methodology

## 1. Dataset Collection

The project uses a structured cybersecurity FAQ dataset
stored in CSV and JSON formats.

## 2. Text Preprocessing

Text preprocessing includes:

- Lowercase conversion
- URL removal
- Punctuation removal
- Whitespace normalization

## 3. TF-IDF Retrieval

TF-IDF converts questions into numerical feature vectors.

It is used for keyword-based retrieval.

## 4. Semantic Retrieval

Sentence Transformers generate dense numerical
representations of questions.

Cosine similarity measures semantic closeness.

## 5. Hybrid Retrieval

The system combines lexical and semantic scores.

Hybrid Score = (0.35 × TF-IDF Score)
             + (0.65 × Semantic Score)

## 6. Answer Selection

The system ranks FAQ records using hybrid similarity
and selects the highest-ranked result.

## 7. Fallback Mechanism

If the highest-ranked result is below the configured
similarity threshold, the chatbot returns a fallback
message instead of displaying an answer.

## 8. User Interface

Streamlit provides an interactive interface
for submitting questions and displaying answers.