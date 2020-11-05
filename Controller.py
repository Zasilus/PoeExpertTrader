from operator import getitem
from typing import OrderedDict
import requests
import math
import operator

import CurrencyModel
import DivinationModel

controllerCStats = dict()

def main():
    getCurrencyData()
    print(controllerCStats)
    sortCurrencyByName()
    sortCurrencyByExchange()
    sortCurrencyByROI()

def getDivData():
    "comment"

def getCurrencyData():
    CurrencyModel.main()
    global controllerCStats
    controllerCStats = CurrencyModel.getCurrencyData()

def calculateCurrencyOptimal(chaosAmount: int):
    optimal_value = 0
    optimal_Currency = "None"
    for x in controllerCStats:
        currency_Name = controllerCStats[x]
        currency_Get = math.floor(controllerCStats[x]['pay']/chaosAmount)
        currency_Return = currency_Get * controllerCStats[x]['ROI']
        if (currency_Return > optimal_value):
            optimal_value = currency_Return
            optimal_Currency = currency_Name
    return optimal_Currency
    
def sortCurrencyByName():
    global controllerCStats
    nameCStats = OrderedDict(sorted(controllerCStats.items()))
    print("\n By name: \n",nameCStats)
    return nameCStats

def sortCurrencyByExchange():
    global controllerCStats
    exchangeCStats = sorted(controllerCStats.items(), key=lambda x:getitem(x[1],'difference'), reverse=True)
    print("\n By Exchange Difference: \n", exchangeCStats)
    return exchangeCStats

def sortCurrencyByROI():
    global controllerCStats
    roiCStats = sorted(controllerCStats.items(), key=lambda x:getitem(x[1],'ROI'), reverse=True)
    print("\n By ROI: \n",roiCStats)
    return roiCStats

if __name__ == '__main__':
    main()
