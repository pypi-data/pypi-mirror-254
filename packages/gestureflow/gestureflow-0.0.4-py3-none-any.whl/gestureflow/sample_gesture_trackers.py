from .definitions import *

class GestureTracker:
    def __init__(self) -> None:
        self.gestures = []
        self.trackRightHand = True
        self.trackLeftHand = True

        self.gestureFound = False
        self.stateTrackers = []

        self.resetState()

    def addGesture(self, gesture):
        self.gestures.append(gesture)

    def removeGesture(self, gesture):
        self.gestures.remove(gesture)

    def addStateTracker(self, stateTracker):
        self.stateTrackers.append(stateTracker)

    def setTrackRightHand(self, track):
        self.trackRightHand = track

    def setTrackLefttHand(self, track):
        self.trackLeftHand = track

    def updateState(self, handState):
        self.angleX = handState[ANGLE_X]
        self.angleY = handState[ANGLE_Y]
        self.angleZ = handState[ANGLE_Z]

        self.center = handState[COORD_LIST][9]
        self.fingerPoints = [handState[COORD_LIST][4], handState[COORD_LIST][8], handState[COORD_LIST][12], handState[COORD_LIST][16], handState[COORD_LIST][20]]

        self.centerLandmark = handState[LANDMARK_LIST][9]
        self.fingerLandmarks= [handState[LANDMARK_LIST][4], handState[LANDMARK_LIST][8], handState[LANDMARK_LIST][12], handState[LANDMARK_LIST][16], handState[LANDMARK_LIST][20]]

    def resetState(self):
        self.angleX = None
        self.angleY = None
        self.angleZ = None

        self.center = None
        self.fingerPoints = None

        self.centerLandmark = None
        self.fingerLandmarks = None

    def getState(self):
        return {
            GESTURE_FOUND: self.gestureFound,
            ANGLE_X: self.angleX,
            ANGLE_Y: self.angleY,
            ANGLE_Z: self.angleZ,
            HAND_CENTER: self.center, 
            FINGER_POINTS: self.fingerPoints,
        }

    def track(self, handStates):
        self.gestureFound = False
        for handState in handStates:
            if ((self.trackRightHand and handState[HAND_LABEL] == 'Right')) or ((self.trackLeftHand and handState[HAND_LABEL]== 'Left')):
                if handState[FINGERS_UP] in self.gestures:
                    self.gestureFound = True
                    self.updateState(handState)
                    break

        if not self.gestureFound:
            self.resetState()

        for stateTracker in self.stateTrackers:
            stateTracker.update(self.getState())


class GestureTracker2D(GestureTracker):
    def __init__(self) -> None:
        super().__init__()

    def getState(self):
        return {
            GESTURE_FOUND: self.gestureFound,
            ANGLE_Z: self.angleZ,
            HAND_CENTER: self.center, 
            FINGER_POINTS: self.fingerPoints,
        }



class GestureTracker3D(GestureTracker):
    def __init__(self) -> None:
        super().__init__()

    def getState(self):
        return {
            GESTURE_FOUND: self.gestureFound,

            ANGLE_X: self.angleX,
            ANGLE_Y: self.angleY,
            ANGLE_Z: self.angleZ,

            HAND_CENTER: self.centerLandmark, 
            FINGER_POINTS: self.fingerLandmarks,
        }
