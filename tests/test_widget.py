import pytest
from src.widget import mask_account_card, get_date

# Фикстуры для тестовых данных
@pytest.fixture
def card_data():
    return "Visa Platinum 7000792289606361"

@pytest.fixture
def account_data():
    return "Счет 1234567890"

@pytest.fixture
def invalid_data():
    return "Invalid Data"

@pytest.fixture
def date_str():
    return "2024-03-11T02:26:18.671407"

# Тесты для mask_account_card
def test_mask_account_card_card(card_data):
    assert mask_account_card(card_data) == "Visa Platinum 7000 79** **** 6361"

def test_mask_account_card_account(account_data):
    assert mask_account_card(account_data) == "Счет **7890"

def test_mask_account_card_invalid(invalid_data):
    with pytest.raises(ValueError):
        mask_account_card(invalid_data)

# Тесты для get_date
def test_get_date(date_str):
    assert get_date(date_str) == "11.03.2024"
