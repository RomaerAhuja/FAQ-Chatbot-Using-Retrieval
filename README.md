# 🔐 CyberFAQ — Hybrid Retrieval-Based Cybersecurity FAQ Chatbot

**CyberFAQ** is a hybrid retrieval-based chatbot developed to answer frequently asked questions related to cybersecurity.

The system combines traditional keyword-based information retrieval using **TF-IDF** with semantic search using **Sentence Transformers**. It uses a pretrained model hosted on Hugging Face to generate sentence embeddings and identify relevant answers from a structured cybersecurity knowledge base.

The application provides an interactive web interface using Streamlit, allowing users to submit cybersecurity-related questions and receive relevant answers with reference sources.

### 🌐 Live Application

**[Launch CyberFAQ](https://faq-chatbot-using-retrieval.streamlit.app/)**

---

## 🚀 Key Features

- Structured cybersecurity FAQ knowledge base.
- CSV and JSON dataset support.
- Text preprocessing and normalization.
- TF-IDF-based keyword retrieval.
- Semantic retrieval using Sentence Transformers.
- Pretrained Hugging Face model integration.
- Dense sentence embedding generation.
- Cosine similarity calculation.
- Hybrid similarity scoring.
- Ranked FAQ retrieval.
- Configurable similarity threshold.
- Fallback response mechanism.
- Basic multiple-question handling.
- Interactive Streamlit web interface.
- Conversation history.
- Source references for retrieved answers.
- Automated testing using Pytest.
- Retrieval evaluation using Top-1 and Top-3 accuracy.

---

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Keyword Retrieval | TF-IDF |
| Semantic Retrieval | Sentence Transformers |
| Pretrained Model | all-MiniLM-L6-v2 |
| Model Hosting | Hugging Face |
| Similarity Calculation | Cosine Similarity |
| Machine Learning | Scikit-learn, PyTorch |
| Frontend | Streamlit |
| Testing | Pytest |
| Dataset Formats | CSV, JSON |
| Version Control | Git, GitHub |
| Deployment | Streamlit Community Cloud |

---

## 🤗 Hugging Face Pretrained Model

CyberFAQ uses the pretrained **all-MiniLM-L6-v2** Sentence Transformer model hosted on Hugging Face.

### Model Information

| Property | Details |
|---|---|
| Model Name | all-MiniLM-L6-v2 |
| Repository | sentence-transformers/all-MiniLM-L6-v2 |
| Platform | Hugging Face |
| Architecture | MiniLM |
| Embedding Dimension | 384 |
| Maximum Sequence Length | 256 tokens |
| Framework | Sentence Transformers |
| Primary Application | Semantic Text Similarity |

**Official Model Repository:**

[Hugging Face — all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)

### Model Integration

The model is integrated using the Sentence Transformers library.

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)
```

The model converts FAQ questions and user queries into dense numerical vector embeddings.

These embeddings are compared using cosine similarity to identify questions with similar semantic meaning, even when their wording differs.

### Model Download and Caching

The pretrained model is automatically downloaded from Hugging Face when loaded for the first time.

An internet connection is required for the initial download. The model is subsequently cached and reused during later executions.

The pretrained model weights are not stored in the GitHub repository.

---

## 📁 Project Structure

```text
FAQ-Chatbot-Using-Retrieval/
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   ├── cybersecurity_faq_dataset.csv
│   └── cybersecurity_faq_dataset.json
│
├── docs/
│   ├── architecture.md
│   └── methodology.md
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── retrieval.py
│   ├── semantic_retrieval.py
│   ├── similarity.py
│   ├── chatbot.py
│   └── evaluation.py
│
├── tests/
│   ├── __init__.py
│   ├── test_data_loader.py
│   ├── test_preprocessing.py
│   ├── test_retrieval.py
│   ├── test_similarity.py
│   └── test_chatbot.py
│
├── .gitignore
├── requirements.txt
├── packages.txt
└── README.md
```

---

## ⚙️ Installation and Setup

Follow these steps to run CyberFAQ locally.

### 1. Clone the Repository

```bash
git clone https://github.com/RomaerAhuja/FAQ-Chatbot-Using-Retrieval.git
```

### 2. Navigate to the Project Directory

```bash
cd FAQ-Chatbot-Using-Retrieval
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```cmd
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 5. Upgrade pip

```bash
python -m pip install --upgrade pip
```

### 6. Install Dependencies

```bash
pip install -r requirements.txt
```

### Dependencies

The project uses the following Python packages:

- pandas
- numpy
- scikit-learn
- sentence-transformers
- torch
- streamlit
- pytest

---

## ▶️ Running the Application

Ensure that your virtual environment is activated and that you are in the project root directory.

Execute:

```bash
python -m streamlit run app/streamlit_app.py
```

Open the application in your browser:

```text
http://localhost:8501
```

---

## 🧠 System Architecture

CyberFAQ follows a hybrid information retrieval architecture.

### Processing Pipeline

```text
                 USER QUESTION
                       |
                       v
               TEXT PREPROCESSING
                       |
                       v
              +---------------------+
              |  RETRIEVAL ENGINE   |
              +---------------------+
                       |
                +------+------+
                |             |
                v             v
             TF-IDF       SEMANTIC SEARCH
            RETRIEVAL       (MINILM)
                |             |
                v             v
           KEYWORD         SENTENCE
           VECTORS         EMBEDDINGS
                |             |
                +------+------+
                       |
                       v
                HYBRID SCORING
                       |
                       v
                  FAQ RANKING
                       |
                       v
                THRESHOLD CHECK
                       |
                 +-----+-----+
                 |           |
                 v           v
             RELEVANT     NO MATCH
              ANSWER      FALLBACK
