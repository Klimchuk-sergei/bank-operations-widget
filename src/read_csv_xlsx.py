import csv
import pandas as pd

from typing import List, Dict
from .file_path import validate_file_path


def read_csv(file_name: str) -> List[Dict]:
    """Чтение CSV файла из папки data/"""
    file_path = validate_file_path(file_name, '.csv')
    with open(file_path, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def read_excel(file_name: str) -> List[Dict]:
    """Чтение Excel файла из папки data/"""
    file_path = validate_file_path(file_name, '.xlsx')
    return pd.read_excel(file_path).to_dict('records')
