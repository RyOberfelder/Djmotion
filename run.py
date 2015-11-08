import soundy
print 'imported soundy'
import sys
print 'imported sys'
sys.path += ['/Users/ryanoberfelder/Programming/Projects/Djmotion/LeapSDK/lib',]
print 'sys path added'
import Leap
print 'imported leap'
import os
print 'imported os'
import serial
print 'imported serial super cereal'
import time
print 'imported time'

class SimpleListener(Leap.Listener):

    def on_connect(self, controller):
        self.previousFrame = {'gesture': None, 'frame': None}
        self.distortTimer = 0
        self.MAX_INTERVAL = 10
        print "Leap Motion Connected!"
        print "Enabling Swipe Gesture"
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
        print "Enabling Circle Gestures"
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
        controller.config.set("Gesture.Swipe.MinLength", 160.0)
        controller.config.save()

    def on_disconnect(self, controller):
        print "Leap Motion Disconnected!"

    def on_frame(self, controller):
        frame = controller.frame()
        gestureList = frame.gestures()
        if frame.gestures().is_empty:
            return
        for gesture in gestureList:
            self.getGesture(gesture)

    def getGesture(self, gesture):
        if gesture.type == Leap.Gesture.TYPE_CIRCLE:
            self.onCircle(gesture, self.decreaseTime())
        elif gesture.type == Leap.Gesture.TYPE_SWIPE:
            self.onSwipe(gesture)
        else:
            print 'Unknown Gesture Occured'

    # Method to be called when type is swipe
    def onSwipe(self, gesture):
        # print 'Gesture Info: ' + str(gesture.frame)
        if self.previousFrame['frame'] is not None:
            translation = gesture.frame.translation(
                self.previousFrame['frame'])
            translation_probability = gesture.frame.translation_probability(
                self.previousFrame['frame'])
            if translation_probability > 0.9:
                self.determineSwipe(translation)
        self.previousFrame = {'gesture': 'swipe', 'frame': gesture.frame}

    def decreaseTime(self):
        self.distortTimer -= 1
        return

    def determineSwipe(self, translate):
        x = translate[0]
        y = translate[1]
        z = translate[2]
        if abs(x) > abs(y) and abs(x) > abs(z):
            if x > 0:
                self.onSwipeRight(x, self.decreaseTime())
            elif x < 0:
                self.onSwipeLeft(x, self.decreaseTime())
        elif abs(y) > abs(x) and abs(y) > abs(z):
            if y > 0:
                self.onRise(y, self.decreaseTime())
            elif y < 0:
                self.onLower(y, self.decreaseTime())
        elif abs(z) > abs(x) and abs(z) > abs(y):
            if z > 0:
                self.onBackSwipe(z, self.decreaseTime())
            elif z < 0:
                self.onForwardSwipe(z, self.decreaseTime())
        else:
            return

    def onSwipeRight(self, magnitude, callback):
        if self.distortTimer >= 0:
            return
        magnitude = abs(magnitude)
        self.distortTimer = self.MAX_INTERVAL
        print 'Swipe Right'

    def onSwipeLeft(self, magnitude, callback):
        if self.distortTimer >= 0:
            return
        magnitude = abs(magnitude)
        soundy.scratchback(magnitude)
        self.distortTimer = self.MAX_INTERVAL
        print 'Swipe Left'

    def onRise(self, magnitude, callback):
        if self.distortTimer >= 0:
            return
        magnitude = abs(magnitude)
        self.distortTimer = self.MAX_INTERVAL
        print 'Swipe Up'

    def onLower(self, magnitude, callback):
        if self.distortTimer >= 0:
            return
        magnitude = abs(magnitude)
        self.distortTimer = self.MAX_INTERVAL
        print 'Swipe Down'

    def onBackSwipe(self, magnitude, callback):
        if self.distortTimer >= 0:
            return
        magnitude = abs(magnitude)
        self.distortTimer = self.MAX_INTERVAL
        print 'Swipe Back'

    def onForwardSwipe(self, magnitude, callback):
        if self.distortTimer >= 0:
            return
        self.distortTimer = self.MAX_INTERVAL
        magnitude = abs(magnitude)
        print 'Swipe Forward'

    # Method to be called when type is circle
    def onCircle(self, gesture, callback):
        # print 'Gesture Info: ' + str(gesture.frame)
        if self.distortTimer != 0:
            return
        if self.previousFrame['frame'] is not None:
            translation_probability = gesture.frame.translation_probability(
                self.previousFrame['frame'])
            if translation_probability > 0.9:
                print 'Cricle Gesture'
                # Code on Circle To be Done Here...
                #
                #
                #

        self.distortTimer = self.MAX_INTERVAL
        self.previousFrame = {'gesture': 'circle', 'frame': gesture.frame}


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
        soundy.robot()
    if(keyValues['B'] != pastState['B'] ):
        pass
        #doB()
    if(keyValues['C'] != pastState['C'] ):
        pass
        #doC()
    if(keyValues['D'] != pastState['D'] ):
        pass
        #doD()
    if(keyValues['E'] != pastState['E'] ):
        pass
        #doE()
    if(keyValues['W'] != pastState['W'] ):
        pass
        #doW()
    if(keyValues['X'] != pastState['X'] ):
        pass
        #doX()
    if(keyValues['Y'] != pastState['Y'] ):
        pass
        #doY()
    if(keyValues['Z'] != pastState['Z'] ):
        pass
        #doZ()


if __name__ == '__main__':
    listener = SimpleListener()
    controller = Leap.Controller()

    controller.add_listener(listener)
    # Keep Process Running until it fails

    parent()
