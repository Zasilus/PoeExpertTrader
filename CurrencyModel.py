import requests
import json


currencyStats = dict()
# resp = requests.get("https://poe.ninja/api/data/currencyoverview?league=Heist&type=Currency")
# raw_data = resp.content
# json_result = json.loads(raw_data)
#for n in range(len(json_result["lines"])):
    #print(json_result["lines"][n])


print(currencyStats)

def main():
    pullCurrency()
    print("Currency Pulled Collected")
    calculateROI()
    print(currencyStats)

def pullCurrency():
    global currencyStats
    #resp = requests.get("https://poe.ninja/api/data/currencyoverview?league=Heist&type=Currency")
    #raw_data = resp.content
    #raw_data = '{"lines":[{"currencyTypeName":"Mirror of Kalandra","pay":{"id":0,"league_id":86,"pay_currency_id":22,"get_currency_id":1,"sample_time_utc":"2020-10-22T18:43:01.6556515Z","count":64,"value":0.0000653268000000000000000000,"data_point_count":1,"includes_secondary":true},"receive":{"id":0,"league_id":86,"pay_currency_id":1,"get_currency_id":22,"sample_time_utc":"2020-10-22T18:43:01.6556515Z","count":75,"value":14634.622641509433962264150943,"data_point_count":1,"includes_secondary":true},"paySparkLine":{"data":[0.0,0.0,16.67,16.67,16.67,0.0,7.15],"totalChange":7.15},"receiveSparkLine":{"data":[0.0,0.39,4.86,8.96,8.13,-2.73,-3.66],"totalChange":-3.66},"chaosEquivalent":14944.51,"lowConfidencePaySparkLine":{"data":[0.0,0.0,16.67,16.67,16.67,0.0,7.15],"totalChange":7.15},"lowConfidenceReceiveSparkLine":{"data":[0.0,0.39,4.86,8.96,8.13,-2.73,-3.66],"totalChange":-3.66},"detailsId":"mirror-of-kalandra"}]}'    
    f = open("currencyoverview.json", "r")
    raw_data = f.read()
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