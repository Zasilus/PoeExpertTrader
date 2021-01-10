import requests
import json
import re
from CurrencyModel import CurrencyModel

class DivinationModel:
    currentLeague = "Heist"
    divinationStats = None
    uniqueItems = None
    currencyModel = None
    def __init__(self):
        self.divinationStats = dict()
        self.uniqueItems = dict()
        self.currencyModel = CurrencyModel()
        self.pullUniqueStats()

    def main(self):
        self.pullDivination()
        self.calculateROI()
        self.calculateProfitPerCard()
        return self.divinationStats

    def pullDivination(self):
        #f = open("divinationoverview.json", "r")
        #raw_div_data = f.read()
        respDiv = requests.get("https://poe.ninja/api/data/itemoverview?league="+self.currentLeague+"&type=DivinationCard")
        raw_div_data = respDiv.content
        #f.close()
        json_div_results = json.loads(raw_div_data)

        for x in range(len(json_div_results["lines"])):
            if(json_div_results["lines"][x]['chaosValue'] > 1):
                this_card = json_div_results["lines"][x]['name']
                this_value = json_div_results["lines"][x]['chaosValue']
                this_trade = json_div_results["lines"][x]['explicitModifiers'][0]["text"]
                this_trade = this_trade[this_trade.find("{")+1:this_trade.find("}")]
                this_stack = json_div_results["lines"][x]['stackSize']
                if this_stack == 0:
                    this_stack = 1
                div_entry = {"cost":this_value, "item":this_trade, "stackSize":this_stack}
                self.divinationStats.update({this_card:div_entry})
       # print(self.divinationStats)

    def pullUniqueStats(self):
        self.updateUniqueDict("UniqueArmour")
        self.updateUniqueDict("UniqueWeapon")
        self.updateUniqueDict("UniqueAccessory")
        self.updateUniqueDict("UniqueFlask")
        self.updateUniqueDict("UniqueJewel")
        self.updateUniqueDict("Prophecy")
        self.updateUniqueDict("UniqueMap")

    def updateUniqueDict(self, fileName):
        respDiv = requests.get("https://poe.ninja/api/data/itemoverview?league=" + self.currentLeague + "&type=" + fileName)
        raw_data = respDiv.content
        json_result = json.loads(raw_data)

        for x in range(len(json_result["lines"])):
            entry = json_result["lines"][x]
            #We are limiting the entries to non 6 links and chaosValues over 1 as theres no point
            #in attempting to flip below the 2 chaos threshold and 6 links are a different much
            #rarer form of the item that 
            if entry["links"] != 6 and entry['chaosValue'] > 2:
                this_name = entry['name']
                this_value = entry['chaosValue']
                self.uniqueItems.update({this_name:this_value})

    def calculatePricePerStack(self):
        for x in self.divinationStats:
            basePrice = self.divinationStats[x]["cost"]
            stackSize = self.divinationStats[x]["stackSize"]
            totalCost = basePrice * stackSize
            self.divinationStats[x].update({"StackPrice":totalCost})

    def calculateSellValue(self):
        del_dict = []
        for x in self.divinationStats:
            itemName = self.divinationStats[x]["item"]
            itemValue = self.getItemValue(itemName)
            if itemValue  == 0:
                del_dict.append(x)
            else:
                self.divinationStats[x].update({"SellValue":itemValue})
        #We delete everything we cannot determine the sell value for
        for x in del_dict:
            del self.divinationStats[x]
    
    def calculateProfitPerStack(self):
        self.calculateSellValue()
        self.calculatePricePerStack()
        for x in self.divinationStats:
            difference = self.divinationStats[x]["SellValue"] - self.divinationStats[x]["StackPrice"]
            self.divinationStats[x].update({"difference":difference})
    
    def calculateProfitPerCard(self):
        self.calculateProfitPerStack()
        for x in self.divinationStats:
            difference = self.divinationStats[x]['difference']
            stackSize = self.divinationStats[x]['stackSize']
            profit = difference / stackSize
            self.divinationStats[x].update({"profitPerCard":profit})

    def calculateROI(self):
        self.calculateProfitPerStack()
        for x in self.divinationStats:
            difference = self.divinationStats[x]['difference']
            value = self.divinationStats[x]['StackPrice']
            if value != 0.0:
                roi = difference / value
            self.divinationStats[x].update({"ROI":roi})
    
    def getDivModel(self):
        return self.divinationStats
    # def calculateProfitPerStack(self):
    #     for x in self.divinationStats:


    def getItemValue(self,itemName):
        #Check the Unique dictionary to see if its an item that exists inside it
        if itemName in self.uniqueItems:
            return self.uniqueItems[itemName]
        else:
            #Check to see if it is in the currency dictionary if it isn't we will have to check for for example 10x item
            currencyData = self.currencyModel.getCurrencyData()
            if itemName in currencyData:
                return currencyData[itemName]["ChaosEquivalent"]
            #Checking to see if it is multiple currencies
            elif bool(re.search(r'\dx', itemName)):
                item = itemName[itemName.find(' ')+1:]
                quantity = int(itemName[0:itemName.find('x')])
                currencyPrice = currencyData[item]["ChaosEquivalent"]
                return quantity * currencyPrice
            else:
                return 0
            


""" def calculateProfitPerStack():
    global divinationStats
    from CurrencyModel import currencyStats
    for x in divinationStats:
        this_modifier = divinationStats[x][2]
        this_stackPrice = divinationStats[x]["StackPrice"]
        this_modPrice = 0
        if this_modifier in currencyStats:
            this_modPrice =  """

if __name__ == '__main__':
    divModel = DivinationModel()
    divModel.main()