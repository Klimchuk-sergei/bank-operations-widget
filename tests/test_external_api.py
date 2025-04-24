from unittest.mock import patch

import requests

from src.external_api import convert_to_rub


def test_convert_usd_to_rub():
    """
    Проверяем конвертацию USD в RUB:
    - Мокаем API и устанавливаем курс 1 USD = 90 RUB.
    - Проверяем, что 10 USD корректно конвертируются в 900 RUB.
    """
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"rates": {"RUB": 90.0}}
        transaction = {"amount": 10, "currency": "USD"}
        assert convert_to_rub(transaction) == 900.0


def test_convert_rub_no_conversion():
    """
    Проверяем, что транзакция в RUB возвращается без изменений.
    """
    transaction = {"amount": 100, "currency": "RUB"}
    assert convert_to_rub(transaction) == 100.0


def test_convert_api_failure():
    """
    Проверяем обработку ошибки API:
    - Если API недоступно, возвращает 0.0.
    """
    # Тестируем ошибку соединения
    with patch("requests.get", side_effect=requests.RequestException("API error")):
        transaction = {"amount": 50, "currency": "EUR"}
        assert convert_to_rub(transaction) == 0.0

    # Тестируем ошибку ключа в ответе
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"wrong_key": {}}
        transaction = {"amount": 50, "currency": "EUR"}
        assert convert_to_rub(transaction) == 0.0


def test_convert_invalid_amount():
    """
    Проверяем обработку невалидной суммы.
    """
    transaction = {"amount": "invalid", "currency": "USD"}
    assert convert_to_rub(transaction) == 0.0


def test_convert_missing_currency():
    """
    Проверяем обработку отсутствия валюты (должен использоваться RUB по умолчанию).
    """
    transaction = {"amount": 100}
    assert convert_to_rub(transaction) == 100.0