```

### Architecture Components

1. **User Interface:** Accepts cybersecurity questions through Streamlit.
2. **Data Loader:** Loads the structured FAQ knowledge base.
3. **Text Preprocessing:** Normalizes text before keyword retrieval.
4. **TF-IDF Retrieval:** Identifies lexical similarity between questions.
5. **Semantic Retrieval:** Generates sentence embeddings using the pretrained Hugging Face model.
6. **Cosine Similarity:** Measures similarity between numerical representations.
7. **Hybrid Scoring:** Combines lexical and semantic similarity scores.
8. **FAQ Ranking:** Ranks available answers according to their hybrid scores.
9. **Threshold Validation:** Checks whether the retrieved result meets the configured similarity threshold.
10. **Response Generation:** Returns the selected FAQ answer or a fallback response.

---

## 🔍 Retrieval Methodology

CyberFAQ combines two information retrieval approaches.

### 1. TF-IDF Retrieval

Term Frequency-Inverse Document Frequency (TF-IDF) represents text as numerical feature vectors.

It identifies lexical similarities between the user's query and questions stored in the FAQ dataset.

The implementation uses:

- Unigrams and bigrams.
- Sublinear term frequency scaling.
- Scikit-learn's `TfidfVectorizer`.

### 2. Semantic Retrieval

Semantic retrieval uses the pretrained Sentence Transformer model to generate dense sentence embeddings.

Unlike traditional keyword matching, semantic embeddings help identify similarities in meaning between differently worded questions.

The model used is:

`sentence-transformers/all-MiniLM-L6-v2`

### 3. Cosine Similarity

Cosine similarity measures the similarity between two vector representations.

It is used to compare the user's query embedding with stored FAQ embeddings.

### 4. Hybrid Retrieval

The system combines TF-IDF and semantic similarity scores.

The current implementation uses the following weighted formula:

```text
Hybrid Score = (0.35 × TF-IDF Score)
             + (0.65 × Semantic Score)
