from src.chatbot import FAQChatbot


def test_valid_question():

    bot = FAQChatbot()

    response = bot.get_answer(
        "What is cybersecurity?"
    )

    assert response["success"] is True

    assert response["answer"] is not None

    assert response["category"] == "Fundamentals"


def test_empty_question():

    bot = FAQChatbot()

    response = bot.get_answer("")

    assert response["success"] is False

    assert response["answer"] is None


def test_unknown_question():

    bot = FAQChatbot(confidence_threshold=1.1)

    response = bot.get_answer(
        "What is cybersecurity?"
    )

    assert response["success"] is False


def test_invalid_input():

    bot = FAQChatbot()

    try:

        bot.get_answer(123)

    except TypeError:

        return

    raise AssertionError("TypeError was not raised")


if __name__ == "__main__":

    test_valid_question()

    test_empty_question()

    test_unknown_question()

    test_invalid_input()

    print("All chatbot backend tests passed!")