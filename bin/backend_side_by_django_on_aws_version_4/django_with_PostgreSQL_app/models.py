from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class CustomDateTimeField(models.DateTimeField):
    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        if val:
            val.replace(microsecond=0)
            return val.isoformat()
        return ''

class data_logger_model (models.Model):
    sensor = models.IntegerField(blank=False)
    water_level = models.IntegerField(blank=False)
    longitude = models.FloatField(blank=False)
    latitude = models.FloatField(blank=False)
    location = models.TextField(blank=False, max_length=30)
    # date_and_time = CustomDateTimeField(blank=False, default=timezone.now)
    # date_and_time = models.DateTimeField(blank=False, format="%d/%m/%Y %H:%i:%s", default=timezone.now)
    date_and_time = models.TextField(blank=False)

    class Meta:
        ordering=('sensor', 'date_and_time',)
        get_latest_by = 'date_and_time',
        # verbose_name = 'data_logger_model',
        db_table = 'data_logger_model'


def __str__(self):
    return self.water_level