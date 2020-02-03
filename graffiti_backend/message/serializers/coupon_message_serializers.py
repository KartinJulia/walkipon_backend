import json
from django.conf import settings
from django.contrib.gis import geos
from rest_framework import serializers
from rest_framework_gis.serializers import GeoModelSerializer
from user_authentication.models import User
from message.models.message import Message
from message.models.criteria import Criteria
from message.commons import MessageCategory, MessageType
from message.serializers.criteria_serializers import CriteriaCreateSerializer, CriteriaInfoSerializer
from store.models.store import Store
from store.models.address import Address
from store.serializers.address_serializers import AddressCreateSerializer, AddressDetailSerializer
from store.serializers.store_serializers import StoreBasicInfoSerializer


class CouponMessageCreateSerializer(GeoModelSerializer):
    user_id = serializers.IntegerField()
    #store_id = serializers.IntegerField()
    location = serializers.CharField()
    #address = AddressCreateSerializer(required=False)
    #criteria = CriteriaCreateSerializer(required=False)
    criteria = serializers.JSONField()
    address = serializers.JSONField()
    class Meta:
        model = Message
        fields = (
            'user_id',
            #'author',
            #'store_id',
            # TODO: 'company_id',
            'location',
            'address',
            'title',
            'category',
            'type',
            'criteria',
            'image',
            'created_time_utc',
            'release_expire_time_utc',
            'usage_expire_time_utc',
        )
        geo_field = 'location'
        #extra_kwargs = {'criteria': {'required': False}}

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user = User.objects.get(id=user_id)
        #store_id = validated_data.pop('store_id')
        #store = Store.objects.get(id=store_id)
        location_data = json.loads(validated_data.pop('location'))
        point = "POINT(%s %s)" % (float(location_data[0]), float(location_data[1]))
        location = geos.fromstr(point)

        if 'criteria' in validated_data:
            #criteria_data = validated_data.pop('criteria')
            criteria_data = json.loads(validated_data.pop('criteria'))
            criteria = Criteria.objects.create(**criteria_data)
            #criteria = CriteriaCreateSerializer(data=criteria_data)
            if 'address' in validated_data:
                address_data = json.loads(validated_data.pop('address'))
                address = Address.objects.create(**address_data)
                message = Message.objects.create(
                    author=user,
                    location=location,
                    longitude=location_data[0],
                    latitude=location_data[1],
                    criteria=criteria,
                    address=address,
                    **validated_data
                )
            else:
                message = Message(
                    author=user,
                    location=location,
                    longitude=location_data[0],
                    latitude=location_data[1],
                    criteria=criteria,
                    address=address,
                    **validated_data
                )
        else:
            if 'address' in validated_data:
                address_data = json.loads(validated_data.pop('address'))
                address = Address.objects.create(**address_data)
                message = Message.objects.create(
                    author=user,
                    location=location,
                    longitude=location_data[0],
                    latitude=location_data[1],
                    address=address,
                    **validated_data
                )
            else:
                message = Message(
                    author=user,
                    location=location,
                    longitude=location_data[0],
                    latitude=location_data[1],
                    **validated_data
                )
        message.save()
        return message

class CouponMessageOverviewSerializer(GeoModelSerializer):
    #message_id = serializers.SerializerMethodField('get_message_id')
    #message_id = serializers.IntegerField()
    #message_id = serializers.ReadOnlyField()
    message_id = serializers.ModelField(model_field=Message()._meta.get_field('id'))
    criteria = CriteriaInfoSerializer(read_only=True)
    class Meta:
        model = Message
        fields = (
            'message_id',
            'location',
            'title',
            'category',
            'type',
            'criteria',
            'created_time_utc',
            'release_expire_time_utc',
            'usage_expire_time_utc',
        )
        geo_field = 'location'

    #def get_message_id(self, object):
    #    return object.id


class CouponMessageDetailSerializer(GeoModelSerializer):
    message_id = serializers.ModelField(model_field=Message()._meta.get_field('id'))
    image = serializers.SerializerMethodField('get_message_image_url')
    address = AddressDetailSerializer(read_only=True)
    criteria = CriteriaInfoSerializer(read_only=True)
    store = StoreBasicInfoSerializer(read_only=True)
    class Meta:
        model = Message
        fields = (
            'message_id',
            'author',
            'location',
            'address',
            'store',
            'title',
            'category',
            'criteria',
            'image',
            'created_time_utc',
            'release_expire_time_utc',
            'usage_expire_time_utc',
        )
        geo_field = 'location'

    def get_message_image_url(self, object):
        path = str(object.image)
        if path is '':
            return None
        path = path.split('/')
        image_name = path[-1]
        return settings.MEDIA_URL + 'image/' + image_name

