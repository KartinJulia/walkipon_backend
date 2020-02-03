from django.db import models
from django.contrib.gis import geos
from django.contrib.gis.db import models as gis_models

class Address(models.Model):
    number = models.IntegerField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length = 20)
    #objects = models.GeoManager()
    #gis = gis_models.GeoManager()
    objects = models.Manager()
