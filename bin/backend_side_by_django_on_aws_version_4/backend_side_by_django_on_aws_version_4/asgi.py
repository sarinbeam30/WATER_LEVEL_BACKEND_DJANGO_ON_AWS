import os
import django
# from django.core.asgi import get_asgi_application
from channels.layers import get_channel_layer
from channels.routing import get_default_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_side_by_django_on_aws_version_4.settings')
django.setup()

application= get_default_application()
channel_layer = get_channel_layer()