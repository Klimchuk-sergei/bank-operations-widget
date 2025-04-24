# import csv
# import pandas as pd
#
# from typing import List, Dict
# from .file_path import validate_file_path
#
#
# def read_csv(file_name: str) -> List[Dict]:
#     """Чтение CSV файла из папки data/"""
#     file_path = validate_file_path(file_name, '.csv')
#     with open(file_path, 'r', encoding='utf-8') as f:
#         return list(csv.DictReader(f))
#
#
# def read_excel(file_name: str) -> List[Dict]:
#     """Чтение Excel файла из папки data/"""
#     file_path = validate_file_path(file_name, '.xlsx')
#     return pd.read_excel(file_path).to_dict('records')

import csv
import logging
from pathlib import Path
from typing import Dict, List

import openpyxl

logger = logging.getLogger(__name__)


def read_csv(file_path: str = None) -> List[Dict]:
    """Чтение транзакций из CSV файла с преобразованием структуры"""
    try:
        data_dir = Path(__file__).parent.parent / "data"

        # Поиск файла
        if file_path is None:
            for item in data_dir.iterdir():
                if item.suffix.lower() == '.csv':
                    path = item
                    logger.info(f"Автоматически выбран файл: {path.name}")
                    break
            else:
                logger.error("Не найден ни один CSV файл в папке data")
                return []
        else:
            path = Path(file_path)
            if not path.is_absolute():
                path = data_dir / path

        logger.info(f"Попытка чтения CSV файла: {path}")

        with open(path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            transactions = []

            for row in reader:
                # Преобразуем плоскую структуру в JSON-подобную
                transaction = {
                    "id": row.get("id", ""),
                    "date": row.get("date", ""),
                    "description": row.get("description", ""),
                    "from": row.get("from", ""),
                    "to": row.get("to", ""),
                    "operationAmount": {
                        "amount": row.get("amount", ""),
                        "currency": {
                            "code": row.get("currency_code", ""),
                            "name": row.get("currency_name", "")
                        }
                    },
                    "state": row.get("state", "")
                }
                transactions.append(transaction)

            logger.info(f"Успешно прочитано {len(transactions)} транзакций")
            return transactions

    except FileNotFoundError:
        logger.error(f"CSV файл не найден: {path}")
        return []
    except Exception as e:
        logger.error(f"Ошибка при чтении CSV: {str(e)}")
        return []


def read_excel(file_path: str = None) -> List[Dict]:
    """Чтение транзакций из Excel файла с преобразованием структуры"""
    try:
        data_dir = Path(__file__).parent.parent / "data"

        # Поиск файла
        if file_path is None:
            for item in data_dir.iterdir():
                if item.suffix.lower() == '.xlsx':
                    path = item
                    logger.info(f"Автоматически выбран файл: {path.name}")
                    break
            else:
                logger.error("Не найден ни один XLSX файл в папке data")
                return []
        else:
            path = Path(file_path)
            if not path.is_absolute():
                path = data_dir / path

        logger.info(f"Попытка чтения XLSX файла: {path}")

        workbook = openpyxl.load_workbook(path)
        sheet = workbook.active

        # Получаем заголовки
        headers = [str(cell.value).lower() if cell.value else f"column_{idx}"
                   for idx, cell in enumerate(sheet[1], 1)]

        transactions = []
        for row in sheet.iter_rows(min_row=2, values_only=True):
            row_dict = dict(zip(headers, row))

            # Преобразуем плоскую структуру в JSON-подобную
            transaction = {
                "id": str(row_dict.get("id", "")),
                "date": str(row_dict.get("date", "")),
                "description": str(row_dict.get("description", "")),
                "from": str(row_dict.get("from", "")),
                "to": str(row_dict.get("to", "")),
                "operationAmount": {
                    "amount": str(row_dict.get("amount", "")),
                    "currency": {
                        "code": str(row_dict.get("currency_code", "")),
                        "name": str(row_dict.get("currency_name", ""))
                    }
                },
                "state": str(row_dict.get("state", ""))
            }
            transactions.append(transaction)

        logger.info(f"Успешно прочитано {len(transactions)} транзакций")
        return transactions

    except FileNotFoundError:
        logger.error(f"XLSX файл не найден: {path}")
        return []
    except Exception as e:
        logger.error(f"Ошибка при чтении XLSX: {str(e)}")
        return []

# import csv
# import pandas as pd
# from typing import List, Dict
# from pathlib import Path
# import logging
# from src.file_path import validate_file_path
#
# logger = logging.getLogger(__name__)
#
#
# def read_csv(file_name: str = None) -> List[Dict]:
#     """Чтение CSV файла из папки data/"""
#     try:
#         if file_name is None:
#             # Автопоиск CSV файла
#             data_dir = Path(__file__).parent.parent / "data"
#             csv_files = list(data_dir.glob("*.csv"))
#             if not csv_files:
#                 raise FileNotFoundError("Не найден CSV файл в папке data")
#             file_name = csv_files[0].name
#
#         file_path = validate_file_path(file_name, '.csv')
#
#         with open(file_path, 'r', encoding='utf-8') as file:
#             reader = csv.DictReader(file)
#             transactions = []
#
#             for row in reader:
#                 transaction = {
#                     "id": row.get("id", ""),
#                     "date": row.get("date", ""),
#                     "description": row.get("description", ""),
#                     "from": row.get("from", ""),
#                     "to": row.get("to", ""),
#                     "operationAmount": {
#                         "amount": row.get("amount", ""),
#                         "currency": {
#                             "code": row.get("currency_code", ""),
#                             "name": row.get("currency_name", "")
#                         }
#                     },
#                     "state": row.get("state", "")
#                 }
#                 transactions.append(transaction)
#
#             return transactions
#
#     except Exception as e:
#         logger.error(f"Ошибка при чтении CSV: {str(e)}")
#         raise
#
#
# def read_excel(file_name: str) -> List[Dict]:
#     """Чтение Excel файла из папки data/"""
#     try:
#         file_path = validate_file_path(file_name, '.xlsx')
#         logger.info(f"Чтение Excel файла: {file_path}")
#
#         df = pd.read_excel(file_path)
#         transactions = df.to_dict('records')
#
#         logger.info(f"Успешно прочитано {len(transactions)} транзакций")
#         return transactions
#
#     except FileNotFoundError as e:
#         logger.error(f"Ошибка: {str(e)}")
#         raise
#     except ValueError as e:
#         logger.error(f"Ошибка: {str(e)}")
#         raise
#     except Exception as e:
#         logger.error(f"Ошибка при чтении Excel: {str(e)}")
#         raise
