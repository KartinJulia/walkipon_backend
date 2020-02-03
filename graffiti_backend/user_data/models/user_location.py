from django.conf import settings
from django.contrib.gis import geos
from django.contrib.gis.db import models as gis_models
from django.db import models
from datetime import datetime
from user_authentication.models.user import User

class UserLocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = gis_models.PointField(u"longitude/latitude", geography=True, blank=True, null=True, srid=4326)
    longitude = models.FloatField(default=0)
    latitude = models.FloatField(default=0)
    time_utc = models.DateTimeField(default=datetime.now, blank=True)

    #gis = gis_models.GeoManager()
    objects = models.Manager()