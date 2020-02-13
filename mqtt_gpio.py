#! /usr/bin/python

import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
import json

GPIO.setmode(GPIO.BCM)   #BCM PINS 15,18

GPIO.setup(15, GPIO.IN)
GPIO.setup(18, GPIO.IN)

HOST = 'Your cloud IP address'
ACCESS_TOKEN = 'Your cloud access token'
client = mqtt.Client()

client.username_pw_set(ACCESS_TOKEN)
client.connect(HOST,Your Port, 10) #timeout = 10
client.loop_start()

while True:
 x=GPIO.input(15)
 y=GPIO.input(18)
 print("x=",x)
 print("y=",y)
 client.publish('Your/topic', json.dumps({'15':x,'18':y}),0) # QOS=0
 time.sleep(1)

client.loop_stop()
client.disconnect()

