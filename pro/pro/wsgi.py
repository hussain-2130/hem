"""
WSGI config for pro project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, seei
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pro.settings")

application = get_wsgi_application()
