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
        downList = []
        for y in exDown:
            downList.append(exDown[y]['difference'])
        checkUp = True
        checkDown = True
        for z in range(len(upList) - 1):
            if upList[z] < upList[z+1]:
                checkUp = False
        for w in range(len(downList) - 1):
            if downList[w] > downList[w+1]:
                checkDown = False
        self.assertTrue(checkUp, checkDown)

    def testSortCurrencyByROI(self):
        self.testController.getCurrencyData()
        roiUp = self.testController.sortCurrencyByROI()
        upList = []
        for x in roiUp:
            upList.append(roiUp[x]['ROI'])
        roiDown = self.testController.sortCurrencyByROI()
        downList = []
        for y in roiDown:
            downList.append(roiDown[y]['ROI'])
        checkUp = True
        checkDown = True
        for z in range(len(upList) - 1):
            if upList[z] < upList[z+1]:
                checkUp = False
        for w in range(len(downList) - 1):
            if downList[w] > downList[w+1]:
                checkDown = False
        self.assertTrue(checkUp, checkDown)

    def testSortDivinationByName(self):
        self.testController.getDivData()
        div_alphabet = self.testController.sortDivinationByName()
        div_reverse_Alphabet = self.testController.sortDivinationByName()
        forward_list = list(div_alphabet.keys())
        reverse_list = list(div_reverse_Alphabet.keys())
        checkF = True
        checkB = True
        for x in range(len(forward_list) - 1):
            if forward_list[x] > forward_list[x + 1]:
                checkF = False
        for y in range(len(reverse_list) - 1):
            if reverse_list[y] < reverse_list[y + 1]:
                checkB = False
        self.assertTrue(checkF, checkB)

    def testSortDivinationByProfitPerStack(self):
        self.testController.getDivData()
        stackUp = self.testController.sortDivinationByProfitPerStack()
        upList = []
        for x in stackUp:
            upList.append(stackUp[x]['difference'])
        stackDown = self.testController.sortDivinationByProfitPerStack()
        downList = []
        for y in stackDown:
            downList.append(stackDown[y]['difference'])
        checkUp = True
        checkDown = True
        for z in range(len(upList) - 1):
            if upList[z] < upList[z+1]:
                checkUp = False
        for w in range(len(downList) - 1):
            if downList[w] > downList[w+1]:
                checkDown = False
        self.assertTrue(checkUp, checkDown)

    def testSortDivinationByProfitPerCard(self):
        self.testController.getDivData()
        cardUp = self.testController.sortDivinationByProfitPerCard()
        upList = []
        for x in cardUp:
            upList.append(cardUp[x]['profitPerCard'])
        cardDown = self.testController.sortDivinationByProfitPerCard()
        downList = []
        for y in cardDown:
            downList.append(cardDown[y]['profitPerCard'])
        checkUp = True
        checkDown = True
        for z in range(len(upList) - 1):
            if upList[z] < upList[z+1]:
                checkUp = False
        for w in range(len(downList) - 1):
            if downList[w] > downList[w+1]:
                checkDown = False
        self.assertTrue(checkUp, checkDown)

    def testSortDivinationByROI(self):
        self.testController.getDivData()
        roidUp = self.testController.sortDivinationByROI()
        upList = []
        for x in roidUp:
            upList.append(roidUp[x]['ROI'])
        roidDown = self.testController.sortDivinationByROI()
        downList = []
        for y in roidDown:
            downList.append(roidDown[y]['ROI'])
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
        

