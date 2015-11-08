import soundy
import sys
sys.path += ['C:/Users/Deven/Documents/Workspace/Djmotion/LeapSDK/lib',
             'C:/Users/Deven/Documents/Workspace/Djmotion/LeapSDK/lib/x86']
import Leap

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

if __name__ == '__main__':
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
