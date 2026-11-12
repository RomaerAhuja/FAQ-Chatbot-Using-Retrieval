from src.similarity import FAQSimilarity


def test_similarity_initialization():

    engine = FAQSimilarity()

    assert engine.faq_data is not None


def test_similarity_scores():

    engine = FAQSimilarity()

    scores = engine.calculate_similarity(
        "What is cybersecurity?"
    )

    assert "tfidf" in scores

    assert "semantic" in scores

    assert "hybrid" in scores


def test_ranking():

    engine = FAQSimilarity()

    results = engine.rank_faqs(
        "What is cybersecurity?",
        top_n=5
    )

    assert len(results) > 0

    assert "answer" in results[0]

    assert "similarity" in results[0]


def test_invalid_top_n():

    import pytest

    engine = FAQSimilarity()

    with pytest.raises(ValueError):

        engine.rank_faqs(
            "What is cybersecurity?",
            top_n=0
        )