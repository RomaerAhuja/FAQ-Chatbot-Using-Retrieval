from src.retrieval import FAQRetriever


def test_retriever_initialization():

    retriever = FAQRetriever()

    assert len(retriever.questions) == 30

    assert retriever.faq_vectors.shape[0] == 30


def test_vocabulary():

    retriever = FAQRetriever()

    vocabulary = retriever.get_vocabulary()

    assert len(vocabulary) > 0


def test_query_transformation():

    retriever = FAQRetriever()

    query = "What is cybersecurity?"

    query_vector = retriever.transform_query(query)

    assert query_vector.shape[0] == 1

    assert query_vector.shape[1] == retriever.faq_vectors.shape[1]


def test_unknown_query():

    retriever = FAQRetriever()

    query_vector = retriever.transform_query(
        "Quantum astrophysics"
    )

    assert query_vector.shape[0] == 1

    assert query_vector.nnz == 0


if __name__ == "__main__":

    test_retriever_initialization()

    test_vocabulary()

    test_query_transformation()

    test_unknown_query()

    print("All TF-IDF tests passed!")