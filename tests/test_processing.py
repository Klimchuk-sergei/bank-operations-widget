from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


# Фикстуры для тестовых данных
@pytest.fixture
def sample_operations() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-10-01T12:34:56.789"},
        {"id": 2, "state": "PENDING", "date": "2023-09-15T08:20:10.123"},
        {"id": 3, "state": "EXECUTED", "date": "2023-08-20T15:45:30.456"},
        {"id": 4, "state": "CANCELED", "date": "2023-07-05T10:10:10.101"},
    ]


# Параметризация для тестов filter_by_state
@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [1, 3]),  # Ожидаемые ID для состояния "EXECUTED"
        ("PENDING", [2]),  # Ожидаемые ID для состояния "PENDING"
        ("CANCELED", [4]),  # Ожидаемые ID для состояния "CANCELED"
        ("INVALID", []),  # Некорректное состояние, ожидается пустой список
    ],
)
def test_filter_by_state(sample_operations: List[Dict[str, Any]], state: str, expected_ids: List[int]) -> None:
    filtered = filter_by_state(sample_operations, state)
    assert [op["id"] for op in filtered] == expected_ids


# Параметризация для тестов sort_by_date
@pytest.mark.parametrize(
    "reverse, expected_first_date, expected_last_date",
    [
        (False, "2023-07-05T10:10:10.101", "2023-10-01T12:34:56.789"),  # По возрастанию
        (True, "2023-10-01T12:34:56.789", "2023-07-05T10:10:10.101"),  # По убыванию
    ],
)
def test_sort_by_date(
    sample_operations: List[Dict[str, Any]],
    reverse: bool,
    expected_first_date: str,
    expected_last_date: str,
) -> None:
    sorted_ops = sort_by_date(sample_operations, reverse=reverse)
    assert sorted_ops[0]["date"] == expected_first_date
    assert sorted_ops[-1]["date"] == expected_last_date
