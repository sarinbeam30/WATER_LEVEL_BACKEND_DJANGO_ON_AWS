from .models import data_logger_model
from rest_framework import serializers
from datetime import datetime
from django.db import models

class data_logger_serializer(serializers.ModelSerializer):

    class Meta:
        model = data_logger_model
        fields = ['id','sensor', 'water_level', 'longitude', 'latitude', 'location', 'date', 'time']
    
    