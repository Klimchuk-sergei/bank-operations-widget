import json
from typing import Dict, List, Union


def read_json_file(file_path: str) -> List[Dict[str, Union[str, float]]]:
    """Чтение Json файла и возвращение списка транзакций. если файл пустой, возвращается []"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
