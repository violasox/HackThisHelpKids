import funhouse
import time

pcb = funhouse.PCB()

testid = 5

pcb.set(testid, 0)
time.sleep(1)
pcb.set(testid, 90)
time.sleep(1)
pcb.set(testid, 180)
