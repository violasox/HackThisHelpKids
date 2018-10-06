from pillbox import Pillbox, Servo
from flask import Flask

app = Flask(__name__)

box = Pillbox()

@app.route('/dispense/:id')
def dispense(id):
    drawer = checkDrawer(id)
    box.dispensePill(drawer)

@app.route('/load/:id')
def load(id):
    drawer = checkDrawer(id)
    box.loadPill(drawer)

@app.route('/unlock')
def unlock():
    box.unlock()

@app.route('/lock')
def lock():
    box.lock()
    
def checkDrawer(id):
    if id == 0:
        drawer = Servo.DRAWER1
    elif id == 1:
        drawer = Servo.DRAWER2
    elif id == 2:
        drawer = Servo.DRAWER3
    else
        drawer = Servo.DRAWER4
    
    return drawer    
