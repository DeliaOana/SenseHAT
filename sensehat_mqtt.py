#!/usr/bin/env.python
import math
import time
import json
import paho.mqtt.publish as publish
from sense_hat import SenseHat

sense = SenseHat()

MQTT_HOST = 'mqtt.beia-telemetrie.ro'
MQTT_TOPIC = 'odsi/vlc'

while True: 
	payload_dict = {"TEMP" :  sense.get_temperature(),
                	"HUMID" : sense.get_humidity(),
                	"PRESS" : sense.get_pressure()
            	        }
        try:
            publish.single(MQTT_TOPIC, qos = 1, hostname = MQTT_HOST, payload = json.dumps(payload_dict))
        except:
            time.sleep(0.01) #TODO local storage 
	
	time.sleep(10) 