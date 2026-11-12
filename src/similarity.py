import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

from src.retrieval import FAQRetriever
from src.semantic_retrieval import SemanticRetriever


class FAQSimilarity:

    def __init__(
        self,
        tfidf_weight=0.35,
        semantic_weight=0.65
    ):

        if not np.isclose(
            tfidf_weight + semantic_weight,
            1.0
        ):
            raise ValueError(
                "Retrieval weights must add up to 1."
            )

        self.tfidf_weight = tfidf_weight
        self.semantic_weight = semantic_weight

        self.retriever = FAQRetriever()

        self.semantic_retriever = SemanticRetriever()

        self.faq_data = self.retriever.faq_data

        self.faq_vectors = self.retriever.get_faq_vectors()

    def calculate_similarity(self, user_query):

        query_vector = self.retriever.transform_query(
            user_query
        )

        tfidf_scores = cosine_similarity(
            query_vector,
            self.faq_vectors
        ).flatten()

        semantic_scores = (
            self.semantic_retriever.calculate_similarity(
                user_query
            )
        )

        hybrid_scores = (
            self.tfidf_weight * tfidf_scores
            + self.semantic_weight * semantic_scores
        )

        return {
            "tfidf": tfidf_scores,
            "semantic": semantic_scores,
            "hybrid": hybrid_scores
        }

    def rank_faqs(self, user_query, top_n=5):

        if not isinstance(user_query, str):
            raise TypeError("Query must be a string.")

        if not user_query.strip():
            return []

        if not isinstance(top_n, int) or top_n < 1:
            raise ValueError("top_n must be a positive integer.")

        scores = self.calculate_similarity(user_query)

        ranked_indices = np.argsort(
            scores["hybrid"]
        )[::-1][:top_n]

        results = []

        for index in ranked_indices:

            faq = self.faq_data.iloc[index]

            results.append({

                "id": int(faq["id"]),

                "question": str(faq["question"]),

                "answer": str(faq["answer"]),

                "category": str(faq["category"]),

                "source": str(faq["source"]),

                "tfidf_score": float(
                    scores["tfidf"][index]
                ),

                "semantic_score": float(
                    scores["semantic"][index]
                ),

                "similarity": float(
                    scores["hybrid"][index]
                )

            })

        return results