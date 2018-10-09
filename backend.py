#!/usr/bin/env python3
from pillbox import Pillbox, Servo
from flask import Flask, redirect

# A Flask app so that the UI can call box functionality at the appropriate times
# Check pillbox.py for function descriptions
app = Flask(__name__)
box = Pillbox()

@app.route('/dispense/<id>')
def dispense(id):
    print('route')
    drawer = checkDrawer(int(id))
    print(drawer)
    box.dispensePill(drawer)
    return ""

@app.route('/load/<id>')
def load(id):
    drawer = checkDrawer(int(id))
    box.loadPill(drawer)
    return ""

@app.route('/unlock')
def unlock():
    box.unlock()
    return ""

@app.route('/lock')
def lock():
    box.lock()
    return ""

@app.route('/lightsOff')
def lights():
    box.lightsOff()
    return ""

@app.route('/')
def index():
    return redirect('/static/index.html')

def checkDrawer(id):
    if id == 0:
        drawer = Servo.DRAWER1
    elif id == 1:
        drawer = Servo.DRAWER2
    elif id == 2:
        drawer = Servo.DRAWER3
    else:
        drawer = Servo.DRAWER4

    return drawer

app.run()
