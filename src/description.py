import re
from collections import defaultdict


def filter_operations_by_description(operations, search_string):
    """
    Фильтрация списков операций по наличию строки поиска в описании операции.

    Принимает:
        operations: Список словарей с данными о банковских операциях.
                   В каждом словаре должен быть ключ 'description'.
        search_string: Строка для поиска в описании операций.

    Возвращает:
        Список словарей, в описании которых найдена строка поиска.
    """
    if not search_string:
        return operations

    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    filtered_operations = [
        op for op in operations
        if 'description' in op and pattern.search(op['description'])
    ]

    return filtered_operations


def count_operations_by_categories(operations, categories):
    """
    Счетчик количества операций каждой категории.

    Принимает:
        operations: Список словарей с данными о банковских операциях.
                   Каждый словарь должен содержать ключ 'description'.
        categories: Список строк с названиями категорий для подсчёта.

    Возвращает:
        Словарь, в котором ключи - названия категорий, значения - количество операций.
        Если категория нет, она будет равна 0.
    """
    category_counts = defaultdict(int)

    # Инициализируем все категории с нулевым счётчиком
    for category in categories:
        category_counts[category] = 0

    # Подсчитываем операции
    for operation in operations:
        if 'description' not in operation:
            continue

        description = operation['description'].lower()
        for category in categories:
            if category.lower() in description:
                category_counts[category] += 1
                break  # Операция относится только к одной категории

    return dict(category_counts)
