from src.decorators import log
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

"""Пример вызова функций из masks.py"""
print(get_mask_account("72777747288831274747"))
print(get_mask_card_number("2598415763546857"))

"""Пример вызова функций из widget.py"""
print(mask_account_card("Visa Platinum 7000792289606361"))
print(get_date("2024-03-11T02:26:18.671407"))

"""Фильтрация списков по ключу"""
filter_list = filter_by_state(
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
)

print(filter_list)

"""Сортировка по дате"""
sort = sort_by_date(
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
)

print(sort)

transactions = [
    {
        "id": 939719570,
        "operationAmount": {"amount": "9824.07", "currency": {"code": "USD"}},
        "description": "Перевод организации",
    },
    {
        "id": 142264268,
        "operationAmount": {"amount": "79114.93", "currency": {"code": "USD"}},
        "description": "Перевод со счета на счет",
    },
    {
        "id": 873106923,
        "operationAmount": {"amount": "43318.34", "currency": {"code": "RUB"}},
        "description": "Перевод со счета на счет",
    },
]

if __name__ == "__main__":
    print("=== USD транзакции ===")
    print(*filter_by_currency(transactions, "USD"), sep="\n---\n")

    print("\n=== Описания транзакций ===")
    print(*transaction_descriptions(transactions), sep="\n")

    print("\n=== Номера карт 1-5 ===")
    print(*card_number_generator(1, 5), sep="\n")


@log(filename="mylog.txt")
def add(a: int, b: int) -> int:
    return a + b


add(1, 2)  # Запишет в файл: "2024-04-01 12:34:56 - add ok: Result = 3"


@log()  # Без filename — вывод в консоль
def divide(a: int, b: int) -> float:
    return a / b


divide(1, 0)  # Выведет в консоль: "divide error: ZeroDivisionError. Inputs: (1, 0), {}"
