from src.data_loader import load_faq_data


def test_csv_loading():

    data = load_faq_data("csv")

    assert len(data) == 30

    assert "question" in data.columns

    assert "answer" in data.columns


def test_json_loading():

    data = load_faq_data("json")

    assert len(data) == 30

    assert "question" in data.columns

    assert "answer" in data.columns


if __name__ == "__main__":

    test_csv_loading()

    test_json_loading()

    print("All dataset loader tests passed!")