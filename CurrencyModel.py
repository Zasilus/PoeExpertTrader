import requests
import json

resp = requests.get("https://poe.ninja/api/data/currencyoverview?league=Heist&type=Currency")
raw_data = resp.content
json_result = json.loads(raw_data)
for n in range(len(json_result)):
    print(json_result["lines"][n])

currentStats = dict()
for x in range(len(json_result)):
    this_card = json_result["lines"][x]['currencyTypeName']
    this_price = json_result["lines"][x]['chaosEquivalent']
    currentStats.update({this_card:this_price})

print(currentStats)