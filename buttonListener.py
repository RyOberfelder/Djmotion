import os
import serial
import time
tokenlength = 30
def child(pipeout):
  ser=serial.Serial(port='/dev/cu.usbmodem1421', baudrate=9600)
  bottles = 99
  count = 0
  out = ''
  while True:
      if ser.inWaiting() > 0:
          out += ser.read(1)
          count = count + 1
      if out != '' and count >=tokenlength:
          os.write(pipeout, out)
          count = 0
          out = ''

def parent():
    pipein, pipeout = os.pipe()
    if os.fork() == 0:
        child(pipeout)
    else:
        counter = 1
        while True:
            verse = os.read(pipein, 117)
            print verse

parent()
