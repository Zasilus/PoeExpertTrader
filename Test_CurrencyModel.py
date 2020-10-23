import unittest
import io
import sys
from CurrencyModel import *

class Test_CurrencyModel(unittest.TestCase):
   
    def test_calculateExchangeDifference(self):
        pullCurrency()
        calculateExchangeDifference()
        check = True
        for x in currencyStats:
            inner_check = False
            if 'difference' in currencyStats[x]:
                inner_check = True
            if (inner_check == False):
                check = False
        self.assertTrue(check)

    def test_calculateROI(self):
        pullCurrency()
        calculateROI()
        check = True
        for x in currencyStats:
            inner_check = False
            if 'ROI' in currencyStats[x]:
                inner_check = True
            if (inner_check == False):
                check = False
        self.assertTrue(check)
    
    def test_getCurrencyData(self):
        pullCurrency()
        output = getCurrencyData()
        assert output is not None
    
    def test_main(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        main()
        sys.stdout = sys.__stdout__
        assert capturedOutput.getvalue() is not None

if __name__ == "__main__":
    unittest.main()