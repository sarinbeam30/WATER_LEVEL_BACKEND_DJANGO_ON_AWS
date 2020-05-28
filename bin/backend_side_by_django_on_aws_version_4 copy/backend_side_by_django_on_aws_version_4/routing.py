from channels.routing import ProtocolTypeRouter, ChannelNameRouter, URLRouter
from django_with_PostgreSQL_app.mqtt_consumers import MqttConsumer


application = ProtocolTypeRouter({
    "channel": ChannelNameRouter({
        "mqtt": MqttConsumer
    }),
})