import numpy as np
from .definitions import *

class StateTracker:
    def __init__(self) -> None:
        self.on_update = None

    def setOnUpdate(self, on_update):
        self.on_update = on_update

    def update(self):
        print("Doing nothing ...")


class RotationCounter(StateTracker):
    def __init__(self) -> None:
        super().__init__()
        self.currentValue = 0
        self.delta = 0
        self.minValue = 0
        self.maxValue = 100
        self.discUnit = 10
        self.initialAngle = None

    def setMin(self, minValue):
        self.minValue = minValue

    def setMax(self, maxValue):
        self.maxValue = maxValue

    def setDiscUnit(self, discUnit):
        self.discUnit = discUnit

    def getState(self):
        return (self.currentValue + self.delta)

    def update(self, state):
        found, angle = state[GESTURE_FOUND], state[ANGLE_Z]
        if found:
            if not self.initialAngle:
                self.initialAngle = angle

            diffAngle = (angle - self.initialAngle + 360) % 360
            if diffAngle > 180:
                diffAngle -= 360
            self.delta = min(self.maxValue - self.currentValue, max(self.minValue - self.currentValue, diffAngle // self.discUnit)) 
            if self.on_update:
                self.on_update(self.getState())

        elif self.initialAngle:
            self.initialAngle = None
            self.currentValue += self.delta
            self.delta = 0



class DisplacementTracker(StateTracker):
    def __init__(self) -> None:
        super().__init__()
        self.isPrevPosition = False
        self.prevPosition = None
        self.displacement = None
        self.currentDisplacement = None
        self.isDisplaced = False

    def getState(self):
        if self.isDisplaced:
            return tuple(self.displacement)
        return self.displacement


    def update(self, state):
        currentPosition = None
        if state[GESTURE_FOUND]:
            currentPosition = np.array(state[FINGER_POINTS] + [state[HAND_CENTER]])
            if self.isPrevPosition:
                if self.isDisplaced:
                    self.displacement += currentPosition - self.prevPosition
                else:
                    self.isDisplaced = True
                    self.displacement = currentPosition - self.prevPosition
            self.isPrevPosition = True
            if self.on_update:
                self.on_update(self.getState())
        else:
            self.isPrevPosition = False

        self.prevPosition = currentPosition


class PositionTracker(StateTracker):
    def __init__(self) -> None:
        super().__init__()
        self.position = None
        self.isPosition = False

    def getState(self):
        if self.isPosition:
            return tuple(self.position)
        return self.position


    def update(self, state):
        if state[GESTURE_FOUND]:
            self.position = np.array(state[FINGER_POINTS] + [state[HAND_CENTER]])
            self.isPosition = True
            if self.on_update:
                self.on_update(self.getState())
        else:
            self.position = None
            self.isPosition = False

class IndexPointerTracker(StateTracker):
    def __init__(self) -> None:
        super().__init__()
        self.point = None

    def getState(self):
        return self.point

    def update(self, state):
        if state[GESTURE_FOUND]:
            self.point = state[FINGER_POINTS][1]
            if self.on_update:
                self.on_update(self.getState())
        else:
            self.point = None


