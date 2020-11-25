import sched, time
import threading

from flask import Flask
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
        time.sleep(5)
        updateData()

def updateData():
    print("Updating Data")
    global controller
    controller.cModel.pullCurrency()
    controller.dModel.pullDivination()

@app.route("/")
def home():
    global controller
    return controller.controllerCStats

if __name__ == '__main__':
    main()