import os
from typing import Dict, Union

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")


def convert_to_rub(transaction: Dict[str, Union[str, float]]) -> float:
    """Конвертируем сумму в рубли"""
    amount = transaction.get("amount", 0.0)
    currency = transaction.get("currency", "RUB")

    if currency == "RUB":
        return float(amount)

    try:
        response = requests.get(API_URL, headers={"apikey": API_KEY}, params={"base": currency, "symbols": "RUB"})
        response.raise_for_status()
        rate = response.json()["rates"]["RUB"]
        return float(amount) * rate
    except (requests.RequestException, KeyError):
        return 0.0
