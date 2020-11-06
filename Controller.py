from operator import getitem
from typing import OrderedDict, Tuple
import requests
import math
import operator

from CurrencyModel import CurrencyModel
import DivinationModel

class Controller:
    controllerCStats = dict()
    cModel = CurrencyModel()

    currencySort = "None"
    currencyDirection = False

    divinationSort = "None"
    divinationDirection = False

    def __init__(self):
        self.getCurrencyData()
        print(self.currencySort)
        print(self.currencyDirection)
        self.sortCurrencyByName()
        print(self.currencySort)
        print(self.currencyDirection)
        self.sortCurrencyByName()
        print(self.currencySort)
        print(self.currencyDirection)
        self.sortCurrencyByExchange()
        print(self.currencySort)
        print(self.currencyDirection)
        self.sortCurrencyByExchange()
        print(self.currencySort)
        print(self.currencyDirection)
        self.sortCurrencyByExchange()
        print(self.currencySort)
        print(self.currencyDirection)
        self.sortCurrencyByROI()
        print(self.currencySort)
        print(self.currencyDirection)

    def main(self):
        self.getCurrencyData()
        print(self.controllerCStats)
        name = self.sortCurrencyByName()
        print(name)
        self.sortCurrencyByExchange()
        self.sortCurrencyByROI()

    def getDivData(self):
        "comment"

    def getCurrencyData(self):
        #cModel = CurrencyModel()
        self.controllerCStats
        self.controllerCStats = self.cModel.getCurrencyData()
        self.currencyDirection = False
        self.currencySort = "None"

    def calculateCurrencyOptimal(self, chaosAmount: int):
        optimal_value = 0
        optimal_Currency = "None"
        for x in self.controllerCStats:
            currency_Name = self.controllerCStats[x]
            currency_Get = math.floor(self.controllerCStats[x]['pay']/chaosAmount)
            currency_Return = currency_Get * self.controllerCStats[x]['ROI']
            if (currency_Return > optimal_value):
                optimal_value = currency_Return
                optimal_Currency = currency_Name
        return optimal_Currency
        
    def sortCurrencyByName(self):
        nameCStats = self.controllerCStats
        if (self.currencySort != "Name"):
            nameCStats = OrderedDict(sorted(self.controllerCStats.items()))
            self.currencySort = "Name"
            self.currencyDirection = True
        elif (self.currencySort == "Name" and self.currencyDirection == True):
            nameCStats = OrderedDict(sorted(self.controllerCStats.items(), reverse= True))
            self.currencyDirection = False
        else:
            nameCStats = OrderedDict(sorted(self.controllerCStats.items()))
            self.currencyDirection = True
        print("\n By name: \n",nameCStats)
        return nameCStats

    def sortCurrencyByExchange(self):
        exchangeCStats = self.controllerCStats
        if (self.currencySort != "Exchange"):
            exchangeCStats = sorted(self.controllerCStats.items(), key=lambda x:getitem(x[1],'difference'), reverse=True)
            self.currencySort = "Exchange"
            self.currencyDirection = True
        elif(self.currencySort == "Exchange" and self.currencyDirection == True):
            exchangeCStats = sorted(self.controllerCStats.items(), key=lambda x:getitem(x[1],'difference'))
            self.currencyDirection = False
        else:
            exchangeCStats = sorted(self.controllerCStats.items(), key=lambda x:getitem(x[1],'difference'), reverse=True)
            self.currencyDirection = True
        print("\n By Exchange Difference: \n", exchangeCStats)
        return exchangeCStats

    def sortCurrencyByROI(self):
        roiCStats = self.controllerCStats
        if (self.currencySort != "ROI"):
            roiCStats = sorted(self.controllerCStats.items(), key=lambda x:getitem(x[1],'ROI'), reverse=True)
            self.currencySort = "ROI"
            self.currencyDirection = True
        elif (self.currencySort == "ROI" and self.currencyDirection == True):
            roiCStats = sorted(self.controllerCStats.items(), key=lambda x:getitem(x[1],'ROI'))
            self.currencyDirection = False
        else:
            roiCStats = sorted(self.controllerCStats.items(), key=lambda x:getitem(x[1],'ROI'), reverse=True)
            self.currencyDirection = True
        print("\n By ROI: \n",roiCStats)
        return roiCStats

if __name__ == '__main__':
    model = Controller()
