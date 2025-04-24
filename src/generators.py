from typing import Dict, Iterator, List

# def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
#     """
#     Фильтрация транзакций по указанной валюте
#     transactions: список словарей с транзакциями
#     currency: код валюты необходимый для фильтрации (например USD)
#     """
#     for transaction in transactions:
#         op_amount = transaction.get("operationAmount", {})
#         curr = op_amount.get("currency", {}).get("code")
#         if curr == currency:
#             yield transaction

def filter_by_currency(transactions: list[dict], currency: str) -> filter:
    """Фильтр, работающий с разными структурами данных"""

    def get_currency_code(tr):
        # Вариант 1: Стандартная структура
        if "operationAmount" in tr:
            return tr["operationAmount"].get("currency", {}).get("code")
        # Вариант 2: Плоская структура
        return tr.get("currency_code") or tr.get("currency")

    return filter(lambda x: get_currency_code(x) == currency, transactions)


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генерация описаний транзакций
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генерация номеров банковских карт в указанном диапазоне
    """
    if start > end:
        raise ValueError("Первое число не может быть больше последнего")

    for num in range(start, end + 1):
        card_num = f"{num:016d}"
        form_num = " ".join(
            [
                card_num[0:4],
                card_num[4:8],
                card_num[8:12],
                card_num[12:16],
            ]
        )
        yield form_num
