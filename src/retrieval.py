from sklearn.feature_extraction.text import TfidfVectorizer

from src.data_loader import load_faq_data
from src.preprocessing import TextPreprocessor


class FAQRetriever:

    def __init__(self):

        # Load FAQ dataset
        self.faq_data = load_faq_data("csv")

        # Initialize text preprocessor
        self.preprocessor = TextPreprocessor()

        # Extract FAQ questions
        self.questions = self.faq_data["question"].tolist()

        # Preprocess FAQ questions
        self.processed_questions = [
            self.preprocessor.clean_text(question)
            for question in self.questions
        ]

        # Initialize TF-IDF vectorizer
        self.vectorizer = TfidfVectorizer()

        # Convert FAQ questions into TF-IDF vectors
        self.faq_vectors = self.vectorizer.fit_transform(
            self.processed_questions
        )

    def transform_query(self, user_query):

        """
        Convert user query into TF-IDF vector.
        """

        processed_query = self.preprocessor.clean_text(user_query)

        query_vector = self.vectorizer.transform(
            [processed_query]
        )

        return query_vector

    def get_vocabulary(self):

        """
        Return vocabulary learned by TF-IDF.
        """

        return self.vectorizer.get_feature_names_out()

    def get_faq_vectors(self):

        """
        Return TF-IDF vectors of stored FAQs.
        """

        return self.faq_vectors


if __name__ == "__main__":

    retriever = FAQRetriever()

    print("\nTF-IDF INITIALIZATION SUCCESSFUL")

    print("\nTotal FAQs:", len(retriever.questions))

    print("\nVocabulary Size:", len(retriever.get_vocabulary()))

    print("\nSample Vocabulary:")

    print(retriever.get_vocabulary()[:20])

    print("\nFAQ Vector Shape:")

    print(retriever.get_faq_vectors().shape)

    query = "What is cybersecurity?"

    query_vector = retriever.transform_query(query)

    print("\nUser Query:", query)

    print("Query Vector Shape:", query_vector.shape)