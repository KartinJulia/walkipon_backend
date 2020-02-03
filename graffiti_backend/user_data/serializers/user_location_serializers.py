import json
from django.conf import settings
from django.contrib.gis import geos
from rest_framework import serializers
from rest_framework_gis.serializers import GeoModelSerializer
from user_authentication.models import User
from user_data.models.user_location import UserLocation


class UserLocationCreateSerializer(GeoModelSerializer):
    user_id = serializers.IntegerField()
    location = serializers.CharField()
    class Meta:
        model = UserLocation
        fields = (
            'user_id',
            'location',
            'time_utc'
        )
        geo_field = 'location'

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user = User.objects.get(id=user_id)
        location_data = json.loads(validated_data.pop('location'))
        point = "POINT(%s %s)" % (float(location_data[0]), float(location_data[1]))
        location = geos.fromstr(point)
        user_location = UserLocation(
            user = user,
            location = location,
            longitude=location_data[0],
            latitude=location_data[1],
            **validated_data
        )
        user_location.save()
        return user_location


class UserLocationDetailSerializer(GeoModelSerializer):
    class Meta:
        model = UserLocation
        fields = (
            'user_id',
            'location',
            'time_utc'
        )