import requests
import json
from CurrencyModel import CurrencyModel

class DivinationModel:
    divinationStats = dict()
    uniqueItems = dict()
    currencyModel = CurrencyModel()
    def __init__(self):
        self.pullDivination()
        print("Divination Cards Pulled")
        self.pullUniqueStats()
        self.getItemValue("Exalted Orb")

    def pullDivination(self):
        f = open("divinationoverview.json", "r")
        raw_data = f.read()
        #respDiv = requests.get("https://poe.ninja/api/data/itemoverview?league=Blight&type=DivinationCard")
        #raw_div_data = respDiv.content
        f.close()
        json_div_results = json.loads(raw_data)

        for x in range(len(json_div_results["lines"])):
            if(json_div_results["lines"][x]['chaosValue'] > 1):
                this_card = json_div_results["lines"][x]['name']
                this_value = json_div_results["lines"][x]['chaosValue']
                this_trade = json_div_results["lines"][x]['explicitModifiers'][0]["text"]
                this_trade = this_trade[this_trade.find("{")+1:this_trade.find("}")]
                this_stack = json_div_results["lines"][x]['stackSize']
                div_entry = {"cost":this_value, "item":this_trade, "stackSize":this_stack}
                self.divinationStats.update({this_card:div_entry})
       # print(self.divinationStats)

    def pullUniqueStats(self):
        self.updateUniqueDict("uniquearmor.json")
        self.updateUniqueDict("uniqueweapon.json")
        self.updateUniqueDict("uniqueaccessory.json")
        self.updateUniqueDict("uniqueflask.json")
        self.updateUniqueDict("uniquejewel.json")
        self.updateUniqueDict("prophecyoverview.json")

    def updateUniqueDict(self, fileName):
        f = open(fileName, "r")
        raw_data = f.read()
        f.close()
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

    def calculateProfitPerStack(self):
        return ""

    def getItemValue(self,itemName):
        #Check the Unique dictionary to see if its an item that exists inside it
        if itemName in self.uniqueItems:
            print(self.uniqueItems[itemName])
            return self.uniqueItems[itemName]
        else:
            currencyData = self.currencyModel.getCurrencyData()
            print(currencyData)
            if itemName in currencyData:
                print(currencyData[itemName]["ChaosEquivalent"])
                return currencyData[itemName]["ChaosEquivalent"]
            


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