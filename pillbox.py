#!/usr/bin/env python3
import funhouse
from enum import Enum

# Interface for the physical functionality of the box
class Pillbox():
    def __init__(self):
        self.pcb = funhouse.PCB()
        self.ServoStates = [ServoState.LOAD, ServoState.LOAD, ServoState.LOAD, ServoState.LOAD, ServoState.CLOSED, ServoState.CLOSED]
        self.initializeServos()

    # Set the specified servo to the specified location using provided Enums
    def setServo(self, servoType, position):
        self.ServoStates[servoType.value] = position
        self.pcb.set(servoType.value, position.value)

    # Initialize all servos to their starting positions
    def initializeServos(self):
        self.setServo(Servo.DRAWER1, ServoState.LOAD)
        self.setServo(Servo.DRAWER2, ServoState.LOAD)
        self.setServo(Servo.DRAWER3, ServoState.LOAD)
        self.setServo(Servo.DRAWER4, ServoState.LOAD)
        self.setServo(Servo.PILLIN, ServoState.CLOSED)
        # Fun fact, LEDs are really just a type of servo
        self.setServo(Servo.LED, ServoState.CLOSED)

    # Dispense a pill from the specified drawer by rotating the turnstile
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

    # Lock the parent door with the servo
    def lock(self):
        self.setServo(Servo.PILLIN, ServoState.CLOSED)

    # Unlock the parent door with the servo
    def unlock(self):
        self.setServo(Servo.PILLIN, ServoState.OPEN)

    # Rotate turnstile to starting position so pills can be loaded
    def loadPill(self, drawer):
        self.setServo(drawer, ServoState.LOAD)

    # Turn the LEDs off (separate function so there can be a delay without blocking)
    def lightsOff(self):
        self.setServo(Servo.LED, ServoState.CLOSED)

# Enum to keep track of the different servo motors, + an LED
class Servo(Enum):
    DRAWER1 = 0
    DRAWER2 = 1
    DRAWER3 = 2
    DRAWER4 = 3
    PILLIN = 4
    LED = 5

# Enum to simplify servo positions
# Might have to adjust if servos aren't identical
class ServoState(Enum):
    LOAD = 180
    SLOT1 = 135
    SLOT2 = 90
    SLOT3 = 45
    SLOT4 = 0
    OPEN = 180
    CLOSED = 0
