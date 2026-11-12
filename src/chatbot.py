import re

from src.similarity import FAQSimilarity


class FAQChatbot:

    def __init__(self, similarity_threshold=0.55):

        self.similarity_engine = FAQSimilarity()

        self.similarity_threshold = similarity_threshold

    def get_answer(self, user_query):

        if not isinstance(user_query, str):
            raise TypeError("Query must be a string.")

        if not user_query.strip():

            return {
                "success": False,
                "message": "Please enter a question.",
                "answer": None
            }

        results = self.similarity_engine.rank_faqs(
            user_query,
            top_n=5
        )

        if not results:

            return {
                "success": False,
                "message": "No matching information found.",
                "answer": None
            }

        best_match = results[0]

        score = best_match["similarity"]

        if score < self.similarity_threshold:

            return {
                "success": False,
                "message": (
                    "Sorry, I couldn't find a relevant "
                    "answer in my knowledge base."
                ),
                "answer": None,
                "similarity": score
            }

        return {

            "success": True,

            "question": best_match["question"],

            "answer": best_match["answer"],

            "category": best_match["category"],

            "source": best_match["source"],

            "similarity": score,

            "tfidf_score": best_match["tfidf_score"],

            "semantic_score": best_match["semantic_score"]

        }

    def get_multiple_answers(self, user_query):

        if not isinstance(user_query, str):
            raise TypeError("Query must be a string.")

        if not user_query.strip():
            return []

        questions = [
            part.strip()
            for part in re.split(
                r"(?<=[.!?])\s+",
                user_query
            )
            if part.strip()
        ]

        if len(questions) <= 1:
            return [self.get_answer(user_query)]

        return [
            self.get_answer(question)
            for question in questions
        ]


if __name__ == "__main__":

    chatbot = FAQChatbot()

    print("CYBERFAQ CHATBOT")
    print("Type 'exit' to stop.")

    while True:

        query = input("\nYou: ")

        if query.lower().strip() in ["exit", "quit", "bye"]:
            break

        response = chatbot.get_answer(query)

        if response["success"]:

            print("\nCyberFAQ:", response["answer"])

            print("Category:", response["category"])

            print(
                "Similarity:",
                round(response["similarity"], 4)
            )

        else:

            print("\nCyberFAQ:", response["message"])