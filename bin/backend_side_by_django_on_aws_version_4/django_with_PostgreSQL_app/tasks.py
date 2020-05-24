from __future__ import absolute_import, unicode_literals
from celery.schedules import crontab
from celery import shared_task
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

import requests, os, time

@shared_task()

def update_water_level_api():
    URL = "http://django-env.eba-cwpa3c9w.ap-southeast-1.elasticbeanstalk.com"
    requests.get(URL)
    print("GET MA LEAW")

while True:
    time.sleep(25)
    update_water_level_api()

