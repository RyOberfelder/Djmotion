import serial
import time	
from threading import Thread
#ttyACM0 is the name of the arduino
ser=serial.Serial(port='/dev/cu.usbmodem1421', baudrate=9600)
while True:
    time.sleep(.01)
    out = ''
    while ser.inWaiting() > 0:
        out += ser.read(1)
    if out != '':
        print out
    


