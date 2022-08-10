from unittest import result
from app.expense import convert_currency, list_currency

def test_convert_currency():
    result = convert_currency(currency_base = 'USD', currency_output = 'EUR', cost = '100')
    assert isinstance(result, float)

def test_list_currency():
    result = list_currency()
    assert isinstance(result, list)

    