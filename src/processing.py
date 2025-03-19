def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует список операций по статусу.
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует список операций по дате.
    """
    return sorted(operations, key=lambda x: x["date"], reverse=reverse)
