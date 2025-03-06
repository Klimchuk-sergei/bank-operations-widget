from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date

# Пример вызова функций из masks.py
print(get_mask_account("72777747288831274747"))
print(get_mask_card_number("2598415763546857"))

# Пример вызова функций из widget.py
print(mask_account_card("Visa Platinum 7000792289606361"))
print(get_date("2024-03-11T02:26:18.671407"))