import pdb
from django.conf.urls import include, url
from django.conf import settings
#from django.views.decorators.csrf import csrf_exempt
#from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^v0/users/$', views.user_view_handler),
    #url(r'^v0/users/(?P<user_id>\d+)$', views.user_view_handler),
    url(r'^v0/login/$', views.login_view_handler),
    url(r'^v0/logout/$', views.logout_view_handler),
    # TODO: Social login. 
]