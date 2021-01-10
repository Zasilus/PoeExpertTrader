import sched, time
import threading
import json

from flask import Flask
from flask import render_template
from flask import request
from Controller import Controller

app = Flask(__name__)
controller = None
# s = sched.scheduler(time.time, time.sleep)

def main():
    global controller
    print("Entering Main method")
    controller = Controller()
    x = threading.Thread(target=threadUpdateData)
    x.daemon = True
    x.start()
    app.run(debug=True)

def threadUpdateData():
    while True:
        #time.sleep(5)
        updateData()
        time.sleep(3000)

def updateData():
    print("Updating Data")
    global controller
    controller.cModel.pullCurrency()
    controller.cModel.calculateROI()
    controller.dModel.pullDivination()
    controller.dModel.calculateROI()

@app.route("/")
def home():
    return render_template('view_home.html', title = "homepage")

@app.route("/")
@app.route("/optimalcurrency", methods=["GET", "POST"])
def getOptimalCurrency():
    global controller
    if request.method == "POST":
        req = request.form
        amt = controller.calculateCurrencyOptimal(int(req['cinput']))
        return amt
    else:
        return ""


@app.route("/")
@app.route("/homepage")
def homepage():
    return render_template('view_home.html', title = "homepage")

@app.route("/")
@app.route("/currency")
def Currency():
    global controller
    cStats = controller.controllerCStats
    json_object = json.dumps(cStats, indent = 4)
    return render_template('view_currency.html', title = "Currency", cStats = cStats)

@app.route("/")
@app.route("/divination")
def Divination():
    global controller
    dStats = controller.controllerDStats
    json_object = json.dumps(dStats, indent = 4)
    return render_template('view_divination.html', title = "Divination", dStats = dStats)

if __name__ == '__main__':
    main()