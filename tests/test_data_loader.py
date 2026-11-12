from src.data_loader import load_faq_data


def test_csv_loading():

    data = load_faq_data("csv")

    assert len(data) > 0

    assert "question" in data.columns

    assert "answer" in data.columns


def test_json_loading():

    data = load_faq_data("json")

    assert len(data) > 0

    assert "question" in data.columns

    assert "answer" in data.columns