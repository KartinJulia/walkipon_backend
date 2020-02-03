from django.conf import settings
from django.contrib.gis import geos
from rest_framework import serializers
from rest_framework_gis.serializers import GeoModelSerializer
from user_authentication.models import User
from store.models.store import Store
from store.models.address import Address
from store.serializers.address_serializers import AddressCreateSerializer, AddressDetailSerializer


class StoreCreateSerializer(GeoModelSerializer):
    store_id = serializers.IntegerField()
    location = serializers.CharField()
    address = AddressCreateSerializer(required=False)
    class Meta:
        model = Store
        fields = (
            'store_name',
            'store_logo',
            'location',
            'address',
            'user_id',
        )
        geo_field = 'location'

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user = User.objects.get(id=user_id)
        location_data = json.loads(validated_data.pop('location'))
        point = "POINT(%s %s)" % (float(location_data[0]), float(location_data[1]))
        location = geos.fromstr(point)
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        store = Store.objects.create(
            store_manager = user,
            location=location,
            longitude=location_data[0],
            latitude=location_data[1],
            address=address,
        )
        store.save()
        return store


class StoreBasicInfoSerializer(GeoModelSerializer):
    store_id = serializers.SerializerMethodField('get_store_id')
    store_logo = serializers.SerializerMethodField('get_store_logo_url')
    address = AddressDetailSerializer()
    class Meta:
        model = Store
        model = Store
        fields = (
            'store_name',
            'store_logo',
            'location',
            'address',
            'user_id',
        )
        geo_field = 'location'

    def get_store_id(self, object):
        return object.id

    def get_store_logo_url(self, object):
        path = str(object.image)
        if path is '':
            return None
        path = path.split('/')
        image_name = path[-1]
        return settings.MEDIA_URL + 'image/' + image_name