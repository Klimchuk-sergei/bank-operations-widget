import pytest
from src.masks import get_mask_card_number, get_mask_account

# Фикстуры для тестовых данных
@pytest.fixture
def valid_card_number():
    return "1234567812345678"

@pytest.fixture
def invalid_card_number():
    return "1234"

@pytest.fixture
def valid_account_number():
    return "1234567890"

@pytest.fixture
def invalid_account_number():
    return "123"

# Тесты для get_mask_card_number
def test_get_mask_card_number_valid(valid_card_number):
    assert get_mask_card_number(valid_card_number) == "1234 56** **** 5678"

def test_get_mask_card_number_invalid(invalid_card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_card_number)

# Тесты для get_mask_account
def test_get_mask_account_valid(valid_account_number):
    assert get_mask_account(valid_account_number) == "**7890"

def test_get_mask_account_invalid(invalid_account_number):
    with pytest.raises(ValueError):
        get_mask_account(invalid_account_number)
