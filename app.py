from flask import Flask, render_template, request
import cv2
import numpy as np
import pymongo
import mediapipe_utils as mp_utils
from landmarks import draw_landmarks
import time

host = "mongodb+srv://Pixel:Pixel7788@cluster0.3dpfxx3.mongodb.net/mydb?retryWrites=true&w=majority"
client = pymongo.MongoClient(host)
db = client['Posture_Data']

application = Flask(__name__)

cap = cv2.VideoCapture(0)

@application.route('/')
def index():
    return render_template('index.html')


@application.route('/posture', methods=['POST'])
def posture():
    ret, frame = cap.read()

    if not ret:
        return "Error reading frame"
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = mp_utils.pose.process(frame_rgb)

    frame_with_landmarks, eye_landmarks, shoulder_landmarks = draw_landmarks(frame, results)

    if eye_landmarks is not None and shoulder_landmarks is not None:
   
        posture = mp_utils.classify_posture(eye_landmarks, shoulder_landmarks)
        
        calmness1=mp_utils.classify_calmness(eye_landmarks, shoulder_landmarks)
        time.sleep(2)
        ret, frame = cap.read()
        if not ret:
            return "Error reading frame"
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
 
        results = mp_utils.pose.process(frame_rgb)
        frame_with_landmarks, eye_landmarks, shoulder_landmarks = draw_landmarks(frame, results)
        if eye_landmarks is not None and shoulder_landmarks is not None:
            calmness2=mp_utils.classify_calmness(eye_landmarks, shoulder_landmarks)
            if(abs(calmness1-calmness2)>0.1):
                calmness="Agitated"
            else:
                calmness="Calm"
            print(posture)
            print(calmness)
            return posture
        else:
            return "Error reading frame"
        
     

    return "No posture detected"

if __name__ == '__main__':
    application.run(debug=True, port=5050)
