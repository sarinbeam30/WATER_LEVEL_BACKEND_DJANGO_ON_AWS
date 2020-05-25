from __future__ import absolute_import, unicode_literals
from celery.schedules import crontab
from celery import shared_task

import paho.mqtt.client as mqtt
import time, sys

import requests, os, time

@shared_task()
def update_water_level_api():
    URL_AWS = "http://django-env.eba-cwpa3c9w.ap-southeast-1.elasticbeanstalk.com"
    requests.get(URL_AWS)
    print("GET MA LEAW")



########### -------------- MQTT SECTION ------------------ ****************
# MQTT Initialize
MQTT_BROKER_URL = "hairdresser.cloudmqtt.com"
MQTT_BROKER_PORT = 17758
MQTT_BROKER_SSL = 27758
MQTT_BROKER_USER = "odbyktmn"
MQTT_BROKER_PWD = "9esnfcLYs5wF"

ID = 'MQTT'
client = mqtt.Client(ID)

def on_connect(client, userdata, rc):
    print("SUB LEAW")
   

def on_message(client, userdata, msg):
    print(str(msg.topic) + " : " + str(msg.payload.decode('utf-8')) )

def on_disconnect():
    print('Disconnected from MQTT broker, reconnecting...')
    client.loop_stop(force=False)
    if rc != 0:
        print("Unexpected disconnection.")
    else:
        print("Disconnected")

def connect_to_mqtt_broker():
    client.username_pw_set(username=MQTT_BROKER_USER, password=MQTT_BROKER_PWD)
    client.connect(host=MQTT_BROKER_URL, port=MQTT_BROKER_PORT, keepalive=60)
    print("CONNECT_TO_BROKER_SUCCESS")
    client.subscribe([("BOARD_1",1),("BOARD_2",1)])
    client.on_message = on_message
    client.loop_stop()

    
@shared_task()
def mqtt_task():
    connect_to_mqtt_broker()
    print("KO TEST NOI")

while True:
    mqtt_task()
    update_water_level_api()
    time.sleep(20)