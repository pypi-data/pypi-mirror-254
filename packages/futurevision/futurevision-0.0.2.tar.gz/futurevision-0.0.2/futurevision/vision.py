"""

futurevision/vision.py
   _____                _           _   _                      _ _   ______    _ _
  / ____|              | |         | | | |               /\   | (_) |  ____|  | (_)
 | |     _ __ ___  __ _| |_ ___  __| | | |__  _   _     /  \  | |_  | |__   __| |_ ___
 | |    | '__/ _ \/ _` | __/ _ \/ _` | | '_ \| | | |   / /\ \ | | | |  __| / _` | / __|
 | |____| | |  __/ (_| | ||  __/ (_| | | |_) | |_| |  / ____ \| | | | |___| (_| | \__ \
  \_____|_|  \___|\__,_|\__\___|\__,_| |_.__/ \__, | /_/    \_\_|_| |______\__,_|_|___/
                                               __/ |
                                              |___/

"""
from sys import addaudithook
import time
from cv2 import VideoCapture, flip, cvtColor, COLOR_BGR2RGB, imshow, waitKey, putText, FONT_HERSHEY_SIMPLEX, LINE_AA,circle,COLOR_BGR2HSV,COLOR_BGR2GRAY, line,rectangle,COLOR_RGB2BGR,dnn,resize,HOUGH_GRADIENT,bilateralFilter,HoughCircles,Canny,imread,FONT_HERSHEY_DUPLEX,FILLED

import mediapipe as mp
import numpy as np 
import time 
import dlib
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from scipy.spatial import distance
import pyautogui
import pyaudio
import math 
import struct
from gtts import gTTS
from pygame import mixer

