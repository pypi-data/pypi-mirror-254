import mediapipe as mp
import numpy as np
from .definitions import *
import cv2


GestureRecognizer = mp.tasks.vision.GestureRecognizer

def dist(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5


def getPalmOpenRatio(landMarks):
    palmOpenRatios = []
    midIndices = [3, 6, 10, 14, 18]
    topIndices = [4, 8, 12, 16, 20]
    for midIndex, topIndex in zip(midIndices, topIndices):
        topVec = np.array(landMarks[topIndex]) - np.array(landMarks[0])
        midVec = np.array(landMarks[topIndex]) - np.array(landMarks[midIndex])
        topVec = topVec / np.linalg.norm(topVec)
        midVec = midVec / np.linalg.norm(midVec)
        palmOpenRatios.append(np.dot(topVec, midVec))
    return palmOpenRatios

def getFingersUp(landMarks):
    fingersUp = []
    minThresholds = [.9 , .5, .5, .5, .5]
    maxThresholds = [1  , 1, 1, 1, 1]
    openRatios = getPalmOpenRatio(landMarks)
    for mn, mx, ratio in zip(minThresholds, maxThresholds, openRatios):
        if (mn <= ratio) and (ratio <= mx):
            fingersUp.append(True)
        else:
            fingersUp.append(False)
    return fingersUp

def getOrientation(vector):
    # Extracting individual components
    x, y, z = vector

    # Calculate roll (rotation around x-axis)
    roll = np.arctan2(y, z)

    # Calculate pitch (rotation around y-axis)
    pitch = np.arctan2(-x, np.sqrt(y**2 + z**2))

    # Calculate yaw (rotation around z-axis)
    yaw = np.arctan2(np.sin(roll)*z - np.cos(roll)*y, np.cos(roll)*x - np.sin(roll)*y)

    # Convert angles from radians to degrees
    roll = np.degrees(roll)
    pitch = np.degrees(pitch)
    yaw = np.degrees(yaw)

    return roll, pitch, yaw


def getOrientation2(vector1, vector2):
    # Normalize vectors
    vector1 = vector1 / np.linalg.norm(vector1)
    vector2 = vector2 / np.linalg.norm(vector2)

    # Calculate the normal vector of the plane using the cross product
    normal_vector = np.cross(vector1, vector2)
    normal_vector = normal_vector / np.linalg.norm(normal_vector)

    # Calculate yaw (rotation around z-axis)
    yaw = np.degrees(np.arctan2(normal_vector[1], normal_vector[0]))

    # Calculate pitch (rotation around y-axis)
    pitch = np.degrees(np.arctan2(-normal_vector[2], np.sqrt(normal_vector[0]**2 + normal_vector[1]**2)))

    # Calculate roll (rotation around x-axis)
    vector = (vector1 + vector2) / 2
    roll = np.degrees(np.arctan2(vector[1], vector[0]))

    return roll, pitch, yaw


class HandTracker:
    def __init__(self):
        # initialize mediapipe hands module
        self.mp_hands = mp.solutions.hands
        self.hands = mp.solutions.hands.Hands()
        self.gestures = []
        self.visualize = False

    def setVisualize(self, visualize):
        self.visualize = visualize

    def run(self, frame):
        results = self.hands.process(frame)

        handStates = []

        # Check if hand landmarks are detected
        if results.multi_hand_landmarks:
            for idx, handLandmarks in enumerate(results.multi_hand_landmarks):
                landMarkList = []
                coordList = []
                for landMark in handLandmarks.landmark:
                    height,width,_ = frame.shape
                    coorx, coory, coorz = landMark.x, landMark.y, landMark.z
                    landMarkList.append((coorx, coory, coorz))
                    coorx, coory = int(coorx * width), int(coory * height)
                    coordList.append((coorx, coory))

                landMarkList = [np.array(v) for v in landMarkList]


                label = results.multi_handedness[idx].classification[0].label
                fingersUp = getFingersUp(landMarkList)
                
                roll, _, _ = getOrientation(landMarkList[9] - landMarkList[0])
                _, pitch, yaw = getOrientation2(landMarkList[5] - landMarkList[0], landMarkList[17] - landMarkList[0])

                state = {
                    HAND_LABEL: label,
                    FINGERS_UP: fingersUp,
                    LANDMARK_LIST: landMarkList,
                    COORD_LIST: coordList,
                    ROLL: roll,
                    PITCH: pitch,
                    YAW: yaw,
                }

                if self.visualize:
                    x = 10
                    y = 20
                    for key, val in state.items():
                        cv2.putText(frame, f"{key}: {val}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
                        y += 20

                handStates.append(state)

        for gesture in self.gestures:
            gesture.track(handStates)

    def add_gesture(self, gestureTracker):
        self.gestures.append(gestureTracker)


if __name__ == "__main__":

    import cv2
    from sample_gesture_trackers import DiscGestureTracker
    from sample_state_trackers import DiscValueTracker
    tracker = HandTracker()
    gest = DiscGestureTracker()
    valueTracker = DiscValueTracker(gest)
    tracker.add_gesture(gest)
    tracker.add_state(valueTracker)

    cap = cv2.VideoCapture(0)  # Use 0 for default camera, or specify the camera index
    while cap.isOpened():
        # Read a frame from the live stream
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the image 
        frame = cv2.flip(frame, 1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        tracker.run(frame)
        print(valueTracker.getState())


        cv2.imshow("Tracker", frame)

        if cv2.waitKey(1) and 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()




