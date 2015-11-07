import os, sys, inspect, thread, time


sys.path += ['C:/Users/Deven/Documents/Workspace/Djmotion/LeapSDK/lib', 'C:/Users/Deven/Documents/Workspace/Djmotion/LeapSDK/lib/x86']
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

def main():

    # Keep Process Running until it fails
    print u'Press Enter to quit...'
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
