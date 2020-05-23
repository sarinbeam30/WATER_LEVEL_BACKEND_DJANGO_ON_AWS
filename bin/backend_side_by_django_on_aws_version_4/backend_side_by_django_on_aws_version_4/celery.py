from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.http import HttpResponse
from kombu.utils.url import safequote

aws_access_key = safequote('AKIAXRAXOT3LS55XGFWA')
aws_secret_key = safequote('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')

broker_url = "sqs://{aws_access_key}:{aws_secret_key}@".format(
    aws_access_key=aws_access_key, aws_secret_key=aws_secret_key,
)

broker_transport_options = {'region': 'ap-southeast-1'}
os.environ.setdefault("DJANGO_SETTINGS_MODULE","backend_side_by_django_on_aws_version_4.settings")
app = Celery('backend_side_by_django_on_aws_version_4', broker=broker_url)
app.autodiscover_tasks()