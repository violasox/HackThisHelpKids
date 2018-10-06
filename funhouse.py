#!/usr/bin/env python3
from struct import pack
import serial

class PCB:
    def __init__(self, port = '/dev/ttyACM0'):
        self.usb = serial.Serial('/dev/ttyACM0', baudrate=9600)

    def set(self, port, value):
        print('set {} to {}'.format(port, value))
        cmd = pack('HBB', 1337, port, value)
        self.usb.write(bytes(cmd))
