from django.conf import settings
from django.contrib.gis import geos
from rest_framework import serializers
from rest_framework_gis.serializers import GeoModelSerializer
from store.models.address import Address

class AddressCreateSerializer(GeoModelSerializer):
    class Meta:
        model = Address
        fields = (
            'number',
            'street',
            'city',
            'state',
            'zipcode',
        )

    def create(self, validated_data):
        return Address.objects.create(**validated_data)


class AddressDetailSerializer(GeoModelSerializer):
    class Meta:
        model = Address
        fields = (
            'number',
            'street',
            'city',
            'state',
            'zipcode',
        )
