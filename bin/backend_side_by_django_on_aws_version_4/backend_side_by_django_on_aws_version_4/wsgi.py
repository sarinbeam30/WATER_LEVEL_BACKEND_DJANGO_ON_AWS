"""
WSGI config for backend_side_by_django_on_aws_version_4 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_side_by_django_on_aws_version_4.settings')

application = get_wsgi_application()
