"""

futurevision/raspberrypi.py
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
import RPi.GPIO as GPIO
from sense_hat import SenseHat

class RaspberryPi:
    def __init__(self,sensehat=False):
        if(sensehat):
         self.sense = SenseHat()
        self.joystick_status=""
        
        

        self.IMAGES = [
        [
        0b00000000,
        0b00001000,
        0b00011100,
        0b00111110,
        0b01111111,
        0b00011100,
        0b00011100,
        0b00011100
        ],
        [
        0b00000000,
        0b00011100,
        0b00011100,
        0b00011100,
        0b01111111,
        0b00111110,
        0b00011100,
        0b00001000
    ],
    [
        0b00000000,
        0b00001000,
        0b00001100,
        0b01111110,
        0b01111111,
        0b01111110,
        0b00001100,
        0b00001000
    ],
    [
        0b00000000,
        0b00001000,
        0b00011000,
        0b00111111,
        0b01111111,
        0b00111111,
        0b00011000,
        0b00001000
    ],
    [
        0b00000000,
        0b00111110,
        0b01000001,
        0b01010101,
        0b01000001,
        0b01010101,
        0b01001001,
        0b00111110
    ],
    [
        0b00000000,
        0b00111110,
        0b01000001,
        0b01010101,
        0b01000001,
        0b01011101,
        0b01100011,
        0b00111110
    ],
    [
        0b00000000,
        0b00100010,
        0b01110111,
        0b01111111,
        0b01111111,
        0b00111110,
        0b00011100,
        0b00001000
    ]
]
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        self.matrix_colors = {
            'none': (0, 0, 0),
            'white': (255, 255, 255),
            'red': (255, 0, 0),
            'green': (0, 255, 0),
            'blue': (0, 0, 255),
            'yellow': (255, 255, 0),
            'purple': (128, 0, 128),
            'orange': (255, 140, 0),
            'pink': (255, 192, 203),
            'cyan': (0, 255, 255),
            'brown': (88, 57, 39),
            'lime': (50, 205, 50),
            'teal': (0, 128, 128),
            'maroon': (128, 0, 0)
        }
    
    
    def wait(self, second:int):
        sleep(second)
    def fill(self,color):
        color = color.lower()

        if color not in self.matrix_colors:
            print("Invalid Color")
            return
        self.sense.clear(self.matrix_colors[color])
    
    def clear(self):
        self.sense.clear()
    def show_message(
            self,
            data,
            text_colour="white",
            back_colour="none",scroll_speed=0.2
        ):
        color = text_colour.lower()
        color2 = back_colour.lower()

        if color not in self.matrix_colors:
            print("Invalid Color")
            return

        if color2 not in self.matrix_colors:
            print("Invalid Color")
            return
        self.sense.show_message(data,scroll_speed,(self.matrix_colors[color][0],self.matrix_colors[color][1],self.matrix_colors[color][2]),(self.matrix_colors[color2][0],self.matrix_colors[color2][1],self.matrix_colors[color2][2]))

    def show_letter(self,data="",text_colour="white",
                    back_colour="none"):
        data=str(data)
        color = text_colour.lower()
        color2 = back_colour.lower()
        if color2 not in self.matrix_colors:
            print("Invalid Color")
            
            return
        if color not in self.matrix_colors:
            print("Invalid Color")
            
            return
        self.sense.show_letter(data,(self.matrix_colors[color][0],self.matrix_colors[color][1],self.matrix_colors[color][2]),(self.matrix_colors[color2][0],self.matrix_colors[color2][1],self.matrix_colors[color2][2]))
        
    def show_sign(self, data,color="white"):
        color = color.lower()

        if color not in self.matrix_colors:
            print("Invalid Color")
            
            return
        
        
        
        if(data=="up"):
            pixel_list = [pixel for row in self.IMAGES[0] for pixel in [(row >> i) & 1 for i in range(7, -1, -1)]]
            rgb_values = [(value * self.matrix_colors[color][0], value * self.matrix_colors[color][1], value * self.matrix_colors[color][2]) for value in pixel_list]
            self.sense.set_pixels(rgb_values)
        elif(data=="down"):
            pixel_list = [pixel for row in self.IMAGES[1] for pixel in [(row >> i) & 1 for i in range(7, -1, -1)]]
            rgb_values = [(value * self.matrix_colors[color][0], value * self.matrix_colors[color][1], value * self.matrix_colors[color][2]) for value in pixel_list]            
            self.sense.set_pixels(rgb_values)
        elif(data=="right"):
            pixel_list = [pixel for row in self.IMAGES[2] for pixel in [(row >> i) & 1 for i in range(7, -1, -1)]]
            rgb_values = [(value * self.matrix_colors[color][0], value * self.matrix_colors[color][1], value * self.matrix_colors[color][2]) for value in pixel_list]
            self.sense.set_pixels(rgb_values)
        elif(data=="left"):
            pixel_list = [pixel for row in self.IMAGES[3] for pixel in [(row >> i) & 1 for i in range(7, -1, -1)]]
            rgb_values = [(value * self.matrix_colors[color][0], value * self.matrix_colors[color][1], value * self.matrix_colors[color][2]) for value in pixel_list]
            self.sense.set_pixels(rgb_values)
        elif(data=="happy"):
            pixel_list = [pixel for row in self.IMAGES[4] for pixel in [(row >> i) & 1 for i in range(7, -1, -1)]]
            rgb_values = [(value * self.matrix_colors[color][0], value * self.matrix_colors[color][1], value * self.matrix_colors[color][2]) for value in pixel_list]
            self.sense.set_pixels(rgb_values)
        elif(data=="unhappy"):
            pixel_list = [pixel for row in self.IMAGES[5] for pixel in [(row >> i) & 1 for i in range(7, -1, -1)]]
            rgb_values = [(value * self.matrix_colors[color][0], value * self.matrix_colors[color][1], value * self.matrix_colors[color][2]) for value in pixel_list]            
            self.sense.set_pixels(rgb_values)
        elif(data=="heart"):
            pixel_list = [pixel for row in self.IMAGES[6] for pixel in [(row >> i) & 1 for i in range(7, -1, -1)]]
            rgb_values = [(value * self.matrix_colors[color][0], value * self.matrix_colors[color][1], value * self.matrix_colors[color][2]) for value in pixel_list]            
            self.sense.set_pixels(rgb_values)
        

    def on(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)

        
    def joystick_button(self):
     for event in self.sense.stick.get_events():
        if event.action == 'pressed':
            self.joystick_status='pressed'
    
        elif event.action == 'released':
            self.joystick_status='released'
     return self.joystick_status
    

    def joystick(self):
        
        for event in self.sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "up":
                    self.joystick_status="up"
                elif event.direction == "down":
                    self.joystick_status="down"
                elif event.direction == "left": 
                    self.joystick_status="left"
                elif event.direction == "right":
                    self.joystick_status="right"
                elif event.direction == "middle":
                    self.joystick_status="middle"
        return self.joystick_status
        
 
    def get_gyroscope(self):
        gyro_data = self.sense.get_gyroscope_raw()
        return [gyro_data['x'],gyro_data['y'],gyro_data['z']]

    def get_accelerometer(self):
        accel_data = self.sense.get_accelerometer_raw()
        return [accel_data['x'],accel_data['y'],accel_data['z']]

    def get_compass(self):
        compass_data = self.sense.get_compass()
        return compass_data
    
    def read_button(self,pin):
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        status=""
        if GPIO.input(pin) == GPIO.LOW:
            status="pressed"
        return status
    def cleanup(self):
        self.GPIO.cleanup()
    def get_temperature(self):
        temp_data = self.sense.get_temperature()
        return temp_data

    def get_pressure(self):
        pressure_data = self.sense.get_pressure()
        return pressure_data

    def get_humidity(self):
        humidity_data = self.sense.get_humidity()
        return humidity_data

    def off(self, pin):

        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

    def rgb_led(self,color,r_pin,g_pin,b_pin):
        GPIO.setup(r_pin,GPIO.OUT)
        GPIO.setup(g_pin,GPIO.OUT)
        GPIO.setup(b_pin,GPIO.OUT)
        color=color.lower()

        if(color=="red"):
            GPIO.output(r_pin,GPIO.LOW)
            GPIO.output(g_pin,GPIO.HIGH)
            GPIO.output(b_pin,GPIO.HIGH)

        elif(color=="yellow"):
            GPIO.output(r_pin,GPIO.LOW)
            GPIO.output(g_pin,GPIO.LOW)
            GPIO.output(b_pin,GPIO.HIGH)

        elif(color=="green"):
            GPIO.output(r_pin,GPIO.HIGH)
            GPIO.output(g_pin,GPIO.LOW)
            GPIO.output(b_pin,GPIO.HIGH)
        
        elif(color=="blue"):
            GPIO.output(r_pin,GPIO.HIGH)
            GPIO.output(g_pin,GPIO.HIGH)
            GPIO.output(b_pin,GPIO.LOW)

        elif(color=="white"):
            GPIO.output(r_pin,GPIO.LOW)
            GPIO.output(g_pin,GPIO.LOW)
            GPIO.output(b_pin,GPIO.LOW)
        
        elif(color=="purple"):
            GPIO.output(r_pin,GPIO.LOW)
            GPIO.output(g_pin,GPIO.HIGH)
            GPIO.output(b_pin,GPIO.LOW)
        
        elif(color=="off" or color=="clear"):
            GPIO.output(r_pin,GPIO.HIGH)
            GPIO.output(g_pin,GPIO.HIGH)
            GPIO.output(b_pin,GPIO.HIGH)

        elif(color=="lightblue" or color=="lightBlue" or color=="light blue"):
            GPIO.output(r_pin,GPIO.HIGH)
            GPIO.output(g_pin,GPIO.LOW)
            GPIO.output(b_pin,GPIO.LOW)
        else:
            print("Invalid Color")
            return

    




def main():
    print(1)

if __name__ == "__main__":
    main()
