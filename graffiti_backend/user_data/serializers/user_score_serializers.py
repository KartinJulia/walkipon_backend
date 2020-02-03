import json
from django.conf import settings
from django.contrib.gis import geos
from rest_framework import serializers
from user_data.models.user_score import UserScore


class UserScoreSerializer(serializers.ModelSerializer):
    user_id = serializers.SerializerMethodField('get_user_id')
    store_id = serializers.SerializerMethodField('get_store_id')
    class Meta:
        model = UserScore
        fields = (
            'user_id',
            'store_id',
            'score_type',
            'score_value'
        )

    def get_user_id(serf, object):
        return object.user.id

    def get_store_id(serf, object):
        return object.store.id