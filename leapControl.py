import os
import sys
import inspect
import thread
import time


sys.path += ['C:/Users/Deven/Documents/Workspace/Djmotion/LeapSDK/lib',
             'C:/Users/Deven/Documents/Workspace/Djmotion/LeapSDK/lib/x86']
import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture


class SimpleListener(Leap.Listener):

    def on_connect(self, controller):
        print "Leap Motion Connected!"
        print "Enabling Swipe Gesture"
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
        print "Enabling Circle Gestures"
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
        controller.config.set("Gesture.Swipe.MinLength", 20.0)
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
            self.onCircle(gesture)
        elif gesture.type == Leap.Gesture.TYPE_SWIPE:
            self.onSwipe(gesture)
        else:
            print 'Unknown Gesture Occured'

    # Method to be called when type is swipe
    def onSwipe(self, gesture):
        print 'Gesture Info: ' + str(gesture.frame)

    # Method to be called when type is circle
    def onCircle(self, gesture):
        print 'Circle Occured'


def main():

    listener = SimpleListener()
    controller = Leap.Controller()

    controller.add_listener(listener)
    # Keep Process Running until it fails
    print u'Press Enter to quit...'
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)

if __name__ == '__main__':
    main()
