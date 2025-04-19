# Учебный проект "Банковские операции"

## В проекте на данный момент реализованы функции маскировки номера карты или счета, в зависимости, что вводите. Реализованны функции сортировки по дате, и по вводимому ключу.

## Установка

```
Для работы нужен Python 3.13 или более новый
```

### 1. Клонируйте репозиторий:

```
git clone https://github.com/Klimchuk-sergei/bank-operations-widget.git
```

### 2. Установите зависимости:

```
pip install -r requirements.txt
```

# Функционал:

### - Модуль masks имеет функции для маскировки номера карт и счета

### - Модуль widget содержит функции для форматирования даты, и скрытия маскировки номера карты или счета

### - Модуль processing фильтрует данные по ключу, и сортирует данные по дате
### - Модуль generators содержит функции для фильтрации транзакций, генерации их описания, и генерацию номера банковских карт в заданном диапазоне.
### - Модуль decorators содержит декораторы для логирования выполнения функций.
## Пример использования:

Пример вызова функций из masks.py

```
from src.masks import get_mask_account, get_mask_card_number

print(get_mask_account("72777747288831274747"))
print(get_mask_card_number("2598415763546857"))
```

Пример вызова функций из widget.py

```
from src.widget import get_date, mask_account_card

print(mask_account_card("Visa Platinum 7000792289606361"))
print(get_date("2024-03-11T02:26:18.671407"))
```

Фильтрация списков по ключу

```
from src.processing import filter_by_state

filter = filter_by_state(
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
)

print(filter)
```

Сортировка по дате

```
from src.processing import sort_by_date

sort = sort_by_date(
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
)

print(sort)
```

Фильтр транзакций по заданной валюте 

```
from src.generators import filter_by_currency

usd_transactions = filter_by_currency(transactions, "USD")
for tx in usd_transactions:
    print(tx)
```

Генерация описания транзакций

```
from src.generators  import transaction_descriptions

for desc in transaction_descriptions(transactions):
    print(desc)
```

Гнерация номеров банковских карт в заданном диапазоне

```
from src.generators  import card_number_generator

for card_num in card_number_generator(1, 5):
    print(card_num)
    
# 0000 0000 0000 0001
# 0000 0000 0000 0002
# ...
```

Логирование функций

```
from src.decorators  import log

Декоратор выполняет логирование функции, и записывает результат в файл, либо выводит информацию в консоль (если имя файла не указано)

Возможности

✔ Логирование в консоль или файл  
✔ Фиксация успешных выполнений и ошибок  
✔ Сохранение параметров вызова при ошибках  
✔ Гибкая настройка через параметры 

Логирование в консоль

@log()
def add(a: int, b: int) -> int:
    return a + b


Логирование в файл

@log(filename="operations.log")
def multiply(a: int, b: int) -> int:
    return a * b
```

## Чтение файлов CSV и XLSX

Теперь проект поддерживает чтение финансовых операций из:
- JSON файлов (как и раньше)
- CSV файлов
- Excel файлов (XLSX)

Используйте:
- `read_csv_file()` для CSV
- `read_excel_file()` для Excel

Пример:
```python
from read_csv_xlsx import read_csv, read_excel

csv_data = read_csv('transactions.csv')
excel_data = read_excel('transactions.xlsx')

## Тестирование
```
Для тестирования используйте фреймворк pytest, а для измерения покрытия кода тестами — инструмент pytest-cov.
```
### Запуск тестов
```
Чтобы запустить все тесты, выполните следующую команду в терминале: pytest
```
### Измерение покрытия кода тестами
```
Для измерения покрытия кода тестами используется инструмент pytest-cov. Чтобы запустить тесты с измерением покрытия, выполните: pytest --cov=src --cov-report=term
```
### Генерация HTML-отчёта о покрытии
```
Чтобы сгенерировать HTML-отчёт о покрытии, выполните: pytest --cov=src --cov-report=html
```
## Лицензия
```
Этот проект распространяется под лицензией MIT.
```

<span style="font-size: larger; color: green;">Klimchuk-sergei</span>