from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import pymongo
from flask_cors import CORS
import mediapipe_utils as mp_utils
from landmarks import draw_landmarks
import time

import base64

host = "mongodb+srv://Pixel:Pixel7788@cluster0.3dpfxx3.mongodb.net/mydb?retryWrites=true&w=majority"
client = pymongo.MongoClient(host)
db = client['Posture_Data']

app = Flask(__name__)




CORS(app)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posture', methods=['POST'])
def posture():
    # Get the image data from the request
    image_data = request.form['image']
    
    # Decode the base64 image
    image_data = base64.b64decode(image_data.split(',')[1])
    
    # Convert the image data to a numpy array
    nparr = np.frombuffer(image_data, np.uint8)
    
    # Decode the image
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if frame is None:
        return "Error reading frame"
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = mp_utils.pose.process(frame_rgb)

    frame_with_landmarks, eye_landmarks, shoulder_landmarks = draw_landmarks(frame, results)

    if eye_landmarks is not None and shoulder_landmarks is not None:
   
        posture = mp_utils.classify_posture(eye_landmarks, shoulder_landmarks)
        
        # calmness1=mp_utils.classify_calmness(eye_landmarks, shoulder_landmarks)
        # frame = frame_rgb
    
        # # frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
 
        # results = mp_utils.pose.process(frame_rgb)
        # frame_with_landmarks, eye_landmarks, shoulder_landmarks = draw_landmarks(frame, results)
        # print(eye_landmarks, shoulder_landmarks)
        # if eye_landmarks is not None and shoulder_landmarks is not None:
        #     calmness2=mp_utils.classify_calmness(eye_landmarks, shoulder_landmarks)
        #     if(abs(calmness1-calmness2)>0.1):
        #         calmness="Agitated"
        #     else:
        #         calmness="Calm"
        #     print(posture)
        #     print(calmness)
        #     return posture
        print(posture)
        return jsonify({'posture': posture})
    else:
        return "Error reading frame"  
    return "No posture detected"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

