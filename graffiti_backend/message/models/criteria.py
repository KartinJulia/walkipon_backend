from django.conf import settings
from django.contrib.gis import geos
from django.contrib.gis.db import models as gis_models
from django.db import models
from datetime import datetime

class Criteria(models.Model):
    required = models.BooleanField(default=False)
    min_score = models.IntegerField(null=True)
