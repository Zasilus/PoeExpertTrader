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