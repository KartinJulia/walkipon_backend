from django.conf import settings
from django.db import models
from user_authentication.models.user import User
from store.models.store import Store

class UserScore(models.Model):
    #UNIVERSAL_SCORE = 'US'
    #STORE_SCORE = 'SS'

    #SCORE_TYPE_CHOICE = (
    #    (UNIVERSAL_SCORE, 'universal_socre'),
    #    (STORE_SCORE, 'store_score')
    #)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)
    score_type = models.CharField(max_length=30)
    #score_type = models.CharField(max_length=2, choices=UNIVERSAL_SCORE, default=UNIVERSAL_SCORE)
    score_value = models.FloatField(default=0)