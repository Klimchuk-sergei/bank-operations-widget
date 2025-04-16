import json
import logging
from pathlib import Path
from typing import Dict, List, Union

# Настройка логгера
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

# Создание папки logs в корне проекта
LOG_DIR = Path(__file__).parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

# Настройка FileHandler
file_handler = logging.FileHandler(
    filename=LOG_DIR / "utils.log",
    mode="w",
    encoding="utf-8"
)
file_handler.setLevel(logging.DEBUG)

# Настройка Formatter
file_formatter = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def read_json_file(file_path: str) -> List[Dict[str, Union[str, float]]]:
    """Чтение Json файла и возвращение списка транзакций. Если файл пустой, возвращается []"""
    try:
        logger.debug(f"Попытка чтения файла: {file_path}")

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                logger.info(f"Успешно прочитано {len(data)} транзакций из файла {file_path}")
                return data

            logger.warning(f"Файл {file_path} не содержит список транзакций")
            return []

    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []

    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле: {file_path}")
        return []

    except Exception as e:
        logger.error(f"Неожиданная ошибка при чтении файла {file_path}: {str(e)}", exc_info=True)
        return []
