import unittest
import io
import sys
from unittest.case import expectedFailure
from Controller import Controller

class Test_Controller(unittest.TestCase):
    testController = Controller()
    
    def testGetCurrencyOptimal(self):
        self.testController.getCurrencyData()
        output = self.testController.calculateCurrencyOptimal(200)
        assert output is not None

    def testSortCurrencyByName(self):
        self.testController.getCurrencyData()
        alphabet = self.testController.sortCurrencyByName()
        reverse_Alphabet = self.testController.sortCurrencyByName()
        forward_list = list(alphabet.keys())
        reverse_list = list(reverse_Alphabet.keys())
        checkF = True
        checkB = True
        for x in range(len(forward_list) - 1):
            if forward_list[x] > forward_list[x + 1]:
                checkF = False
        for y in range(len(reverse_list) - 1):
            if reverse_list[y] < reverse_list[y + 1]:
                checkB = False
        self.assertTrue(checkF, checkB)

    def testSortCurrencyByExchange(self):
        self.testController.getCurrencyData()
        exUp = self.testController.sortCurrencyByExchange()
        upList = []
        for x in exUp:
            upList.append(exUp[x]['difference'])
        exDown = self.testController.sortCurrencyByExchange()
        print(exUp, "\n", exDown, "\n")
        downList = []
        for y in exDown:
            downList.append(exDown[y]['difference'])
        print(upList, "\n", downList)
        checkUp = True
        checkDown = True
        for z in range(len(upList) - 1):
            if upList[z] < upList[z+1]:
                checkUp = False
        for w in range(len(downList) - 1):
            if downList[w] > downList[w+1]:
                checkDown = False
        self.assertTrue(checkUp, checkDown)

if __name__ == "__main__":
    unittest.main()
        

