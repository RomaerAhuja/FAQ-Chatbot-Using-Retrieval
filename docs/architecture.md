# CyberFAQ System Architecture

## Overview

CyberFAQ is a hybrid retrieval-based FAQ chatbot
designed to answer cybersecurity-related questions.

## Architecture Components

1. User Interface
2. Text Preprocessing
3. FAQ Dataset
4. TF-IDF Retrieval
5. Semantic Retrieval
6. Hybrid Similarity Calculation
7. Answer Ranking
8. Confidence Threshold
9. Response Generation

## Data Flow

User Query
    |
    v
Preprocessing
    |
    v
TF-IDF Retrieval + Semantic Retrieval
    |
    v
Hybrid Similarity Calculation
    |
    v
Ranking
    |
    v
Threshold Validation
    |
    +---- Relevant Match ----> FAQ Answer
    |
    +---- No Relevant Match -> Fallback

## Technology Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Sentence Transformers
- PyTorch
- Streamlit