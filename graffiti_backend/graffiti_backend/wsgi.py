"""
WSGI config for graffiti_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""
#import sys
import os

from django.core.wsgi import get_wsgi_application

#sys.path.append('/var/www/graffiti_backend')

#sys.path.append('/var/www/graffiti_backend/graffiti_backend')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "graffiti_backend.settings")

application = get_wsgi_application()
