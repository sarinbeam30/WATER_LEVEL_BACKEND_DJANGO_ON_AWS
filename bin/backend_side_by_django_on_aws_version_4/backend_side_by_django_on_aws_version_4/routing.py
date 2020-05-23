from channels.routing import ProtocolTypeRouter, ChannelNameRouter, URLRouter
from django_with_PostgreSQL_app.mqtt_consumers import MqttConsumer
from django.urls import path

application = ProtocolTypeRouter({
    "channel": ChannelNameRouter({
        "mqtt": MqttConsumer
    }),
})