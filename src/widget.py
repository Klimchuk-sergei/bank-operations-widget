from src.masks import get_mask_account, get_mask_card_number


# def mask_account_card(data: str) -> str:
#     """
#     Скрываем номер карты или счета.
#     """
#     parts = data.split()  # Разделяем входные данные на части
#     if len(parts) < 2:
#         raise ValueError("Некорректный формат входных данных.")
#
#     account_type = " ".join(parts[:-1])  # Получаем название карты или счета
#     number = parts[-1]  # Берем номер
#
#     if number.isdigit() and len(number) == 16:  # Проверка на карту
#         masked_number = get_mask_card_number(number)
#     elif number.isdigit() and len(number) > 4:  # Проверка на счет
#         masked_number = get_mask_account(number)
#     else:
#         raise ValueError("Некорректный номер карты или счёта.")
#
#     return f"{account_type} {masked_number}"
def mask_account_card(data: str) -> str:
    """
    Скрываем номер карты или счета.
    Возвращает оригинальную строку, если не удалось определить тип номера.
    """
    if not data or not isinstance(data, str):
        return "Некорректные данные"

    try:
        parts = data.split()  # Разделяем входные данные на части
        if len(parts) < 2:
            return data  # Возвращаем как есть, если не можем разобрать

        account_type = " ".join(parts[:-1])  # Получаем название карты или счета
        number = parts[-1]  # Берем номер

        # Удаляем все нецифровые символы из номера
        clean_number = ''.join(c for c in number if c.isdigit())

        if len(clean_number) == 16:  # Проверка на карту
            masked_number = get_mask_card_number(clean_number)
        elif len(clean_number) > 4:  # Проверка на счет
            masked_number = get_mask_account(clean_number)
        else:
            return data  # Возвращаем как есть, если не соответствует форматам

        return f"{account_type} {masked_number}"

    except Exception:
        return data  # В случае любой ошибки возвращаем исходные данные


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата '2024-03-11T02:26:18.671407' в 'ДД.ММ.ГГГГ'.
    Если формат некорректен, выбрасывает ValueError.
    """
    if "T" not in date_str:
        raise ValueError("Некорректный формат даты. Ожидается формат 'YYYY-MM-DDThh:mm:ss'.")

    try:
        date_part = date_str.split("T")[0]  # Разделяем по букве Т
        year, month, day = date_part.split("-")
        formatted_date = f"{day}.{month}.{year}"
        return formatted_date
    except (IndexError, ValueError):
        raise ValueError("Некорректный формат даты. Ожидается формат 'YYYY-MM-DDThh:mm:ss'.")
