#!/usr/bin/env python3
from struct import pack
import serial

class PCB:
    def __init__(self, port: str = '/dev/ttyACM0') -> None:
        self.usb = serial.Serial('/dev/ttyACM0', baudrate=9600)

    def set(self, port: int, value: int) -> None:
        cmd = pack('Hbb', 1337, 0, 60)
        self.usb.write(bytes(cmd))
