import pytest

from src.chatbot import FAQChatbot


@pytest.fixture(scope="module")
def chatbot():

    return FAQChatbot()


def test_valid_question(chatbot):

    result = chatbot.get_answer(
        "What is cybersecurity?"
    )

    assert result["success"] is True

    assert result["answer"] is not None


def test_empty_question(chatbot):

    result = chatbot.get_answer("")

    assert result["success"] is False


def test_unknown_question(chatbot):

    result = chatbot.get_answer(
        "Explain quantum mechanics and astrophysics."
    )

    assert result["success"] is False


def test_invalid_input(chatbot):

    with pytest.raises(TypeError):

        chatbot.get_answer(123)


def test_multiple_questions(chatbot):

    results = chatbot.get_multiple_answers(
        "What is cybersecurity? Explain the CIA triad."
    )

    assert len(results) == 2