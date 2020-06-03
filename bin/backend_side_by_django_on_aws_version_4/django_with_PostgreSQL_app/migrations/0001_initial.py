# Generated by Django 2.2.12 on 2020-06-03 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data_logger_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor', models.IntegerField()),
                ('water_level', models.IntegerField()),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('location', models.TextField(max_length=30)),
                ('date', models.TextField()),
                ('time', models.TextField()),
            ],
            options={
                'db_table': 'data_logger_model',
                'ordering': ('time', 'date', 'sensor'),
                'get_latest_by': ('date',),
            },
        ),
    ]
