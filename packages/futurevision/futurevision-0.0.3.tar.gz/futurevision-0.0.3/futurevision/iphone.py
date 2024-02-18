"""

futurevision/iPhone.py
   _____                _           _   _                      _ _   ______    _ _
  / ____|              | |         | | | |               /\   | (_) |  ____|  | (_)
 | |     _ __ ___  __ _| |_ ___  __| | | |__  _   _     /  \  | |_  | |__   __| |_ ___
 | |    | '__/ _ \/ _` | __/ _ \/ _` | | '_ \| | | |   / /\ \ | | | |  __| / _` | / __|
 | |____| | |  __/ (_| | ||  __/ (_| | | |_) | |_| |  / ____ \| | | | |___| (_| | \__ \
  \_____|_|  \___|\__,_|\__\___|\__,_| |_.__/ \__, | /_/    \_\_|_| |______\__,_|_|___/
                                               __/ |
                                              |___/

"""
import logging

from time import sleep
from flask import Flask, jsonify,request
from threading import Thread

class iPhone:
    def __init__(self, port=5001):
        self.status = ""
        self.app = Flask(__name__)
        self.app.route('/data', methods=['POST'])(self.receive_data)
        self.server_thread = Thread(target=self.run)
        self.server_running = False
        self.led_status=False
        self.led_matrixi = ["0", "0", "0", "0", "0"]
        self.read_data_value=""
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.ERROR)
        if not self.server_running:
            self.server_thread.start()
            self.server_running = True


    def flash_on(self):
        self.led_status=False
        self.status = "flashon"
    def send_data(self,data):
        self.led_status=False
        self.status = data
    def flash_off(self):
        self.led_status=False
        self.status = "flashoff"

    def screen_brightness(self,volume):
        self.led_status=False
        
        self.status = "sb"+str(volume)
    def volume_intensity(self,volume_intensity):
        self.led_status=False
        
        self.status = "v"+str(volume_intensity)

    def led_on(self,pin):
    
        self.led_status=True
        if(pin==1):
            self.led_matrixi[0]="1"
        if(pin==2):
            self.led_matrixi[1]="1"
        if(pin==3):
            self.led_matrixi[2]="1"
        if(pin==4):
            self.led_matrixi[3]="1"
        if(pin==5):
            self.led_matrixi[4]="1"
        

    def led_off(self,pin):
        self.led_status=True
        
        if(pin==1):
            self.led_matrixi[0]="0"
        if(pin==2):
            self.led_matrixi[1]="0"
        if(pin==3):
            self.led_matrixi[2]="0"
        if(pin==4):
            self.led_matrixi[3]="0"
        if(pin==5):
            self.led_matrixi[4]="0"
        

    def receive_data(self):
        data = request.json
        self.read_data_value = data.get('message')
        
        if(self.led_status==False):
            response = {'result1': self.status}
        if(self.led_status==True):
            led_string = "".join(self.led_matrixi)
            led_string="led"+led_string
            response = {'result1': led_string}

        return jsonify(response)
    
    def read_data(self):
        if(self.read_data_value=="15" or self.read_data_value==15 ):
            self.read_data_value=None

        return self.read_data_value
    def wait(self, second):
        sleep(second)

    def run(self):
        self.app.run(debug=False, host='0.0.0.0', port=5001)

