#!/usr/bin/env python3
import funhouse
from enum import Enum

class Pillbox():
    def __init__(self):
        self.pcb = funhouse.PCB()
        self.ServoStates = [ServoState.LOAD, ServoState.LOAD, ServoState.LOAD, ServoState.LOAD, ServoState.CLOSED, ServoState.CLOSED]
        self.initializeServos()

    def setServo(self, servoType, position):
        self.ServoStates[servoType.value] = position
        self.pcb.set(servoType.value, position.value)

    def initializeServos(self):
        self.setServo(Servo.DRAWER1, ServoState.LOAD)
        self.setServo(Servo.DRAWER2, ServoState.LOAD)
        self.setServo(Servo.DRAWER3, ServoState.LOAD)
        self.setServo(Servo.DRAWER4, ServoState.LOAD)
        self.setServo(Servo.PILLIN, ServoState.CLOSED)
        self.setServo(Servo.LED, ServoState.CLOSED)

    def dispensePill(self, drawer):
        state = self.ServoStates[drawer.value]
        print(state)
        self.setServo(Servo.LED, ServoState.OPEN)
        if state == ServoState.LOAD:
            self.setServo(drawer, ServoState.SLOT1)
        if state == ServoState.SLOT1:
            self.setServo(drawer, ServoState.SLOT2)
        elif state == ServoState.SLOT2:
            self.setServo(drawer, ServoState.SLOT3)
        elif state == ServoState.SLOT3:
            self.setServo(drawer, ServoState.SLOT4)

    def lock(self):
        self.setServo(Servo.PILLIN, ServoState.CLOSED)

    def unlock(self):
        self.setServo(Servo.PILLIN, ServoState.OPEN)

    def loadPill(self, drawer):
        self.setServo(drawer, ServoState.LOAD)

    def lightsOff(self):
        self.setServo(Servo.LED, ServoState.CLOSED)

class Servo(Enum):
    DRAWER1 = 0
    DRAWER2 = 1
    DRAWER3 = 2
    DRAWER4 = 3
    PILLIN = 4
    LED = 5

class ServoState(Enum):
    LOAD = 180
    SLOT1 = 110
    SLOT2 = 100
    SLOT3 = 80
    SLOT4 = 0
    OPEN = 180
    CLOSED = 0
