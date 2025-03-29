import pytest

from src.masks import get_mask_account, get_mask_card_number


# Параметризация для тестов get_mask_card_number
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),  # Валидный номер карты
        ("0000000000000000", "0000 00** **** 0000"),  # Номер карты из нулей
        ("1111222233334444", "1111 22** **** 4444"),  # Другой валидный номер
        ("9999888877776666", "9999 88** **** 6666"),  # Ещё один валидный номер
    ],
)
def test_get_mask_card_number_valid(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


# Параметризация для тестов get_mask_card_number с некорректными данными
@pytest.mark.parametrize(
    "card_number",
    [
        "1234",  # Слишком короткий номер
        "12345678123456789",  # Слишком длинный номер
        "abcdefghijklmnop",  # Номер с буквами
        "",  # Пустая строка
        "1234 5678 9012 3456",  # Номер с пробелами
        "1234-5678-9012-3456",  # Номер с дефисами
    ],
)
def test_get_mask_card_number_invalid(card_number: str) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


# Параметризация для тестов get_mask_account
@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("1234567890", "**7890"),  # Валидный номер счёта
        ("0000000000", "**0000"),  # Номер счёта из нулей
        ("9876543210", "**3210"),  # Другой валидный номер
        ("111122223333", "**3333"),  # Номер счёта из 12 цифр
    ],
)
def test_get_mask_account_valid(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected


# Параметризация для тестов get_mask_account с некорректными данными
@pytest.mark.parametrize(
    "account_number",
    [
        "123",  # Слишком короткий номер
        "abcdef",  # Номер с буквами
        "",  # Пустая строка
        "1234 5678 90",  # Номер с пробелами
        "1234-5678-90",  # Номер с дефисами
    ],
)
def test_get_mask_account_invalid(account_number: str) -> None:
    with pytest.raises(ValueError):
        get_mask_account(account_number)
