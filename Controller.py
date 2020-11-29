from operator import getitem
from typing import OrderedDict, Tuple
import requests
import math
import operator

from CurrencyModel import CurrencyModel
from DivinationModel import DivinationModel

class Controller:
    controllerCStats = dict()
    controllerDStats = dict()
    dModel = DivinationModel()
    cModel = dModel.currencyModel
    
    currencySort = "None"
    currencyDirection = False

    divinationSort = "None"
    divinationDirection = False

    def __init__(self):
        self.getCurrencyData()
        self.sortCurrencyByROI()
        self.getDivData()
        self.sortDivinationByROI()
        
    def getDivData(self):
        self.controllerDStats
        self.controllerDStats = self.dModel.getDivModel()
        self.divinationDirection = False
        self.divinationSort = "None"

    def getCurrencyData(self):
        #cModel = CurrencyModel()
        self.controllerCStats
        self.controllerCStats = self.cModel.getCurrencyData()
        self.currencyDirection = False
        self.currencySort = "None"

    def calculateCurrencyOptimal(self, chaosAmount: int):
        optimal_value = 0
        optimal_Currency = "None"
        currency_List = list(self.controllerCStats.keys())
        counter = 0
        for x in self.controllerCStats:
            currency_Name = currency_List[counter]
            currency_Get = math.floor(chaosAmount/self.controllerCStats[x]['pay'])
            if currency_Get > 1000:
                currency_Get = 1000
            currency_Return = currency_Get * self.controllerCStats[x]['ROI']
            #print("Current optimal is ", optimal_Currency, " at ", optimal_value)
            #print(currency_Name, " is worth ", currency_Return)
            if (currency_Return > optimal_value):
                optimal_value = currency_Return
                optimal_Currency = currency_Name
            counter = counter + 1
        #print (optimal_Currency, optimal_value)
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
        #print("\n By name: \n",nameCStats)
        return nameCStats

    def sortCurrencyByExchange(self):
        exchangeCStats = self.controllerCStats
        if (self.currencySort != "Exchange"):
            exchangeCStats = OrderedDict(sorted(self.controllerCStats.items(), key=lambda x:getitem(x[1],'difference'), reverse=True))
            self.currencySort = "Exchange"
            self.currencyDirection = True
        elif(self.currencySort == "Exchange" and self.currencyDirection == True):
            exchangeCStats = OrderedDict(sorted(self.controllerCStats.items(), key=lambda x:getitem(x[1],'difference')))
            self.currencyDirection = False
        else:
            exchangeCStats = OrderedDict(sorted(self.controllerCStats.items(), key=lambda x:getitem(x[1],'difference'), reverse=True))
            self.currencyDirection = True
        #print("\n By Exchange Difference: \n", exchangeCStats)
        return exchangeCStats

    def sortCurrencyByROI(self):
        roiCStats = self.controllerCStats
        if (self.currencySort != "ROI"):
            roiCStats = OrderedDict(sorted(self.controllerCStats.items(), key=lambda x:getitem(x[1],'ROI'), reverse=True))
            self.currencySort = "ROI"
            self.currencyDirection = True
        elif (self.currencySort == "ROI" and self.currencyDirection == True):
            roiCStats = OrderedDict(sorted(self.controllerCStats.items(), key=lambda x:getitem(x[1],'ROI')))
            self.currencyDirection = False
        else:
            roiCStats = OrderedDict(sorted(self.controllerCStats.items(), key=lambda x:getitem(x[1],'ROI'), reverse=True))
            self.currencyDirection = True
        #print("\n By ROI: \n",roiCStats)
        return roiCStats
    
    def sortDivinationByName(self):
        nameDStats = self.controllerDStats
        if (self.divinationSort != "Name"):
            nameDStats = OrderedDict(sorted(self.controllerDStats.items()))
            self.divinationDirection = True
            self.divinationSort = "Name"
        elif(self.divinationSort == "Name" and self.divinationDirection == True):
            nameDStats = OrderedDict(sorted(self.controllerDStats.items(), reverse = True))
            self.divinationDirection = False
        else:
            nameDStats = OrderedDict(sorted(self.controllerDStats.items()))
            self.divinationDirection = True
        #print("\n By name: \n",nameDStats)
        return nameDStats
    
    def sortDivinationByProfitPerStack(self):
        stackDStats = self.controllerDStats
        if (self.divinationSort != "Stack"):
            stackDStats = OrderedDict(sorted(self.controllerDStats.items(), key=lambda x:getitem(x[1], "difference"), reverse= True))
            self.divinationSort = "Stack"
            self.divinationDirection = True
        elif (self.divinationSort == "Stack" and self.divinationDirection == True):
            stackDStats = OrderedDict(sorted(self.controllerDStats.items(), key=lambda x:getitem(x[1], "difference")))
            self.divinationDirection = False
        else:
            stackDStats = OrderedDict(sorted(self.controllerDStats.items(), key=lambda x:getitem(x[1], "difference"), reverse= True ))
            self.divinationDirection = True
        #print("\n By Profit Per Stack: \n", stackDStats)
        return stackDStats

    def sortDivinationByProfitPerCard(self):
        cardDStats = self.controllerDStats
        if (self.divinationSort != "Card"):
            cardDStats = OrderedDict(sorted(self.controllerDStats.items(), key=lambda x:getitem(x[1], "profitPerCard"), reverse= True))
            self.divinationSort = "Card"
            self.divinationDirection = True
        elif(self.divinationSort == "Card" and self.divinationDirection == True):
            cardDStats = OrderedDict(sorted(self.controllerDStats.items(), key=lambda x:getitem(x[1], "profitPerCard")))
            self.divinationDirection = False
        else:
            cardDStats = OrderedDict(sorted(self.controllerDStats.items(), key=lambda x:getitem(x[1], "profitPerCard"), reverse= True))
            self.divinationDirection = True
        #print("\n By Profit Per Card: \n", cardDStats)
        return cardDStats
    
    def sortDivinationByROI(self):
        roiDStats = self.controllerDStats
        if (self.divinationSort != "ROI"):
            roiDStats = OrderedDict(sorted(self.controllerDStats.items(), key=lambda x:getitem(x[1], "ROI"), reverse= True))
            self.divinationSort = "ROI"
            self.divinationDirection = True
        elif(self.divinationSort == "ROI" and self.divinationDirection == True):
            roiDStats = OrderedDict(sorted(self.controllerDStats.items(), key=lambda x:getitem(x[1], "ROI")))
            self.divinationDirection = False
        else:
            roiDStats = OrderedDict(sorted(self.controllerDStats.items(), key=lambda x:getitem(x[1], "ROI"), reverse= True))
            self.divinationDirection = True
        #print("\n By ROI: \n", roiDStats)
        return roiDStats

    def filterCurrency(self):
        "empty"

    def filterDivination(self):
        "empty"

    def returnView(self):
        "empty"

if __name__ == '__main__':
    model = Controller()
