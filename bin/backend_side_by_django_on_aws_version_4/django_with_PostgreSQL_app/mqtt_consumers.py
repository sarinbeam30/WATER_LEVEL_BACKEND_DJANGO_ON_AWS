import datetime, time
from asgiref.sync import async_to_sync
from channels.consumer import SyncConsumer
from .models import data_logger_model
from django.conf import settings

class MqttConsumer(SyncConsumer):

    def mqtt_sub(self, event):
        topic = event['text']['topic']
        payload = event['text']['payload']
        print(f"topic_sub: {topic}, payload_sub: {payload}")


        #TYPE : DICT (payload)
        keys, values = zip(*payload.items())
        WATER_VALUE_STR = values[0]
        LATITUDE_STR = values[1]
        NUM_OF_SENSORS_INT = int(values[2])
        LONGITUDE_STR = values[3]
        LOCATION_STR = values[4]
        DATE_AND_TIME_STR = values[5]

        # time.sleep(5)
        data_logger_model.objects.create(sensor=NUM_OF_SENSORS_INT, water_level=WATER_VALUE_STR, longitude=LONGITUDE_STR, latitude=LATITUDE_STR, location=LOCATION_STR )
        print("It is added to table successfully")

    
    def mqtt_pub(self, event):
        topic = event['text']['topic']
        payload = event['text']['payload']
        # do something with topic and payload
        print(f"topic: {topic}, payload: {payload}")