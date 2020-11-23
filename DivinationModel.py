import requests
import json

divinationStats = dict()

def pullDivination():
    global divinationStats
    respDiv = requests.get("https://poe.ninja/api/data/itemoverview?league=Blight&type=DivinationCard")
    raw_div_data = respDiv.content
    json_div_results = json.loads(raw_div_data)

    for x in range(len(json_div_results["lines"])):
        this_card = json_div_results["lines"][x]['name']
        this_value = json_div_results["lines"][x]['chaosValue']
        this_trade = json_div_results["lines"][x]['explicitModifiers']
        this_stack = json_div_results["lines"][x]['stackSize']
        divinationStats.update({this_card:[this_value,this_trade,this_stack]})

    print(divinationStats)

def calculatePricePerStack():
    global divinationStats
    for x in divinationStats:
        basePrice = divinationStats[x][1]
        stackSize = divinationStats[x][3]
        this_stackPrice = basePrice * stackSize
        divinationStats[x].update({"StackPrice":this_stackPrice})

""" def calculateProfitPerStack():
    global divinationStats
    from CurrencyModel import currencyStats
    for x in divinationStats:
        this_modifier = divinationStats[x][2]
        this_stackPrice = divinationStats[x]["StackPrice"]
        this_modPrice = 0
        if this_modifier in currencyStats:
            this_modPrice =  """