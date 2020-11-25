from app import app
import Controller

@app.route("/")
@app.route("/currency")
def currency():
    ctrl = Controller()
    ctrl.getCurrencyData()
