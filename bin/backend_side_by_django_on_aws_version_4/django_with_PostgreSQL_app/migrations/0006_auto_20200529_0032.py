# Generated by Django 2.2.12 on 2020-05-29 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_with_PostgreSQL_app', '0005_auto_20200526_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_logger_model',
            name='date_and_time',
            field=models.TextField(),
        ),
    ]
