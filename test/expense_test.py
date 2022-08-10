from app.expense import convert_currency

def test_convert_currency():
    result = convert_currency(currency_base = 'USD', currency_output = 'EUR', cost = '100')
    assert isinstance(result, float)