from sklearn.feature_extraction.text import TfidfVectorizer

from src.data_loader import load_faq_data
from src.preprocessing import TextPreprocessor


class FAQRetriever:

    def __init__(self):

        self.faq_data = load_faq_data("csv")

        self.preprocessor = TextPreprocessor()

        self.questions = self.faq_data["question"].tolist()

        self.processed_questions = [
            self.preprocessor.clean_text(question)
            for question in self.questions
        ]

        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            sublinear_tf=True
        )

        self.faq_vectors = self.vectorizer.fit_transform(
            self.processed_questions
        )

    def transform_query(self, user_query):

        processed_query = self.preprocessor.clean_text(
            user_query
        )

        return self.vectorizer.transform(
            [processed_query]
        )

    def get_vocabulary(self):

        return self.vectorizer.get_feature_names_out()

    def get_faq_vectors(self):

        return self.faq_vectors


if __name__ == "__main__":

    retriever = FAQRetriever()

    print("TF-IDF RETRIEVAL ENGINE")

    print("Total FAQs:", len(retriever.questions))

    print("Vocabulary size:", len(retriever.get_vocabulary()))

    print("Vector dimensions:", retriever.get_faq_vectors().shape)