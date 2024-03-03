import cv2
import numpy as np
import mediapipe_utils as mp_utils

def draw_landmarks(frame, results):
 
    if results.pose_landmarks:
        mp_utils.mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_utils.mp_pose.POSE_CONNECTIONS)

      
        left_eye_landmark = results.pose_landmarks.landmark[mp_utils.mp_pose.PoseLandmark.LEFT_EYE]
        right_eye_landmark = results.pose_landmarks.landmark[mp_utils.mp_pose.PoseLandmark.RIGHT_EYE]
        left_shoulder_landmark = results.pose_landmarks.landmark[mp_utils.mp_pose.PoseLandmark.LEFT_SHOULDER]
        right_shoulder_landmark = results.pose_landmarks.landmark[mp_utils.mp_pose.PoseLandmark.RIGHT_SHOULDER]

        eye_landmarks = np.array([[left_eye_landmark.x, left_eye_landmark.y],
                                  [right_eye_landmark.x, right_eye_landmark.y]])
        shoulder_landmarks = np.array([[left_shoulder_landmark.x, left_shoulder_landmark.y],
                                       [right_shoulder_landmark.x, right_shoulder_landmark.y]])

        return frame, eye_landmarks, shoulder_landmarks

    return frame, None, None
