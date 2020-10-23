import unittest
from CurrencyModel import *

class Test_CurrencyModel(unittest.TestCase):

    def test_pullCurrency():
        pullCurrency()
        assert currencyStats is not None
    
    def test_calculateExchangeDifference():
        calculateExchangeDifference()
        check = True
        for x in currencyStats:
            inner_check = False
            if 'difference' in currencyStats[x]:
                inner_check = True
            if (inner_check == False):
                check = False
        