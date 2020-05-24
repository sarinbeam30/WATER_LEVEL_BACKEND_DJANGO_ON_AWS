from .models import data_logger_model
from rest_framework import serializers
from datetime import datetime
from django.db import models

class data_logger_serializer(serializers.ModelSerializer):
    date_and_time = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S")

    class Meta:
        model = data_logger_model
        fields = ['sensor', 'water_level', 'longitude', 'latitude', 'location', 'date_and_time']
    
    