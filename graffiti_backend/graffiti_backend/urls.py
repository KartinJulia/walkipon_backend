"""graffiti_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import pdb
from django.conf.urls import include, url
from django.conf import settings
#from django.views.decorators.csrf import csrf_exempt
#from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns
#from . import views
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('user_authentication.urls')),
    url(r'^', include('user_data.urls')),
    url(r'^', include('message.urls')),
    re_path(r'^v0/static/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
