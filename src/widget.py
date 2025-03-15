from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Скрываем номер карты или счета.
    """
    parts = data.split()  # Разделяем входные данные на части
    if len(parts) < 2:
        raise ValueError("Некорректный формат входных данных.")

    account_type = " ".join(parts[:-1])  # Получаем название карты или счета
    number = parts[-1]  # Берем номер

    if number.isdigit() and len(number) == 16:  # Проверка на карту
        masked_number = get_mask_card_number(number)
    elif number.isdigit() and len(number) > 4:  # Проверка на счет
        masked_number = get_mask_account(number)
    else:
        raise ValueError("Некорректный номер карты или счёта.")

    return f"{account_type} {masked_number}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата '2024-03-11T02:26:18.671407' в 'ДД.ММ.ГГГГ'.
    """
    date_part = date_str.split("T")[0]  # Разделяем по букве Т
    year, month, day = date_part.split("-")
    formatted_date = f"{day}.{month}.{year}"
    return formatted_date
