import logging
from pathlib import Path

# Проверяем есть ли папка logs, создаем её если её нет
Path("logs").mkdir(exist_ok=True)

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/masks.log", mode="w")
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    try:
        logger.debug("Начало маскировки номера карты")

        """ Проверяем, что номер карты состоит из 16 цифр """
        if len(card_number) != 16 or not card_number.isdigit():
            raise ValueError("Номер карты должен состоять из 16 цифр.")

        """Маскируем номер карты"""
        masked_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

        logger.info(f"Карта успешно замаскирована: {masked_card}")

        return masked_card

    except Exception as e:
        logger.error(f"Ошибка при маскировке номера картыЖ: {str(e)}", exc_info=True)
        raise


def get_mask_account(account_number: str) -> str:
    try:

        logger.debug("НАчало маскировки номера счёта")

        """Проверяем, что номер счёта состоит более чем из 4 цифр"""
        if len(account_number) < 4 or not account_number.isdigit():
            raise ValueError("Номер счёта должен состоять минимум из 4 цифр.")

        """Маскируем номер счёта"""
        masked_account = f"**{account_number[-4:]}"

        logger.info(f"Счёт успешно замаскирован: {masked_account}")

        return masked_account

    except Exception as e:
        logger.error(f"Ошибка при маскировании счёта: {str(e)}", exc_info=True)
        raise
