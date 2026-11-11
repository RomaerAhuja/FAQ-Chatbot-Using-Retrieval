from sklearn.metrics.pairwise import cosine_similarity

from src.retrieval import FAQRetriever


class FAQSimilarity:

    def __init__(self):

        # Initialize the retrieval engine
        self.retriever = FAQRetriever()

        # Retrieve stored FAQ vectors
        self.faq_vectors = self.retriever.get_faq_vectors()

        # Retrieve original FAQ dataset
        self.faq_data = self.retriever.faq_data

    def calculate_similarity(self, user_query):

        """
        Calculate cosine similarity between
        user query and all stored FAQ questions.
        """

        # Convert user query into TF-IDF vector
        query_vector = self.retriever.transform_query(user_query)

        # Calculate similarity scores
        scores = cosine_similarity(
            query_vector,
            self.faq_vectors
        ).flatten()

        return scores

    def rank_faqs(self, user_query, top_n=5):

        """
        Rank FAQs based on similarity scores.
        """

        scores = self.calculate_similarity(user_query)

        # Sort indices by descending similarity
        ranked_indices = scores.argsort()[::-1][:top_n]

        results = []

        for index in ranked_indices:

            faq = self.faq_data.iloc[index]

            results.append({

                "id": int(faq["id"]),

                "question": faq["question"],

                "answer": faq["answer"],

                "category": faq["category"],

                "source": faq["source"],

                "similarity": float(scores[index])

            })

        return results


if __name__ == "__main__":

    similarity_engine = FAQSimilarity()

    query = "Explain cybersecurity"

    results = similarity_engine.rank_faqs(query)

    print("\nUSER QUERY:", query)

    print("\nTOP MATCHING FAQs\n")

    for result in results:

        print("Question:", result["question"])

        print("Similarity:", round(result["similarity"], 4))

        print("Answer:", result["answer"])

        print("-" * 60)