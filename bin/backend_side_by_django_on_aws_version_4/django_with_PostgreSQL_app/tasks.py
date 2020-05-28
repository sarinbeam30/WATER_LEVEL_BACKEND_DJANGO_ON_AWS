from __future__ import absolute_import, unicode_literals
from celery.schedules import crontab
from celery import shared_task
import time, sys, requests, os
from .models import data_logger_model
import paho.mqtt.client as mqtt

@shared_task()
def update_water_level_api():
    URL_AWS = "http://django-env.eba-cwpa3c9w.ap-southeast-1.elasticbeanstalk.com"
    requests.get(URL_AWS)
    print("GET MA LEAW")


while True:
    update_water_level_api()
    time.sleep(30)




