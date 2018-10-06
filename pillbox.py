#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Point
from enum import Enum

class Pillbox():
    def __init__(self):
        self.servoPublisher = rospy.Publisher("servo", Point, queue_size=10);
        self.servoStates = [ServoState.LOAD, ServoState.LOAD, ServoState.LOAD, ServoState.LOAD, ServoState.CLOSED, ServoState.CLOSED]
        self.initializeServos(self)
        
    def setServo(self, servoType, position):
        servoMessage = Point(servoNum, position)
        self.servoPublisher.publish(servoMessage)
        self.servoStates[servoType] = position

    def initializeServos(self):
        self.setServo(Servo.DRAWER1, ServoState.LOAD)
        self.setServo(Servo.DRAWER2, ServoState.LOAD)
        self.setServo(Servo.DRAWER3, ServoState.LOAD)
        self.setServo(Servo.DRAWER4, ServoState.LOAD)
        self.setServo(Servo.PILLIN, ServoState.CLOSED)
        self.setServo(Servo.PILLOUT, ServoState.CLOSED)

    def dispensePill(self, drawer):
        state = self.servoStates[drawer]
        if state == ServoState.LOAD:
            self.setServo(drawer, servoState.SLOT1)
        if state == ServoState.SLOT1:
            self.setServo(drawer, ServoState.SLOT2)
        elif state == ServoState.SLOT2:
            self.setServo(drawer, ServoState.SLOT3)
        elif state == ServoState.SLOT3:
            self.setServo(drawer, ServoState.SLOT4)
        self.setServo(Servo.PILLOUT, servoState.OPEN)

    def doneDispensePill(self):
        self.setServo(Servo.PILLOUT, servoState.CLOSED)

    def loadPill(self, drawer):
        self.setServo(drawer, servoState.LOAD)
        self.setServo(Servo.PILLIN, servoState.OPEN)

    def doneLoadPill(self):
        self.setServo(Servo.PILLIN, servoState.CLOSED)
        

class Servo(Enum):
    DRAWER1 = 0
    DRAWER2 = 1
    DRAWER3 = 2
    DRAWER4 = 3
    PILLIN = 4
    PILLOUT = 5

class ServoState(Enum):
    LOAD = -127
    SLOT1
    SLOT2
    SLOT3
    SLOT4
    OPEN
    CLOSED
