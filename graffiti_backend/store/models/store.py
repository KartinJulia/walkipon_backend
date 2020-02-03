from django.conf import settings
from django.contrib.gis import geos
from django.contrib.gis.db import models as gis_models
from django.db import models
from store.models.address import Address
#from user_authentication.models.user import User


class Store(models.Model):
    store_name = models.CharField(unique=True, max_length=100, blank=False)
    #store_logo = models.ImageField(upload_to=settings.MEDIA_ROOT+'/logo', null=True)
    store_logo = models.ImageField(upload_to='logo', null=True)
    #company = models.ForeignKey(Company)
    location = gis_models.PointField(u"longitude/latitude", geography=True, blank=True, null=True, srid=4326)
    longitude = models.FloatField(default=0)
    latitude = models.FloatField(default=0)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    store_manager = models.ForeignKey('user_authentication.User', on_delete=models.CASCADE, related_name="manager_commerical_user")
    #store_manager = models.ForeignKey(User, on_delete=models.CASCADE)
    #gis = gis_models.GeoManager()
    objects = models.Manager()
    
    # TODO: store inventory and cash flow