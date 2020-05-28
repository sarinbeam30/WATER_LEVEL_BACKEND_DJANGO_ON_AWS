from django.contrib import admin
from django.db import models
from .models import data_logger_model

class data_logger_admin(admin.ModelAdmin):
    model = data_logger_model
    list_display = ('id','sensor', 'water_level', 'longitude', 'latitude', 'location', 'date_and_time', )

admin.site.register(data_logger_model, data_logger_admin)
