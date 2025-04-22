import pytest
from unittest.mock import patch, mock_open, MagicMock
from src.read_csv_xlsx import read_csv, read_excel

TEST_CSV_DATA = """id,transaction,amount
1,Payment,100.50
2,Transfer,200.75"""

TEST_EXCEL_DATA = [
    {"id": 1, "transaction": "Payment", "amount": 100.50},
    {"id": 2, "transaction": "Transfer", "amount": 200.75}
]


# Тест 1: Успешное чтение CSV
@patch('src.read_csv_xlsx.validate_file_path')
def test_read_csv_returns_correct_data(mock_validate):
    """Проверяем, что read_csv корректно читает данные"""

    mock_validate.return_value = "/fake/path.csv"

    with patch('builtins.open', mock_open(read_data=TEST_CSV_DATA)):
        result = read_csv("transactions.csv")

        # Проверяем результаты
        assert len(result) == 2
        assert result[0]["transaction"] == "Payment"
        assert result[1]["amount"] == "200.75"
        mock_validate.assert_called_once_with("transactions.csv", ".csv")


# Тест 2: Ошибка при отсутствии CSV файла
@patch('src.read_csv_xlsx.validate_file_path')
def test_read_csv_handles_missing_file(mock_validate):
    """Проверяем обработку отсутствия файла"""
    mock_validate.side_effect = FileNotFoundError("File not found")

    with pytest.raises(FileNotFoundError):
        read_csv("missing.csv")


# Тест 3: Успешное чтение Excel
@patch('src.read_csv_xlsx.validate_file_path')
@patch('pandas.read_excel')
def test_read_excel_returns_correct_data(mock_read_excel, mock_validate):
    """
    Тестируем что:
    1. Функция корректно читает Excel файлы
    2. Проверяет только .xlsx расширение
    3. Возвращает правильные данные
    """
    # Настраиваем моки
    mock_validate.return_value = "/fake/path.xlsx"
    mock_df = MagicMock()
    mock_df.to_dict.return_value = TEST_EXCEL_DATA
    mock_read_excel.return_value = mock_df

    # Вызываем тестируемую функцию
    result = read_excel("transactions.xlsx")

    # Проверяем результаты
    assert len(result) == 2
    assert result[1]["amount"] == 200.75

    # Проверяем что validate_file_path вызвана с правильными параметрами
    mock_validate.assert_called_once_with("transactions.xlsx", ".xlsx")


# Тест 4: Ошибка при неверном формате Excel
@patch('src.read_csv_xlsx.validate_file_path')
def test_read_excel_handles_wrong_format(mock_validate):
    """Проверяем обработку неверного формата файла"""
    mock_validate.side_effect = ValueError("Invalid file format")

    with pytest.raises(ValueError):
        read_excel("invalid.txt")
