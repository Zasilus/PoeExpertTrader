import requests
import json

class CurrencyModel:
    currencyStats = dict()
    def __init__(self):
        self.pullCurrency()
        print("Currency Pulled Collected")
        self.calculateROI()
        #print(self.currencyStats)

    def pullCurrency(self):
        #resp = requests.get("https://poe.ninja/api/data/currencyoverview?league=Heist&type=Currency")
        #raw_data = resp.content
        f = open("currencyoverview.json", "r")
        raw_data = f.read()
        f.close()
        json_result = json.loads(raw_data)
        for x in range(len(json_result["lines"])):
            this_currency = json_result["lines"][x]['currencyTypeName']
            this_price = json_result["lines"][x]['chaosEquivalent']
            if json_result["lines"][x]["pay"] == None:
                continue
            this_sell_price = 1 / json_result["lines"][x]["pay"]["value"]
            this_buy_price = json_result["lines"][x]["receive"]["value"]
            curr_dict = {"pay": this_sell_price, "receive":this_buy_price,"ChaosEquivalent":this_price}
            self.currencyStats.update({this_currency:curr_dict})
        chaos_dict = {"pay": 1, "receive": 1, "ChaosEquivalent": 1}
        self.currencyStats.update({"Chaos Orb": chaos_dict})

    def calculateExchangeDifference(self):
        for x in self.currencyStats:
            difference = self.currencyStats[x]['pay'] - self.currencyStats[x]['receive']
            self.currencyStats[x].update({"difference":difference})

    def calculateROI(self):
        self.calculateExchangeDifference()
        for x in self.currencyStats:
            difference = self.currencyStats[x]['difference']
            value = self.currencyStats[x]['ChaosEquivalent']
            roi = difference / value
            self.currencyStats[x].update({"ROI":roi})
        
    def getCurrencyData(self):
        return self.currencyStats
    
if __name__ == '__main__':
    model = CurrencyModel()