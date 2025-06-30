from src.description import count_operations_by_categories, filter_operations_by_description


def test_filter_operations_by_description() -> None:
    transactions = [
        {"id": 1, "description": "Оплата ЖКХ"},
        {"id": 2, "description": "Перевод другу"},
        {"id": 3, "description": "Покупка продуктов"},
        {"id": 4},  # Без описания
    ]

    # Тест 1: Поиск существующего слова
    result = filter_operations_by_description(transactions, r"оплата")
    assert len(result) == 1, f"Ожидалось 1 совпадение, получено {len(result)}"
    assert result[0]["id"] == 1, "Найден неверный элемент"

    # Тест 2: Поиск с учетом регистра
    result = filter_operations_by_description(transactions, r"ПЕРЕВОД")
    assert len(result) == 1, "Поиск должен быть регистронезависимым"

    # Тест 3: Поиск отсутствующего слова
    result = filter_operations_by_description(transactions, r"кредит")
    assert not result, "При отсутствии совпадений должен возвращаться пустой список"


def test_count_operations_by_categories() -> None:
    transactions = [
        {"description": "Оплата коммунальных услуг"},
        {"description": "Перевод на карту"},
        {"description": "Покупка в магазине"},
        {"description": "Оплата мобильной связи"},
        {},  # Без описания
    ]
    categories = ["оплата", "перевод", "покупка", "кредит"]

    # Тест 1: Стандартный случай
    counts = count_operations_by_categories(transactions, categories)
    assert counts == {"оплата": 2, "перевод": 1, "покупка": 1, "кредит": 0}, f"Некорректный подсчет: {counts}"

    # Тест 2: Пустые входные данные
    assert count_operations_by_categories([], categories) == {k: 0 for k in categories}
    assert count_operations_by_categories(transactions, []) == {}

    # Тест 3: Разный регистр категорий
    counts = count_operations_by_categories(transactions, ["ОПЛАТА", "Перевод", "ПоКуПка"])
    assert counts["ОПЛАТА"] == 2, "Должен игнорировать регистр категорий"
