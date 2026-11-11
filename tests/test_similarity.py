from src.similarity import FAQSimilarity


def test_similarity_calculation():

    engine = FAQSimilarity()

    scores = engine.calculate_similarity(
        "What is cybersecurity?"
    )

    assert len(scores) == 30

    assert scores.max() > 0


def test_faq_ranking():

    engine = FAQSimilarity()

    results = engine.rank_faqs(
        "What is cybersecurity?",
        top_n=5
    )

    assert len(results) == 5

    assert results[0]["similarity"] >= results[1]["similarity"]


def test_result_structure():

    engine = FAQSimilarity()

    results = engine.rank_faqs(
        "What is phishing?",
        top_n=3
    )

    required_keys = [
        "id",
        "question",
        "answer",
        "category",
        "source",
        "similarity"
    ]

    for result in results:

        for key in required_keys:

            assert key in result


def test_invalid_empty_query():

    engine = FAQSimilarity()

    scores = engine.calculate_similarity("")

    assert scores.max() == 0


if __name__ == "__main__":

    test_similarity_calculation()

    test_faq_ranking()

    test_result_structure()

    test_invalid_empty_query()

    print("All similarity tests passed!")