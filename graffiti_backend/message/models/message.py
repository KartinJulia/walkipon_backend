from django.conf import settings
from django.contrib.gis import geos
from django.contrib.gis.db import models as gis_models
from django.db import models
from datetime import datetime
#from message_app.commons import MessageType
from user_authentication.models.user import User
#from store.models.tag import Tag
from store.models.address import Address
from store.models.store import Store
from message.models.criteria import Criteria
# When User app finish need import for authentication.

class Message(models.Model):

    #CATEGORY_REWARD_SCORE = 'RS'
    #CATEGORY_COUPON_MESSAGE = 'CM'
    #CATEGORY_RED_ENVELOPE = 'RE'

    #CATEGORY_CHOICES = (
    #    (CATEGORY_REWARD_SCORE, 'reward_score'),
    #    (CATEGORY_COUPON_MESSAGE, 'coupon'),
    #    (CATEGORY_RED_ENVELOPE, 'red_envelope'),
    #)

    title = models.CharField(max_length=100, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commerical_user") # the commerical user who post the message
    owners = models.ManyToManyField(User, related_name="personal_user")  # the personal user get the message
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)
    category = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    create_time_utc = models.DateTimeField(default=datetime.now, blank=True)
    usage = models.CharField(max_length=100, null=True)
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE, null=True, blank=True)
    created_time_utc = models.DateTimeField(null=True, blank=True)
    release_expire_time_utc = models.DateTimeField(null=True, blank=True)     # For Coupon, Event and Encounter
    usage_expire_time_utc = models.DateTimeField(null=True, blank=True) 
    location = gis_models.PointField(u"longitude/latitude", geography=True, blank=True, null=True, srid=4326)
    longitude = models.FloatField(default=0)
    latitude = models.FloatField(default=0)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    total_read_times = models.IntegerField(default=0)
    allowed_read_times = models.IntegerField(default=0)
    total_scores = models.IntegerField(default=0)
    audio = models.FileField(upload_to='audio', null=True)
    image = models.ImageField(upload_to='image/coupon', null=True)
    video = models.FileField(upload_to='video', null=True)
    text = models.TextField(blank=True, null=True)

    #gis = gis_models.GeoManager()
    objects = models.Manager()

