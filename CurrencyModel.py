import requests
import json

currencyStats = dict()

def main():
    pullCurrency()
    print("Currency Pulled Collected")
    calculateROI()
    print(currencyStats)

def pullCurrency():
    global currencyStats
    #resp = requests.get("https://poe.ninja/api/data/currencyoverview?league=Heist&type=Currency")
    #raw_data = resp.content
    f = open("currencyoverview.json", "r")
    raw_data = f.read()
    f.close();
    json_result = json.loads(raw_data)
    for x in range(len(json_result["lines"])):
        this_currency = json_result["lines"][x]['currencyTypeName']
        this_price = json_result["lines"][x]['chaosEquivalent']
        if json_result["lines"][x]["pay"] == None:
            continue
        this_sell_price = 1 / json_result["lines"][x]["pay"]["value"]
        this_buy_price = json_result["lines"][x]["receive"]["value"]
        curr_dict = {"pay": this_sell_price, "receive":this_buy_price,"ChaosEquivalent":this_price}
        currencyStats.update({this_currency:curr_dict})

def calculateExchangeDifference():
    print("Calculating exchange differences")
    global currencyStats
    for x in currencyStats:
        difference = currencyStats[x]['pay'] - currencyStats[x]['receive']
        currencyStats[x].update({"difference":difference})

def calculateROI():
    print("Calculating ROI")
    calculateExchangeDifference()
    global currencyStats
    for x in currencyStats:
        difference = currencyStats[x]['difference']
        value = currencyStats[x]['ChaosEquivalent']
        roi = difference / value
        currencyStats[x].update({"ROI":roi})
        
def getCurrencyData():
    global currencyStats
    return currencyStats
    
if __name__ == '__main__':
    main()