class Vision:
    def __init__(self):
        self.colors = {
            'red': (0, 0, 255),
            'green': (0, 255, 0),
            'blue': (255, 0, 0),
            'yellow': (0, 255, 255),
            'purple': (128, 0, 128),
            'orange': (0, 165, 255),
            'pink': (203, 192, 255),
            'cyan': (255, 255, 0),
            'brown': (42, 42, 165),
            'lime': (50, 205, 50),
            'teal': (128, 128, 0),
            'maroon': (0, 0, 128),
            'black': (0,0,0)
        }
       
        self.list_fingers = []

        
        self.expression = None

        
        self.sample_rate = 44100
        self.chunk = 2048
        self.p = pyaudio.PyAudio()
        

        self.format = pyaudio.paInt16
        self.channels = 1
        


        self.mp_face_mesh = mp.solutions.face_mesh
        self.mp_drawing = mp.solutions.drawing_utils
        self.face_mesh = self.mp_face_mesh.FaceMesh()
        self.mp_face_detection = mp.solutions.face_detection
        self.face_detection = self.mp_face_detection.FaceDetection(min_detection_confidence=0.6)
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

        
        self.EAR_THRESHOLD = 0.15
        self.BLINK_CONSECUTIVE_imgS = 3
        self.blink_counter = 0
        self.eye_blink_start_time = None
        self.blink_duration=None
        self.eye_blink_status=False
        self.EAR=None

        self.hand = mp.solutions.hands
        self.hands = self.hand.Hands(
            static_image_mode=False,
            max_num_hands=1,
            model_complexity=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        self.hand_draw = mp.solutions.drawing_utils
        self.tip_points_id = [4, 8, 12, 16, 20]
        self.left_angle=""
        self.right_angle=""

        self.labels = ["background", "aeroplane", "bicycle", "bird", 
                  "boat","bottle", "bus", "car", "cat", "chair", "cow", 
                  "diningtable","dog", "horse", "motorbike", "person", "pottedplant", 
                  "sheep","sofa", "train", "tvmonitor"]
        
        cwd = os.path.abspath(os.path.dirname(__file__))



        self.object_detectioncolors = np.random.uniform(0, 255, size=(len(self.labels), 3))
        caffe_model_path=os.path.abspath(os.path.join(cwd,"Caffe/SSD_MobileNet.caffemodel"))
        caffe_model_txt=os.path.abspath(os.path.join(cwd,"Caffe/SSD_MobileNet_prototxt.txt"))
        self.nn = dnn.readNetFromCaffe(caffe_model_txt, caffe_model_path)
        self.idx=15


        self.file_names=[]
        self.known_names=[]
        self.known_faces=[]
        self.name=""

        
       
        path = os.path.abspath(os.path.join(cwd, "trained_models/dlib_face_recognition_resnet_model_v1.dat"))
        self.face_recognition_model = dlib.face_recognition_model_v1(path)


        self.hog_face_detector = dlib.get_frontal_face_detector()
        
        model_path = os.path.abspath(os.path.join(cwd, "trained_models/shape_predictor_68_face_landmarks.dat"))
        
        self.dlib_facelandmark = dlib.shape_predictor(model_path)
        
    def face_recognizer(self,img,draw=True):
        gray = cvtColor(img, COLOR_BGR2GRAY)
        faces = self.hog_face_detector(gray)
        for face in faces:
            landmarks = self.dlib_facelandmark(gray, face)
            face_descriptor = self.face_recognition_model.compute_face_descriptor(img, landmarks)
            match_found = False
            for i, known_face in enumerate(self.known_faces):
                distance = np.linalg.norm(np.array(face_descriptor) - np.array(known_face))
                
                if distance < 0.6:
                    self.name = self.known_names[i]
                    match_found = True
                    break
            if not match_found:
                self.name = "unknown"

            left, top, right, bottom = face.left(), face.top(), face.right(), face.bottom()

        
            rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2, LINE_AA)

        
            rectangle(img, (left, bottom - 35), (right, bottom), (0, 0, 255), FILLED)
            font = FONT_HERSHEY_DUPLEX
            putText(img, self.name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1, LINE_AA)
        return img,self.name
    def face_recognition_setup(self,file_names_list=[]):
        
        
        self.file_names = file_names_list
        self.known_names = [os.path.splitext(os.path.basename(file))[0].replace('_', ' ') for file in self.file_names]
        for file_name in self.file_names:
            image = imread(file_name)
            gray = cvtColor(image, COLOR_BGR2GRAY)
            faces = self.hog_face_detector(gray)
            for face in faces:
                landmarks = self.dlib_facelandmark(gray, face)
                face_descriptor = self.face_recognition_model.compute_face_descriptor(image, landmarks)
                self.known_faces.append(face_descriptor)



    def detect_objects(self,img,draw=True):
         (h, w) = img.shape[:2]
         blob = dnn.blobFromImage(resize(img, (300, 300)), 0.007843, (300, 300), 127.5)
         self.nn.setInput(blob)
         detections = self.nn.forward()
         for i in np.arange(0, detections.shape[2]):
             confidence = detections[0, 0, i, 2]
             if confidence > 0.7:
                 self.idx = int(detections[0, 0, i, 1])
                 
                 box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                 (startX, startY, endX, endY) = box.astype("int")
                 label = "{}: {:.2f}%".format(self.labels[self.idx], confidence * 100)
                 if(draw):
                   rectangle(img, (startX, startY), (endX, endY), self.object_detectioncolors[self.idx], 2,lineType=LINE_AA)
                 
                   y = startY - 15 if startY - 15 > 15 else startY + 15
                   putText(img, label, (startX, y),FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2,lineType=LINE_AA)
         return img,self.labels[self.idx]
    def detect_body(self, img, draw=True):
     image = cvtColor(img, COLOR_BGR2RGB)
     
     results = self.pose.process(image)
     if results.pose_landmarks:

        

        landmarks = results.pose_landmarks.landmark
        shoulder = [landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
        elbow = [landmarks[self.mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[self.mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
        wrist = [landmarks[self.mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[self.mp_pose.PoseLandmark.LEFT_WRIST.value].y]

        ab_distance = math.hypot(elbow[0] - shoulder[0], elbow[1] - shoulder[1])
        bc_distance = math.hypot(wrist[0] - elbow[0], wrist[1] - elbow[1])

        radians = math.atan2(wrist[1] - elbow[1], wrist[0] - elbow[0]) - math.atan2(shoulder[1] - elbow[1], shoulder[0] - elbow[0])
        self.left_angle = abs(radians * 180.0 / math.pi)

        right_shoulder = [landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
        right_elbow = [landmarks[self.mp_pose.PoseLandmark.RIGHT_ELBOW.value].x, landmarks[self.mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
        right_wrist = [landmarks[self.mp_pose.PoseLandmark.RIGHT_WRIST.value].x, landmarks[self.mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

        ab_distance = math.hypot(right_elbow[0] - right_shoulder[0], right_elbow[1] - right_shoulder[1])
        bc_distance = math.hypot(right_wrist[0] - right_elbow[0], right_wrist[1] - right_elbow[1])

        radians_right = math.atan2(right_wrist[1] - right_elbow[1], right_wrist[0] - right_elbow[0]) - math.atan2(right_shoulder[1] - right_elbow[1], right_shoulder[0] - right_elbow[0])
        self.right_angle = abs(radians_right * 180.0 / math.pi)


        if draw:
          self.mp_drawing.draw_landmarks(img, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)
     
     return img, self.left_angle,self.right_angle


    def speak(self,text="",lang="en",slow=False,filename="example.mp3"):
        audio = gTTS(text=text, lang=lang, slow=slow)
        audio.save(filename)
        mixer.init()
        mixer.music.load(filename)
        mixer.music.play()
        while mixer.music.get_busy():
            time.sleep(0.01)
    
    def wait(self,second):
        time.sleep(second)

    def start_stream(self):
        self.stream = self.p.open(format=self.format,
                                  channels=self.channels,
                                  rate=44100,
                                  input=True,
                                  frames_per_buffer=self.chunk)

    

    def detect_sound(self):
     data = self.stream.read(self.chunk)
     audio_data = list(struct.unpack(f"{self.chunk}h", data))
     sound_intensity = math.sqrt(sum(x ** 2 for x in audio_data) / len(audio_data))
     return int(sound_intensity)
    def stop_stream(self):
        if hasattr(self, 'stream') and self.stream.is_active():
            self.stream.stop_stream()
            self.stream.close()
        self.p.terminate()

    
    def press(self,key=str):
        pyautogui.press(key)

    def detect_blink(self,img,draw=True):
        gray = cvtColor(img, COLOR_BGR2GRAY)
        faces = self.hog_face_detector(gray)
        for face in faces:
           
         face_landmarks = self.dlib_facelandmark(gray, face)
         if face_landmarks is not None:
            leftEye = []
            rightEye = []
            for n in range(0, 68):
                    x = face_landmarks.part(n).x
                    y = face_landmarks.part(n).y
                    if(draw):
                        circle(img, (x, y), 1, (0, 0, 255), -1,LINE_AA)
            for n in range(36, 42):
                    x = face_landmarks.part(n).x
                    y = face_landmarks.part(n).y
                    leftEye.append((x, y))
                    next_point = n + 1
                    if n == 41:
                        next_point = 36
                    x2 = face_landmarks.part(next_point).x
                    y2 = face_landmarks.part(next_point).y
                    if(draw):
                        line(img, (x, y), (x2, y2), (0, 0, 255), 1, LINE_AA)
            for n in range(42, 48):
                    x = face_landmarks.part(n).x
                    y = face_landmarks.part(n).y
                    rightEye.append((x, y))
                    next_point = n + 1
                    if n == 47:
                        next_point = 42
                    x2 = face_landmarks.part(next_point).x
                    y2 = face_landmarks.part(next_point).y
                    if(draw):
                        line(img, (x, y), (x2, y2), (0, 0, 255), 1, LINE_AA)
            if(draw):
                    x, y, w, h = face.left(), face.top(), face.width(), face.height()
                    rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2, LINE_AA)

            A = distance.euclidean(leftEye[1], leftEye[5])
            B = distance.euclidean(leftEye[2], leftEye[4])
            C = distance.euclidean(leftEye[0], leftEye[3])
            left_ear = (A + B) / (2.0 * C)
            A = distance.euclidean(rightEye[1], rightEye[5])
            B = distance.euclidean(rightEye[2], rightEye[4])
            C = distance.euclidean(rightEye[0], rightEye[3])
            right_ear = (A + B) / (2.0 * C)
            self.EAR = (left_ear + right_ear) / 2
            self.EAR = round(self.EAR, 2)
            if self.EAR < self.EAR_THRESHOLD:
                self.blink_counter += 1
                self.eye_blink_status=True
                if self.blink_counter == 1:
                    self.eye_blink_start_time = time.time()
            else:
                
                self.eye_blink_status=False 
                if self.blink_counter >= self.BLINK_CONSECUTIVE_imgS:
                    end_time = time.time()
                    self.blink_duration = end_time - self.eye_blink_start_time
                
                self.blink_counter = 0
        if(self.blink_duration!=None):
         formatted_blink_duration = f"{self.blink_duration:.2f}"
         self.blink_duration=None
         return img,self.EAR,self.eye_blink_status,formatted_blink_duration
        else:
            return img,self.EAR,self.eye_blink_status,self.blink_duration


    def detect_colors(self,img,circle_color="",text_color="",draw=True):
        
        circle_color = circle_color.lower()
        text_color = text_color.lower()

        
        hsv_img = cvtColor(img, COLOR_BGR2HSV)
        
        height, width, _ = img.shape
        center_x = int(width / 2)
        center_y = int(height / 2)
         
        pixel_center = hsv_img[center_y, center_x]
        hue_value = pixel_center[0]
        color=""
        if hue_value<5 :
              color="red"

        elif hue_value < 40:
            color = "yellow"
        elif hue_value < 78:
            color = "green"
        elif hue_value < 125:
            color = "blue"
        elif hue_value < 170:
            color = "purple"
        elif(hue_value>170):
            color = "red"
        if(draw):
           if circle_color in self.colors:
            circle(img, (center_x, center_y), 5, self.colors[circle_color], 3,LINE_AA)
           else:
               circle(img, (center_x, center_y), 5,self.colors["black"] , 3,LINE_AA)

           if text_color in self.colors:
            putText(img, f"Color: {color}", (50, 50),
                                FONT_HERSHEY_SIMPLEX, 1, self.colors[text_color], 2, LINE_AA)
            
           else:
               putText(img, f"Color: {color}", (50, 50),
                                FONT_HERSHEY_SIMPLEX, 1, self.colors["green"], 2, LINE_AA)
               
            
        return img,color,hue_value
    
    def count_faces(self, img, draw=True):
        img_rgb = cvtColor(img, COLOR_BGR2RGB)
        results = self.face_detection.process(img_rgb)

        face_count = 0
        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                
                if draw:
                    self.mp_drawing.draw_detection(img, detection)
                    
                face_count += 1

        return img, face_count
    
    def emotion(self, img,line_color="",text_color="",draw=True,text=True):
        line_color= line_color.lower()
        text_color = text_color.lower()

        rgb_img = cvtColor(img, COLOR_BGR2RGB)
        self.results = self.face_mesh.process(rgb_img)
        
        if self.results.multi_face_landmarks:
            
            for face_landmarks in self.results.multi_face_landmarks:
                if (draw == True):
                    if line_color in self.colors:
                        
                            
                            self.mp_drawing.draw_landmarks(img, face_landmarks, self.mp_face_mesh.FACEMESH_TESSELATION,
                                                           landmark_drawing_spec=None,
                                                           connection_drawing_spec=self.mp_drawing.DrawingSpec(
                                                               color=self.colors[line_color], thickness=1,
                                                               circle_radius=1))
                    else:
                        self.mp_drawing.draw_landmarks(img, face_landmarks, self.mp_face_mesh.FACEMESH_TESSELATION,
                                                           landmark_drawing_spec=None,
                                                           connection_drawing_spec=self.mp_drawing.DrawingSpec(
                                                               color=self.colors["red"], thickness=1,
                                                               circle_radius=1))
                        

                mouth_openness = abs((face_landmarks.landmark[13].y - face_landmarks.landmark[14].y) + \
                                     (face_landmarks.landmark[15].y - face_landmarks.landmark[16].y))

                self.expression = "happy" if mouth_openness > 0.035 else "unhappy"

                if (text):
                    if text_color in self.colors:
                        putText(img, f"Face Emotion: {self.expression}", (50, 50),
                                FONT_HERSHEY_SIMPLEX, 1, self.colors[text_color], 2, LINE_AA)
                    else:
                        putText(img, f"Face Emotion: {self.expression}", (50, 50),
                                FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, LINE_AA)
        else:
            self.expression=""
        
        return img, self.expression


    def detect_hand(self, img,line_color="",circle_color="", draw=True):
        img=flip(img,1)
        line_color= line_color.lower()
        circle_color= circle_color.lower()
        rgb_img = cvtColor(img, COLOR_BGR2RGB)
        self.results = self.hands.process(rgb_img)
        finger_status = []
        hand_status = False
        h, w, c = img.shape
        if self.results.multi_hand_landmarks:
            for which_hand, handLandmarks in zip(self.results.multi_handedness, self.results.multi_hand_landmarks):
                myHand = {}

                landmark_location_list = []
            
                for id, landmark in enumerate(handLandmarks.landmark):
                    x, y, z = int(landmark.x * w), int(landmark.y * h), int(landmark.z * w)
                    landmark_location_list.append([x, y, z])
                

                if draw:
                    
                    if line_color in self.colors and circle_color in self.colors:

                        self.hand_draw.draw_landmarks(
                            img, handLandmarks, self.hand.HAND_CONNECTIONS,
                            landmark_drawing_spec=self.hand_draw.DrawingSpec(
                                color=self.colors[circle_color], thickness=2, circle_radius=4),
                            connection_drawing_spec=self.hand_draw.DrawingSpec(color=self.colors[line_color],
                                                                               thickness=2, circle_radius=2))
                    else:
                        self.hand_draw.draw_landmarks(img, handLandmarks,
                                                      self.hand.HAND_CONNECTIONS)

                self.list_fingers = []
                if which_hand.classification[0].label == "Left":
                    if landmark_location_list[self.tip_points_id[0]][0] > \
                            landmark_location_list[self.tip_points_id[0] - 1][0]:
                        self.list_fingers.append(1)
                    else:
                        self.list_fingers.append(0)
                else:
                    if landmark_location_list[self.tip_points_id[0]][0] < landmark_location_list[self.tip_points_id[0] - 1][0]:
                        self.list_fingers.append(1)
                    else:
                        self.list_fingers.append(0)

                for id in range(1, 5):
                    if landmark_location_list[self.tip_points_id[id]][1] < landmark_location_list[self.tip_points_id[id] - 2][1]:
                        self.list_fingers.append(1)
                    else:
                        self.list_fingers.append(0)

                
                if self.list_fingers == [0, 0, 0, 0, 0]:
                    hand_status = False
                if self.list_fingers == [1, 1, 1, 1, 1]:
                    hand_status = True
        else:
            self.list_fingers=[]


        return img, self.list_fingers, hand_status
    