```

Where:

- TF-IDF Weight = 0.35
- Semantic Weight = 0.65

These weights are configurable in the similarity engine.

The combined score is used to rank FAQ records and select the highest-ranked candidate.

---

## 📊 Dataset

CyberFAQ uses a structured cybersecurity FAQ dataset maintained in CSV and JSON formats.

### Dataset Attributes

| Field | Description |
|---|---|
| id | Unique FAQ identifier |
| question | Frequently asked cybersecurity question |
| answer | Corresponding answer |
| category | Cybersecurity topic category |
| keywords | Associated keywords |
| source | Reference URL for the answer |

The dataset contains cybersecurity topics organized into categories such as:

- Fundamentals
- Threats
- Network Security
- Other cybersecurity topics represented in the dataset.

The knowledge base can be expanded by adding new FAQ records following the existing structure.

---

## 🛡️ Fallback Mechanism

The chatbot includes a fallback mechanism for queries that do not meet the configured similarity threshold.

Instead of returning an answer for every input, the system can respond:

> Sorry, I couldn't find a relevant answer in my knowledge base.

This helps reduce irrelevant responses when a query does not sufficiently match the available FAQ records.

**Note:** The similarity threshold is an experimental parameter that should be calibrated using representative in-domain and out-of-domain queries. Similarity scores are not probabilities of correctness.

---

## 🧪 Testing

CyberFAQ uses Pytest for automated testing.

Run the complete test suite:

```bash
python -m pytest tests -v
```

### Testing Coverage

The test suite covers:

- CSV dataset loading.
- JSON dataset loading.
- Text preprocessing.
- Lowercase conversion.
- Punctuation removal.
- Whitespace normalization.
- URL removal.
- TF-IDF initialization.
- Query vector transformation.
- Similarity calculation.
- FAQ ranking.
- Chatbot response generation.
- Empty input handling.
- Invalid input handling.
- Multiple-question processing.

---

## 📈 Retrieval Evaluation

The project includes an evaluation module to assess retrieval performance.

| Metric | Description |
|---|---|
| Top-1 Accuracy | Percentage of queries where the first retrieved FAQ matches the expected FAQ |
| Top-3 Accuracy | Percentage of queries where the expected FAQ appears among the first three retrieved results |

Evaluation requires a separately prepared test dataset containing queries and manually verified expected FAQ IDs.

Actual performance metrics should be reported only after executing the evaluation against that test dataset.

---

## ☁️ Deployment

CyberFAQ is deployed using **Streamlit Community Cloud**.

### Live Application

[https://faq-chatbot-using-retrieval.streamlit.app/](https://faq-chatbot-using-retrieval.streamlit.app/)

### Deployment Configuration

| Property | Configuration |
|---|---|
| Platform | Streamlit Community Cloud |
| Source Repository | GitHub |
| Branch | main |
| Main Application File | app/streamlit_app.py |
| Model Provider | Hugging Face |

### Deployment Steps

1. Push the project to GitHub.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Sign in using GitHub.
4. Select Create App.
5. Choose the CyberFAQ repository.
6. Select the `main` branch.
7. Set the application entry point to:

```text
app/streamlit_app.py
```

8. Deploy the application.

The initial deployment may take additional time because dependencies and the pretrained Hugging Face model need to be downloaded.

---

## 🔮 Future Scope

Potential future enhancements include:

- Expanding the cybersecurity FAQ knowledge base.
- Improving semantic retrieval accuracy.
- Advanced query understanding.
- Better multi-intent question handling.
- Context-aware conversational interactions.
- Retrieval-Augmented Generation (RAG).
- Multilingual question answering.
- User feedback collection.
- Advanced retrieval evaluation metrics.
- Integration with external cybersecurity knowledge sources.

---

## 👨‍💻 Author

**Romaer Ahuja**

**GitHub Repository:**

[FAQ Chatbot Using Retrieval](https://github.com/RomaerAhuja/FAQ-Chatbot-Using-Retrieval)

**Live Application:**

[CyberFAQ](https://faq-chatbot-using-retrieval.streamlit.app/)

---

## 📜 Project Information

| Property | Details |
|---|---|
| Project Title | FAQ Chatbot Using Retrieval |
| Application Name | CyberFAQ |
| Domain | Cybersecurity and Information Retrieval |
| Project Type | Academic / Machine Learning Project |
| Primary Approach | Hybrid Retrieval-Based Question Answering |
| Deployment | Streamlit Community Cloud |

---

*CyberFAQ — Making cybersecurity knowledge more accessible through intelligent information retrieval.*