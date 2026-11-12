import pytest

from src.preprocessing import TextPreprocessor


processor = TextPreprocessor()


def test_lowercase():

    assert processor.clean_text(
        "CYBERSECURITY"
    ) == "cybersecurity"


def test_punctuation():

    assert processor.clean_text(
        "Hello!!!"
    ) == "hello"


def test_whitespace():

    assert processor.clean_text(
        "Hello    World"
    ) == "hello world"


def test_url_removal():

    result = processor.clean_text(
        "Visit https://example.com"
    )

    assert "https" not in result


def test_empty_string():

    assert processor.clean_text("") == ""


def test_invalid_input():

    with pytest.raises(TypeError):

        processor.clean_text(123)