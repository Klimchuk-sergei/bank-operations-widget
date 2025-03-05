def get_mask_card_number(card_number: str | int) -> str:
    """Преобразуем номер карты в строку"""
    card_number = str(card_number)

    """ Проверяем, что номер карты состоит из 16 цифр """
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен состоять из 16 цифр.")

    """Маскируем номер карты"""
    masked_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

    return masked_card


def get_mask_account(account_number: str | int) -> str:
    """Преобразуем номер счёта в строку"""
    account_number = str(account_number)

    """Проверяем, что номер счёта состоит более чем из 4 цифр"""
    if len(account_number) < 4 or not account_number.isdigit():
        raise ValueError("Номер счёта должен состоять минимум из 4 цифр.")

    """Маскируем номер счёта"""
    masked_account = f"**{account_number[-4:]}"

    return masked_account
