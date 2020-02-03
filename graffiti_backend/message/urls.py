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
    url(r'^v0/users/(?P<user_id>\d+)/coupon_messages$', views.commercial_user_coupon_message_view_handler),
    url(r'^v0/users/(?P<user_id>\d+)/coupon_messages/(?P<option>(overview|detail))$', views.commercial_user_coupon_message_view_handler),
    url(r'^v0/users/(?P<user_id>\d+)/coupon_messages/(?P<message_id>\d+)$', views.commercial_user_coupon_message_view_handler),
    url(r'^v0/users/(?P<user_id>\d+)/coupon_messages/location$', views.nearby_coupon_messages_view_handler),
    # TODO: Social login. 
]