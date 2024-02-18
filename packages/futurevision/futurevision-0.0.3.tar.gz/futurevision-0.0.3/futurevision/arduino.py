"""

futurevision/arduino.py
   _____                _           _   _                      _ _   ______    _ _
  / ____|              | |         | | | |               /\   | (_) |  ____|  | (_)
 | |     _ __ ___  __ _| |_ ___  __| | | |__  _   _     /  \  | |_  | |__   __| |_ ___
 | |    | '__/ _ \/ _` | __/ _ \/ _` | | '_ \| | | |   / /\ \ | | | |  __| / _` | / __|
 | |____| | |  __/ (_| | ||  __/ (_| | | |_) | |_| |  / ____ \| | | | |___| (_| | \__ \
  \_____|_|  \___|\__,_|\__\___|\__,_| |_.__/ \__, | /_/    \_\_|_| |______\__,_|_|___/
                                               __/ |
                                              |___/

"""

import os
from time import sleep
from serial import Serial
from cv2 import VideoCapture, flip, cvtColor, COLOR_BGR2RGB, imshow, waitKey, putText, FONT_HERSHEY_SIMPLEX, LINE_AA,circle,COLOR_BGR2HSV,COLOR_BGR2GRAY
import mediapipe as mp
import numpy as np 


class Arduino:
    def __init__(self,usb_port=None, baud=9600):
        self.ser = Serial(usb_port, baud)

        sleep(2)
        
    def wait(self, second:int):
        sleep(second)

    def show_led_matrix(self, data, direction=1):
        if(data=="+"):
            data="arti"
        if (data == "-"):
            data = "eksi"
        if (data == "*"):
            data = "carpma"
        if (data == "/"):
            data = "bolme"
        if (data == "%"):
            data = "yuz"
        if (data == "="):
            data = "esit"
        text = "{}{}\n".format(direction, data)
        self.ser.write(bytes(text, 'utf-8'))
    def close(self):
        self.ser.close()
    
    def on(self, pin):

        text = "{}on\n".format(pin)
        self.ser.write(bytes(text, 'utf-8'))
    def read(self):
        data = self.ser.readline() 
        data = data.decode("utf-8")
        return data 

    def off(self, pin):

        text = "{}off\n".format(pin)
        self.ser.write(bytes(text, 'utf-8'))
    def rgb_led(self,color):
        
        color=color.lower()
        
        if(color=="red"):
            
            text = "rgbred\n"
            self.ser.write(bytes(text, 'utf-8'))
            
        if(color=="yellow"):
            text = "rgbyellow\n"
            self.ser.write(bytes(text, 'utf-8'))
            
        if(color=="green"):
            text = "rgbgreen\n"
            self.ser.write(bytes(text, 'utf-8'))
        
        if(color=="blue"):
            text = "rgbblue\n"
            self.ser.write(bytes(text, 'utf-8'))
            

        if(color=="white"):
            text = "rgbwhite\n"
            self.ser.write(bytes(text, 'utf-8'))
            
        
        if(color=="purple"):
            text = "rgbpurple\n"
            self.ser.write(bytes(text, 'utf-8'))
            
        
        if(color=="off" or color=="clear"):
            
            text = "rgboff\n"
            self.ser.write(bytes(text, 'utf-8'))
            

        if(color=="lightblue" or color=="lightBlue" or color=="light blue"):
            text = "rgblightblue\n"
            self.ser.write(bytes(text, 'utf-8'))
        color=""
        
