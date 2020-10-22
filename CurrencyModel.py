import requests
import json

resp = requests.get("https://poe.ninja/api/data/currencyoverview?league=Heist&type=Currency")
raw_data = resp.content
json_result = json.loads(raw_data)
print(range(len(json_result["lines"])))
#for n in range(len(json_result["lines"])):
    #print(json_result["lines"][n])

currencyStats = dict()
for x in range(len(json_result["lines"])):
    this_currency = json_result["lines"][x]['currencyTypeName']
    this_price = json_result["lines"][x]['chaosEquivalent']
    currencyStats.update({this_currency:this_price})

print(currencyStats)

respDiv = requests.get("https://poe.ninja/api/data/itemoverview?league=Blight&type=DivinationCard")
raw_div_data = respDiv.content
json_div_results = json.loads(raw_div_data)

divinationStats = dict()
for x in range(len(json_div_results["lines"])):
    this_card = json_div_results["lines"][x]['name']
    this_value = json_div_results["lines"][x]['chaosValue']
    this_trade = json_div_results["lines"][x]['explicitModifiers']
    this_stack = json_div_results["lines"][x]['stackSize']
    divinationStats.update({this_card:[this_value,this_trade,this_stack]})

print(divinationStats)