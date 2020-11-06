import requests
import json

divinationStats = dict()
uniqueItems = dict()

def main():
    pullDivination()
    print("Divination Cards Pulled")
    pullUniqueStats()

def pullDivination():
    global divinationStats
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
            divinationStats.update({this_card:div_entry})
    
    print(divinationStats)

def pullUniqueStats():
    global uniqueItems
    updateUniqueDict("uniquearmor.json")
    updateUniqueDict("uniqueweapon.json")
    updateUniqueDict("uniqueaccessory.json")
    updateUniqueDict("uniqueflask.json")
    updateUniqueDict("uniquejewel.json")
    updateUniqueDict("prophecyoverview.json")

def updateUniqueDict(fileName):
    global uniqueItems
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
            uniqueItems.update({this_name:this_value})

def calculatePricePerStack():
    global divinationStats
    for x in divinationStats:
        basePrice = divinationStats[x]["cost"]
        stackSize = divinationStats[x]["stackSize"]
        totalCost = basePrice * stackSize
        divinationStats[x].update({"StackPrice":totalCost})

def calculateProfitPerStack():
    return ""

def getItemValue(itemName):
    global uniqueItems
    if uniqueItems[itemName] not None:
        return uniqueItems[itemName]

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
    main()