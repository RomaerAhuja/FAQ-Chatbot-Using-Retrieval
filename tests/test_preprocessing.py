from src.preprocessing import TextPreprocessor

processor = TextPreprocessor()


def test_lowercase():

    assert processor.clean_text(
        "CYBERSECURITY"
    ) == "cybersecurity"


def test_punctuation():

    assert processor.clean_text(
        "What is malware?"
    ) == "what is malware"


def test_whitespace():

    assert processor.clean_text(
        "Network    Security"
    ) == "network security"


def test_url_removal():

    assert processor.clean_text(
        "Visit https://example.com"
    ) == "visit"


def test_empty_string():

    assert processor.clean_text("") == ""


def test_invalid_input():

    try:
        processor.clean_text(123)
    except TypeError:
        return

    raise AssertionError("TypeError was not raised")


if __name__ == "__main__":

    test_lowercase()
    test_punctuation()
    test_whitespace()
    test_url_removal()
    test_empty_string()
    test_invalid_input()

    print("All preprocessing tests passed!")