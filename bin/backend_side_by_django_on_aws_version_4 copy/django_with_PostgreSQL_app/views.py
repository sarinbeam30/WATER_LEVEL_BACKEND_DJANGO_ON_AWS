from django.shortcuts import render
from rest_framework import generics
from .models import data_logger_model
from .serializers import data_logger_serializer

# Create your views here.

class ListWaterLevelView(generics.ListAPIView):
    queryset = data_logger_model.objects.all()
    serializer_class = data_logger_serializer

class DetailWaterLevelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = data_logger_model.objects.all()
    serializer_class = data_logger_serializer
