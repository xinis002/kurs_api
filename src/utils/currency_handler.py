import json


def get_currency_transfer(currency: str) -> str:
    """
    Функция, которая преобразует обозначение валюты из строки в её русскоязычное представление,
    принимая на вход код валюты и возвращая его название на русском языке.

    """
    with open("./data/name_currencies.json") as f:
        f = json.load(f)
        return f.get(currency)