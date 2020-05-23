from .models import data_logger_model
from rest_framework import serializers

class data_logger_serializer(serializers.ModelSerializer):
    class Meta:
        model = data_logger_model
        fields = ['id','sensor', 'water_level', 'longitude', 'latitude', 'location', 'date_and_time']