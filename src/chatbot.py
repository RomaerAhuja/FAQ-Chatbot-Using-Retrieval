from src.similarity import FAQSimilarity


class FAQChatbot:

    def __init__(self, confidence_threshold=0.20):

        self.similarity_engine = FAQSimilarity()

        self.confidence_threshold = confidence_threshold

    def get_answer(self, user_query):

        """
        Retrieve the most relevant FAQ answer.
        """

        # Validate input
        if not isinstance(user_query, str):
            raise TypeError("Query must be a string.")

        if not user_query.strip():

            return {
                "success": False,
                "message": "Please enter a question.",
                "answer": None
            }

        # Retrieve ranked FAQ results
        results = self.similarity_engine.rank_faqs(
            user_query,
            top_n=5
        )

        # Get best matching result
        best_match = results[0]

        confidence = best_match["similarity"]

        # Confidence threshold check
        if confidence < self.confidence_threshold:

            return {
                "success": False,
                "message": "Sorry, I couldn't find a relevant answer in my knowledge base.",
                "answer": None,
                "confidence": confidence
            }

        # Return retrieved answer
        return {
            "success": True,
            "question": best_match["question"],
            "answer": best_match["answer"],
            "category": best_match["category"],
            "source": best_match["source"],
            "confidence": confidence
        }


# Convenient function for external modules

chatbot = FAQChatbot()


def get_answer(user_query):

    return chatbot.get_answer(user_query)


if __name__ == "__main__":

    print("\nFAQ CHATBOT BACKEND")
    print("=" * 50)

    while True:

        query = input("\nYou: ")

        if query.lower() in ["exit", "quit", "bye"]:

            print("Chatbot: Goodbye!")

            break

        response = get_answer(query)

        if response["success"]:

            print("\nChatbot:", response["answer"])

            print("Category:", response["category"])

            print("Confidence:", round(response["confidence"], 4))

            print("Source:", response["source"])

        else:

            print("\nChatbot:", response["message"])