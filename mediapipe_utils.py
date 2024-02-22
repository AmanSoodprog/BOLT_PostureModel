import mediapipe as mp
import numpy as np

import time

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)


def classify_posture(eye_landmarks, shoulder_landmarks):

    eye_distance = np.linalg.norm(eye_landmarks[0] - eye_landmarks[1])

    shoulder_distance = np.linalg.norm(shoulder_landmarks[0] - shoulder_landmarks[1])

    eye_shoulder_distance = np.linalg.norm(eye_landmarks[0] - shoulder_landmarks[0])

    perfect_threshold = shoulder_distance *1.2
    okay_threshold = shoulder_distance 

    if eye_shoulder_distance > okay_threshold and eye_shoulder_distance < perfect_threshold:
        return "Okay"
    elif eye_shoulder_distance <= okay_threshold:
        return "Bad"
    else:
        return "Perfect"

def classify_calmness(eye_landmarks, shoulder_landmarks):
  
    eye_distance = np.linalg.norm(eye_landmarks[0] - eye_landmarks[1])
    shoulder_distance = np.linalg.norm(shoulder_landmarks[0] - shoulder_landmarks[1])
    eye_shoulder_distance = np.linalg.norm(eye_landmarks[0] - shoulder_landmarks[0])

   
    return eye_shoulder_distance

    # Classify the calmness based on the distances
    # if eye_shoulder_distance <= still_threshold:
    #     return "Calm"
    # elif eye_shoulder_distance <= normal_threshold:
    #     return "Normal"
    # else:
    #     return "Agitated"


# def classify_calmness(eye_landmarks, shoulder_landmarks):
#     # Calculate the distance between the eyes
#     eye_distance = np.linalg.norm(eye_landmarks[0] - eye_landmarks[1])

#     # Calculate the distance between the shoulders
#     shoulder_distance = np.linalg.norm(shoulder_landmarks[0] - shoulder_landmarks[1])

#     # Calculate the distance between the eyes and the shoulders
#     eye_shoulder_distance = np.linalg.norm(eye_landmarks[0] - shoulder_landmarks[0])

#     # Define the thresholds for calmness classification
#     calm_threshold = 0.1

#     # Store the initial distances
#     initial_eye_shoulder_distance = eye_shoulder_distance
#     initial_shoulder_distance = shoulder_distance

#     # Wait for 1 second
#   

#     # Recalculate the distances after 1 second
#     eye_distance = np.linalg.norm(eye_landmarks[0] - eye_landmarks[1])
#     shoulder_distance = np.linalg.norm(shoulder_landmarks[0] - shoulder_landmarks[1])
#     eye_shoulder_distance = np.linalg.norm(eye_landmarks[0] - shoulder_landmarks[0])

#     # Calculate the relative change in distances
#     relative_change_eye_shoulder = abs(eye_shoulder_distance - initial_eye_shoulder_distance)
#     relative_change_shoulder = abs(shoulder_distance - initial_shoulder_distance)
#     print(relative_change_eye_shoulder)
#     # Classify the calmness based on the relative change in distances
#     if relative_change_eye_shoulder <= calm_threshold and relative_change_shoulder <= calm_threshold:
#         return "Calm"
#     else:
#         return "Agitated"
