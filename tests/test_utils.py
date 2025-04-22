from unittest.mock import mock_open, patch

from src.utils import read_json_file


def test_read_json_file_valid():
    """Тест на правильное чтение JSON."""
    fake_json = '[{"id": 1, "amount": 100}]'
    with patch("builtins.open", mock_open(read_data=fake_json)):
        result = read_json_file("fake.json")
        assert result == [{"id": 1, "amount": 100}]


def test_read_json_file_invalid():
    """Тест на пустой или битый JSON."""
    # Файла нет
    with patch("builtins.open", side_effect=FileNotFoundError):
        assert read_json_file("no_file.json") == []

    # JSON не список (например, просто число)
    with patch("builtins.open", mock_open(read_data="123")):
        assert read_json_file("bad.json") == []
