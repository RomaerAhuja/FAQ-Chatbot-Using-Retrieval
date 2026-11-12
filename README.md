# 🔐 CyberFAQ — Hybrid Retrieval-Based Cybersecurity FAQ Chatbot

CyberFAQ is a hybrid retrieval-based chatbot designed to answer frequently asked questions related to cybersecurity.

The system combines traditional keyword-based information retrieval using TF-IDF with semantic search using Sentence Transformers to identify relevant answers from a predefined cybersecurity knowledge base.

## 🚀 Features

- Cybersecurity FAQ knowledge base
- CSV and JSON dataset support
- Text preprocessing and normalization
- TF-IDF-based keyword retrieval
- Semantic retrieval using Sentence Transformers
- Cosine similarity calculation
- Hybrid similarity scoring
- Ranked FAQ retrieval
- Configurable similarity threshold
- Fallback response mechanism
- Multiple-question handling
- Interactive Streamlit user interface
- Conversation history
- Automated testing using Pytest

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Keyword Retrieval | TF-IDF |
| Semantic Retrieval | Sentence Transformers |
| Embedding Model | all-MiniLM-L6-v2 |
| Similarity Calculation | Cosine Similarity |
| Machine Learning | Scikit-learn, PyTorch |
| Frontend | Streamlit |
| Testing | Pytest |
| Dataset Format | CSV, JSON |
| Version Control | Git and GitHub |

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

## ⚙️ Installation and Setup

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

The first execution of the semantic retrieval engine may download the pretrained Sentence Transformer model. An internet connection is required for the initial download.

## ▶️ Running the Application

From the project root directory, execute:

```bash
python -m streamlit run app/streamlit_app.py
```

The application will be available at:

```text
http://localhost:8501
```

## 🧠 System Architecture

CyberFAQ follows a hybrid information retrieval architecture.

### Processing Pipeline

1. User submits a cybersecurity question.
2. Text preprocessing normalizes the input.
3. TF-IDF converts the query into a numerical representation.
4. Sentence Transformers generate a semantic embedding.
5. Cosine similarity calculates similarity scores.
6. Hybrid scoring combines lexical and semantic similarity.
7. The retrieval engine ranks the FAQ records.
8. The chatbot checks the configured similarity threshold.
9. The system returns the most relevant answer or a fallback response.

### Hybrid Scoring Formula

The current implementation uses:

```text
Hybrid Score = (0.35 × TF-IDF Score)
             + (0.65 × Semantic Score)
```

The weights are configurable in the similarity engine.

## 📊 Dataset

The project uses a structured cybersecurity FAQ dataset containing:

- FAQ ID
- Question
- Answer
- Category
- Keywords
- Source

The dataset is maintained in both CSV and JSON formats.

## 🧪 Testing

The project uses Pytest for automated testing.

Execute all tests using:

```bash
python -m pytest tests -v
```

The test suite covers:

- Dataset loading
- Text preprocessing
- TF-IDF retrieval
- Similarity calculation
- FAQ ranking
- Chatbot responses
- Input validation
- Multiple-question handling

## 📈 Evaluation

The project includes a retrieval evaluation module that measures:

- Top-1 Accuracy
- Top-3 Accuracy

Evaluation requires independently prepared test queries with manually verified expected FAQ IDs.

Actual evaluation results should be reported only after running the evaluation against the completed test dataset.

## 🔮 Future Scope

Potential future enhancements include:

- Expanding the cybersecurity knowledge base
- Improving retrieval accuracy
- Context-aware conversational interactions
- Retrieval-Augmented Generation (RAG)
- Multilingual question answering
- User feedback collection
- Advanced evaluation metrics
- Integration with external cybersecurity knowledge sources

## 👨‍💻 Author

**Romaer Ahuja**

GitHub Repository:

https://github.com/RomaerAhuja/FAQ-Chatbot-Using-Retrieval

---

*CyberFAQ — Making cybersecurity knowledge more accessible through intelligent information retrieval.*