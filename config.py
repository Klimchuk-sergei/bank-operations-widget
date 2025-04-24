import logging
from pathlib import Path
from typing import Optional

# Базовые пути
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / 'data'
LOGS_DIR = BASE_DIR / 'logs'

# Создаем папки при необходимости
DATA_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)


def setup_logger(name: str) -> logging.Logger:
    """Централизованная настройка логгера"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler(
        filename=LOGS_DIR / f"{name}.log",
        mode='a',
        encoding='utf-8'
    )
    handler.setFormatter(logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    ))

    logger.addHandler(handler)
    return logger


def find_file_by_extension(extension: str) -> Optional[Path]:
    """Находит первый файл с указанным расширением в папке data"""
    for file in DATA_DIR.glob(f'*{extension}'):
        if file.is_file():
            return file
    return None
