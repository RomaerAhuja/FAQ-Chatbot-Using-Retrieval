import numpy as np

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from src.data_loader import load_faq_data


MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


class SemanticRetriever:

    def __init__(self):

        self.faq_data = load_faq_data("csv")

        self.questions = self.faq_data["question"].tolist()

        self.model = SentenceTransformer(MODEL_NAME)

        self.question_embeddings = self.model.encode(
            self.questions,
            convert_to_numpy=True,
            normalize_embeddings=True,
            show_progress_bar=False
        )

    def transform_query(self, user_query):

        return self.model.encode(
            [user_query],
            convert_to_numpy=True,
            normalize_embeddings=True
        )

    def calculate_similarity(self, user_query):

        query_embedding = self.transform_query(user_query)

        scores = cosine_similarity(
            query_embedding,
            self.question_embeddings
        ).flatten()

        return scores

    def get_embeddings(self):

        return self.question_embeddings


if __name__ == "__main__":

    retriever = SemanticRetriever()

    query = "How do I protect my computer from hackers?"

    scores = retriever.calculate_similarity(query)

    best_index = int(np.argmax(scores))

    print("SEMANTIC RETRIEVAL ENGINE")

    print("Query:", query)

    print("Best matching question:")

    print(retriever.questions[best_index])

    print("Similarity:", round(float(scores[best_index]), 4))