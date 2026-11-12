from src.retrieval import FAQRetriever


def test_retriever_initialization():

    retriever = FAQRetriever()

    assert len(retriever.questions) > 0


def test_vocabulary():

    retriever = FAQRetriever()

    assert len(retriever.get_vocabulary()) > 0


def test_query_transformation():

    retriever = FAQRetriever()

    vector = retriever.transform_query(
        "What is cybersecurity?"
    )

    assert vector.shape[1] == len(
        retriever.get_vocabulary()
    )