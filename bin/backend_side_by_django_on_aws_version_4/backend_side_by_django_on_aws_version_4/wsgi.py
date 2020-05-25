import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_side_by_django_on_aws_version_4.settings')

application = get_wsgi_application()
