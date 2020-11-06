import unittest
import io
import sys
from CurrencyModel import CurrencyModel

class Test_CurrencyModel(unittest.TestCase):
    testCurrency = CurrencyModel()
    def test_calculateExchangeDifference(self):
        self.testCurrency.pullCurrency()
        self.testCurrency.calculateExchangeDifference()
        check = True
        for x in self.testCurrency.currencyStats:
            inner_check = False
            if 'difference' in self.testCurrency.currencyStats[x]:
                inner_check = True
            if (inner_check == False):
                check = False
        self.assertTrue(check)

    def test_calculateROI(self):
        self.testCurrency.pullCurrency()
        self.testCurrency.calculateROI()
        check = True
        for x in self.testCurrency.currencyStats:
            inner_check = False
            if 'ROI' in self.testCurrency.currencyStats[x]:
                inner_check = True
            if (inner_check == False):
                check = False
        self.assertTrue(check)
    
    def test_getCurrencyData(self):
        self.testCurrency.pullCurrency()
        output = self.testCurrency.getCurrencyData()
        assert output is not None
    
    def test_main(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.testCurrency.__init__()
        sys.stdout = sys.__stdout__
        assert capturedOutput.getvalue() is not None

if __name__ == "__main__":
    unittest.main()