from src.description import filter_operations_by_description
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.read_csv_xlsx import read_csv, read_excel
from src.utils import read_json_file
from src.widget import get_date, mask_account_card

# """Пример вызова функций из masks.py"""
# print(get_mask_account("72777747288831274747"))
# print(get_mask_card_number("2598415763546857"))
#
# """Пример вызова функций из widget.py"""
# print(mask_account_card("Visa Platinum 7000792289606361"))
# print(get_date("2024-03-11T02:26:18.671407"))
#
# """Фильтрация списков по ключу"""
# filter_list = filter_by_state(
#     [
#         {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#     ]
# )
#
# print(filter_list)
#
# """Сортировка по дате"""
# sort = sort_by_date(
#     [
#         {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#     ]
# )
#
# print(sort)
#
# transactions = [
#     {
#         "id": 939719570,
#         "operationAmount": {"amount": "9824.07", "currency": {"code": "USD"}},
#         "description": "Перевод организации",
#     },
#     {
#         "id": 142264268,
#         "operationAmount": {"amount": "79114.93", "currency": {"code": "USD"}},
#         "description": "Перевод со счета на счет",
#     },
#     {
#         "id": 873106923,
#         "operationAmount": {"amount": "43318.34", "currency": {"code": "RUB"}},
#         "description": "Перевод со счета на счет",
#     },
# ]
#
# if __name__ == "__main__":
#     print("=== USD транзакции ===")
#     print(*filter_by_currency(transactions, "USD"), sep="\n---\n")
#
#     print("\n=== Описания транзакций ===")
#     print(*transaction_descriptions(transactions), sep="\n")
#
#     print("\n=== Номера карт 1-5 ===")
#     print(*card_number_generator(1, 5), sep="\n")
#
#
# @log(filename="mylog.txt")
# def add(a: int, b: int) -> int:
#     return a + b
#
#
# add(1, 2)  # Запишет в файл: "2024-04-01 12:34:56 - add ok: Result = 3"
#
#
# @log()  # Без filename — вывод в консоль
# def divide(a: int, b: int) -> float:
#     return a / b
#
#
# divide(1, 0)  # Выведет в консоль: "divide error: ZeroDivisionError. Inputs: (1, 0), {}"

def main():
    print("""
    Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    """
          )
    choose_file = input().lower().strip()

    while True:
        choose_file = input("Введите номер (1-3): ").strip()
        if choose_file in {"1", "2", "3"}:
            break
        print("Ошибка: введите 1, 2 или 3!")

    if choose_file == "1":
        print("Для обработки выбран JSON-файл.")
    elif choose_file == "2":
        print("Для обработки выбран CSV-файл.")
    elif choose_file == "3":
        print("Для обработки выбран XLSX-файл.")

    status_operation = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        print(
            """
    Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.
            """
        )
        choose_status = input().upper().strip()
        if choose_status in status_operation:
            print(f"Операции отфильтрованы по статусу {choose_status}")
            break
        else:
            print(f"Статус операции {choose_status} недоступен.")

    print("Отсортировать операции по дате? Да/Нет")
    while True:
        choose_sort_by_date = input().lower().strip()
        if choose_sort_by_date in ["да", "нет"]:
            break

    if choose_sort_by_date == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        while True:
            choose_sort_by_date = input().lower().strip()
            if choose_sort_by_date in ["по возрастанию", "по убыванию"]:
                break

    print("Выводить только рублевые тразакции? Да/Нет")
    while True:
        choose_rub = input().lower().strip()
        if choose_rub in ["да", "нет"]:
            break

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    while True:
        choose_word_search = input().lower().strip()
        if choose_word_search in ["да", "нет"]:
            break

    transaction = []
    if choose_file == "1":
        transaction = read_json_file()
    elif choose_file == "2":
        transaction = read_csv()
    elif choose_file == "3":
        transaction = read_excel()

    # Фильтрация по статусу
    transaction = filter_by_state(transaction, choose_status)

    # Сорт по дате
    if choose_sort_by_date == "да":
        revers_choose = choose_sort_by_date == "по убыванию"
        transaction = sort_by_date(transaction, reverse=revers_choose)

    # фильтрация по валюте
    if choose_rub == "да":
        transaction = list(filter_by_currency(transaction, "RUB"))
    else:
        choose_currency = (input("Введите слово для фильтрации валюты: USD, EUR: ")).upper().strip()
        transaction = list(filter_by_currency(transaction, choose_currency))

    # Фильтрация по описанию
    if choose_word_search == "да":
        search_word = (input("Введите ключевое слово ддля поиска: ")).lower().strip()
        transaction = filter_operations_by_description(transaction, search_word)

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке {len(transaction)}")

    for t in transaction:
        date = get_date(t.get("date", "Дата неизвестна"))
        description = t.get("description", "Описание отсутствует")
        from_account = mask_account_card(t.get("from", ""))  # Без дополнительных проверок
        to_account = mask_account_card(t.get("to", ""))  # Функция теперь сама обрабатывает ошибки

        operation_amount = t.get("operationAmount", {})
        amount = operation_amount.get("amount", "Сумма не указана")
        currency = operation_amount.get("currency", {})
        currency_code = currency.get("code", "Валюта не указана")

        print(f"""
        Дата: {date} {description}
        {from_account} -> {to_account}
        Сумма: {amount} {currency_code}
        """)
        print({t["operationAmount"]["currency"]["code"] for t in transaction})


if __name__ == "__main__":
    main()
