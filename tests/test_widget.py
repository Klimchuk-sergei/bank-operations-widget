from typing import Tuple, cast

import pytest

from src.widget import get_date, mask_account_card


# Фикстура для тестов mask_account_card
@pytest.fixture(
    params=[
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ]
)
def account_card_data(request: pytest.FixtureRequest) -> Tuple[str, str]:
    return cast(Tuple[str, str], request.param)


# Позитивные тесты для mask_account_card
def test_mask_account_card(account_card_data: Tuple[str, str]) -> None:
    input_data, expected_output = account_card_data
    assert mask_account_card(input_data) == expected_output


# Негативные тесты для mask_account_card
def test_mask_account_card_invalid() -> None:
    with pytest.raises(ValueError):
        mask_account_card("Invalid Data")  # Некорректные данные
    with pytest.raises(ValueError):
        mask_account_card("Visa Platinum 1234")  # Некорректный номер карты
    with pytest.raises(ValueError):
        mask_account_card("Счет 123")  # Некорректный номер счёта


# Фикстура для тестов get_date
@pytest.fixture(
    params=[
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-31T23:59:59.999999", "31.12.2023"),
    ]
)
def date_data(request: pytest.FixtureRequest) -> Tuple[str, str]:
    return cast(Tuple[str, str], request.param)


# Позитивные тесты для get_date
def test_get_date(date_data: Tuple[str, str]) -> None:
    input_data, expected_output = date_data
    assert get_date(input_data) == expected_output


# Негативные тесты для get_date
def test_get_date_invalid() -> None:
    # Некорректные данные (без 'T')
    with pytest.raises(ValueError):
        get_date("2024-03-11")
    # Некорректные данные (неправильный формат)
    with pytest.raises(ValueError):
        get_date("2024/03/11T02:26:18.671407")
    # Пустая строка
    with pytest.raises(ValueError):
        get_date("")
