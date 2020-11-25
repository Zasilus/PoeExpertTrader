import sched, time
import threading
import json

from flask import Flask
from flask import render_template
from Controller import Controller

app = Flask(__name__)
controller = None
# s = sched.scheduler(time.time, time.sleep)

def main():
    global controller
    print("Entering Main method")
    controller = Controller()
    print(controller.controllerCStats)
    x = threading.Thread(target=threadUpdateData)
    x.daemon = True
    x.start()
    app.run(debug=True)

def threadUpdateData():
    while True:
        #time.sleep(5)
        updateData()
        time.sleep(500)

def updateData():
    print("Updating Data")
    global controller
    controller.cModel.pullCurrency()
    controller.cModel.calculateROI()
    controller.dModel.pullDivination()
    controller.dModel.calculateROI()

@app.route("/")
def home():
    global controller
    print(controller.cModel.getCurrencyData())
    return controller.cModel.getCurrencyData()

@app.route("/")
@app.route("/currency")
def Currency():
    global controller
    cStats = controller.controllerCStats
    json_object = json.dumps(cStats, indent = 4)
    print(cStats)
    return render_template('view_currency.html', title = "Currency", cStats = json_object)

if __name__ == '__main__':
    main()