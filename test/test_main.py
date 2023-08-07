import unittest
import asyncio
from poe_calculator.currency import get_currency_json

class TestCurrency(unittest.TestCase):
    def test_currency_crucible(self):
        assert asyncio.run(get_currency_json(league='Crucible', type='Currency'))
    def test_currency_crucible_hc(self):
        assert asyncio.run(get_currency_json(league='Crucible Hardcore', type='Currency'))
    def test_currency_standard(self):
        assert asyncio.run(get_currency_json(league='Standard', type='Currency'))
    def test_currency_hardcore(self):
        assert asyncio.run(get_currency_json(league='Hardcore', type='Currency'))
        
if __name__ == '__main__':
    unittest.main()
        
        



