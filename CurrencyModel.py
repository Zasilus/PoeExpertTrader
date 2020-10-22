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