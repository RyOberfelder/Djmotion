import os
import serial
import time
tokenlength = 31
pastState = None
def child(pipeout):
  ser=serial.Serial(port='/dev/cu.usbmodem1421', baudrate=9600)
  bottles = 99
  count = 0
  out = ''
  while True:
      if ser.inWaiting() > 0:
          out += ser.read(1)
          count = count + 1
      if out != '' and count >=tokenlength: #and out[0]=='A':
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
            keyvalPairs = toKeyPair(verse)
            print keyvalPairs
            # compare presentState and Past state

            stateChange(keyvalPairs)

            # update past state
            pastState = keyvalPairs

def toKeyPair(rawInput):
    rawInput = sorted(rawInput.split(','))[1:]
    keyPairing = {}
    for Input in rawInput:
        keyPairing[str(Input[0])] = toDec(Input[1:])
    return keyPairing



def toDec(string):
    def getEquivlent(char):
        if char == 'a':
            return 10
        elif char == 'b':
            return 11
        elif char == 'c':
            return 12
        elif char =='d':
            return 13
        elif char =='e':
            return 14
        elif char =='f':
            return 15
        elif char <= '9' or char >= '0':
            return int(char)
        else:
            raise Error('WTF Mate?')
    if len(string) > 1:
        return getEquivlent(string[0])*16 + getEquivlent(string[1])
    else:
        return int(string)
def stateChange(keyValues):
    if(pastState==None):
        return
    if(keyValues['A'] != pastState['A'] ):
        #doA()
    if(keyValues['B'] != pastState['B'] ):
        #doB()
    if(keyValues['C'] != pastState['C'] ):
        #doC()
    if(keyValues['D'] != pastState['D'] ):
        #doD()
    if(keyValues['E'] != pastState['E'] ):
        #doE()
    if(keyValues['W'] != pastState['W'] ):
        #doW()
    if(keyValues['X'] != pastState['X'] ):
        #doX()
    if(keyValues['Y'] != pastState['Y'] ):
        #doY()
    if(keyValues['Z'] != pastState['Z'] ):
        #doZ()

parent()
