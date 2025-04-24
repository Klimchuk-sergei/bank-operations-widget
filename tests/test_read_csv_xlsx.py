# import pytest
# from unittest.mock import patch, mock_open, MagicMock
# from src.read_csv_xlsx import read_csv, read_excel
#
# TEST_CSV_DATA = """id,transaction,amount
# 1,Payment,100.50
# 2,Transfer,200.75"""
#
# TEST_EXCEL_DATA = [
#     {"id": 1, "transaction": "Payment", "amount": 100.50},
#     {"id": 2, "transaction": "Transfer", "amount": 200.75}
# ]
#
#
# # Тест 1: Успешное чтение CSV
# @patch('src.read_csv_xlsx.validate_file_path')
# def test_read_csv_returns_correct_data(mock_validate):
#     """Проверяем, что read_csv корректно читает данные"""
#
#     mock_validate.return_value = "/fake/path.csv"
#
#     with patch('builtins.open', mock_open(read_data=TEST_CSV_DATA)):
#         result = read_csv("transactions.csv")
#
#         # Проверяем результаты
#         assert len(result) == 2
#         assert result[0]["transaction"] == "Payment"
#         assert result[1]["amount"] == "200.75"
#         mock_validate.assert_called_once_with("transactions.csv", ".csv")
#
#
# # Тест 2: Ошибка при отсутствии CSV файла
# @patch('src.read_csv_xlsx.validate_file_path')
# def test_read_csv_handles_missing_file(mock_validate):
#     """Проверяем обработку отсутствия файла"""
#     mock_validate.side_effect = FileNotFoundError("File not found")
#
#     with pytest.raises(FileNotFoundError):
#         read_csv("missing.csv")
#
#
# # Тест 3: Успешное чтение Excel
# @patch('src.read_csv_xlsx.validate_file_path')
# @patch('pandas.read_excel')
# def test_read_excel_returns_correct_data(mock_read_excel, mock_validate):
#     """
#     Тестируем что:
#     1. Функция корректно читает Excel файлы
#     2. Проверяет только .xlsx расширение
#     3. Возвращает правильные данные
#     """
#     # Настраиваем моки
#     mock_validate.return_value = "/fake/path.xlsx"
#     mock_df = MagicMock()
#     mock_df.to_dict.return_value = TEST_EXCEL_DATA
#     mock_read_excel.return_value = mock_df
#
#     # Вызываем тестируемую функцию
#     result = read_excel("transactions.xlsx")
#
#     # Проверяем результаты
#     assert len(result) == 2
#     assert result[1]["amount"] == 200.75
#
#     # Проверяем что validate_file_path вызвана с правильными параметрами
#     mock_validate.assert_called_once_with("transactions.xlsx", ".xlsx")
#
#
# # Тест 4: Ошибка при неверном формате Excel
# @patch('src.read_csv_xlsx.validate_file_path')
# def test_read_excel_handles_wrong_format(mock_validate):
#     """Проверяем обработку неверного формата файла"""
#     mock_validate.side_effect = ValueError("Invalid file format")
#
#     with pytest.raises(ValueError):
#         read_excel("invalid.txt")

from unittest.mock import MagicMock, mock_open, patch

from src.read_csv_xlsx import read_csv, read_excel

# Тестовые данные
TEST_CSV_DATA = """id,date,description,from,to,amount,currency_code,currency_name,state
1,2023-01-01,Payment,Card 1234,Account 5678,100.00,USD,Dollar,EXECUTED
2,2023-01-02,Transfer,Account 5678,Account 9012,200.50,EUR,Euro,EXECUTED"""


# Тесты для read_csv()
def test_read_csv_auto_find_file():
    """Тест автоматического поиска CSV файла"""
    with patch("pathlib.Path.iterdir") as mock_iterdir:
        mock_file = MagicMock()
        mock_file.name = "transactions.csv"
        mock_file.suffix = ".csv"
        mock_file.is_file.return_value = True
        mock_iterdir.return_value = [mock_file]

        with patch("builtins.open", mock_open(read_data=TEST_CSV_DATA)):
            with patch("pathlib.Path.exists", return_value=True):
                result = read_csv()
                assert len(result) == 2
                assert result[0]["operationAmount"]["currency"]["code"] == "USD"
                assert result[1]["state"] == "EXECUTED"


def test_read_csv_specific_file():
    """Тест чтения конкретного CSV файла"""
    test_file = "specific.csv"
    with patch("builtins.open", mock_open(read_data=TEST_CSV_DATA)):
        with patch("pathlib.Path.exists", return_value=True):
            with patch("pathlib.Path.is_file", return_value=True):
                result = read_csv(test_file)
                assert len(result) == 2
                assert result[1]["operationAmount"]["amount"] == "200.50"


def test_read_csv_file_not_found():
    """Тест обработки отсутствия файла"""
    with patch("pathlib.Path.exists", return_value=False):
        result = read_csv("missing.csv")
        assert result == []


def test_read_csv_invalid_data():
    """Тест обработки невалидных данных"""
    with patch("builtins.open", mock_open(read_data="invalid,data\n1,2")):
        with patch("pathlib.Path.exists", return_value=True):
            with patch("csv.DictReader") as mock_reader:
                mock_reader.return_value = []
                result = read_csv("bad.csv")
                assert result == []


# Тесты для read_excel() - только базовые, без проверки содержимого
def test_read_excel_file_not_found():
    """Тест обработки отсутствия файла"""
    with patch("pathlib.Path.exists", return_value=False):
        result = read_excel("missing.xlsx")
        assert result == []


def test_read_excel_invalid_data():
    """Тест обработки невалидных данных"""
    with patch("openpyxl.load_workbook", side_effect=Exception("Invalid file")):
        with patch("pathlib.Path.exists", return_value=True):
            result = read_excel("bad.xlsx")
            assert result == []
