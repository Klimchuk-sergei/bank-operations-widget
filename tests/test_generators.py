import pytest
from src.generators import (filter_by_currency,
                            transaction_descriptions,
                            card_number_generator)


@pytest.fixture
def transactions():
    """
    Тестовые данные для транзакций
    """
    return[
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"code": "USD"}
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"code": "USD"}
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"code": "RUB"}
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {"code": "USD"}
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {"code": "RUB"}
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]


"""
Тесты filter__by_currency
"""

def test_filter_by_currence_usd(transactions):
    """
    Тест фильтрации транзакций USD
    """
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 3
    assert all(transactions["operationAmount"]["currency"]["code"] == "USD" for transactions in result)
    assert [transactions["id"] for transactions in result] == [939719570, 142264268, 895315941]


def test_filter_by_currency_rub(transactions):
    """
    Тест фильтрации транзакций RUB
    """
    result = list(filter_by_currency(transactions, "RUB"))
    assert len(result) == 2
    assert [transactions["id"] for transactions in result] == [873106923, 594226727]    # Проверка на верность фильтрации транзакций


def test_filter_by_currency_empty_result(transactions):
    """
    Тест фильтрации несуществующей валюты
    """
    assert list(filter_by_currency(transactions, "EUR")) == []


"""
Тесты transaction_descriptions
"""

def test_transaction_descriptions_all(transactions):
    """Тест получения всех описаний"""
    result = list(transaction_descriptions(transactions))
    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"]


def test_transaction_descriptions_empty_input():
    """
    Тест с пустым списком транзакций
    """
    assert list(transaction_descriptions([])) == []


def test_transaction_descriptions_generator_behavior(transactions):
    """
    Тест поведения генератора
    """
    gen = transaction_descriptions(transactions)
    assert next(gen) == "Перевод организации"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод с карты на карту"


"""
Тесты для card_number_generator
"""

@pytest.mark.parametrize("start, end, expected", [
    (1, 1, ["0000 0000 0000 0001"]),
    (1, 3, ["0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003"]),
    (9999, 10001, ["0000 0000 0000 9999",
        "0000 0000 0001 0000",
        "0000 0000 0001 0001"]),
])


def test_card_number_generator_output(start, end, expected):
    """
    Тест генерации номеров карт
    """
    assert list(card_number_generator(start, end)) == expected


def test_card_number_generator_invalid_range():
    """
    Тест обработки неверного диапазона
    """
    with pytest.raises(ValueError):
        list(card_number_generator(5, 1))
