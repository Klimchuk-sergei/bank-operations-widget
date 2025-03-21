import pytest
from src.processing import filter_by_state, sort_by_date

# Фикстуры для тестовых данных
@pytest.fixture
def sample_operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-10-01T12:34:56.789"},
        {"id": 2, "state": "PENDING", "date": "2023-09-15T08:20:10.123"},
        {"id": 3, "state": "EXECUTED", "date": "2023-08-20T15:45:30.456"},
        {"id": 4, "state": "CANCELED", "date": "2023-07-05T10:10:10.101"},
    ]

# Тесты для filter_by_state
def test_filter_by_state_executed(sample_operations):
    filtered = filter_by_state(sample_operations, "EXECUTED")
    assert len(filtered) == 2
    assert all(op["state"] == "EXECUTED" for op in filtered)

def test_filter_by_state_pending(sample_operations):
    filtered = filter_by_state(sample_operations, "PENDING")
    assert len(filtered) == 1
    assert all(op["state"] == "PENDING" for op in filtered)

# Тесты для sort_by_date
def test_sort_by_date_ascending(sample_operations):
    sorted_ops = sort_by_date(sample_operations, reverse=False)
    assert sorted_ops[0]["date"] == "2023-07-05T10:10:10.101"
    assert sorted_ops[-1]["date"] == "2023-10-01T12:34:56.789"

def test_sort_by_date_descending(sample_operations):
    sorted_ops = sort_by_date(sample_operations, reverse=True)
    assert sorted_ops[0]["date"] == "2023-10-01T12:34:56.789"
    assert sorted_ops[-1]["date"] == "2023-07-05T10:10:10.101"
