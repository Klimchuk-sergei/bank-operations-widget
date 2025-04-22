from pathlib import Path
from typing import Union

# Пути рассчитываются относительно расположения этого файла в src/
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"


def validate_file_path(file_name: str, expected_ext: Union[str, tuple] = None) -> Path:
    """
    Проверяет существование файла в папке data/ и его расширение
    file_name: Имя файла (например, "transactions.csv")
    expected_ext: Ожидаемое расширение ('.csv', '.xlsx' или None)
    Path: Полный путь к файлу
    FileNotFoundError: Если файл не существует
    ValueError: Если расширение не соответствует
    """
    file_path = DATA_DIR / file_name

    if not file_path.exists():
        raise FileNotFoundError(f"Файл {file_name} не найден в {DATA_DIR}")

    if expected_ext:
        if isinstance(expected_ext, str):
            expected_ext = (expected_ext.lower(),)
        if file_path.suffix.lower() not in expected_ext:
            raise ValueError(f"Ожидалось расширение {expected_ext}, получено {file_path.suffix}")

    return file_path
