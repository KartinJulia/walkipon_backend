import json
from django.conf import settings
from django.contrib.gis import geos
from rest_framework import serializers
from rest_framework_gis.serializers import GeoModelSerializer
from user_authentication.models import User
from message.models.message import Message
from message.models.criteria import Criteria
from message.serializers.criteria_serializers import CriteriaCreateSerializer, CriteriaInfoSerializer
from store.models.address import Address
from store.models.store import Store
from store.serializers.address_serializers import AddressCreateSerializer, AddressDetailSerializer
from store.serializers.store_serializers import StoreCreateSerializer, StoreBasicInfoSerializer


class MessageCreateSerializer(GeoModelSerializer):
    user_id = serializers.IntegerField()
    location = serializers.CharField()
    address = AddressCreateSerializer(required=False)
    class Meta:
        model = Message
        fields = (
            'title',
            'user_id',
            #'author',
            'store_id',
            'category',
            'type',
            'create_time_utc',
            'usage',
            'criteria',
            'release_expire_time_utc',
            'usage_expire_time_utc',
            'location',
            'address',
            'allowed_read_times',
            'total_scores',
            'text',
            'audio',
            'image',
            'video',
        )
        geo_field = 'location'

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user = User.objects.get(id=user_id)
        type = validated_data.pop('type')
        location_data = json.loads(validated_data.pop('location'))
        point = "POINT(%s %s)" % (float(location_data[0]), float(location_data[1]))
        location = geos.fromstr(point)
        store_id = validated_data.pop('store_id')
        store = Store.objects.get(id=store_id)
        criteria_data = validated_data.pop('criteria')
        criteria = Criteria.objects.create(**criteria_data)
        if 'address' in validated_data:
            address_data = validated_data.pop('address')
            address = Address.objects.create(**address_data)
            message = Message(
                author=user,
                store = store,
                location=location,
                longitude=location_data[0],
                latitude=location_data[1],
                type=type,
                address=address,
                criteria = criteria,
                **validated_data
            )
        else:
            message = Message(
                author=user,
                store = store,
                location=location,
                longitude=location_data[0],
                latitude=location_data[1],
                type=type,
                criteria = criteria,
                **validated_data
            )
        message.save()
        return message


class MessageOverviewSerializer(GeoModelSerializer):
    #message_id = serializers.SerializerMethodField('get_message_id')
    message_id = serializers.SerializerMethodField('get_message_id')
    class Meta:
        model = Message
        fields = (
            'message_id',
            'location',
            'title',
            'type',
            'create_time_utc',
        )
        geo_field = 'location'

    def get_message_id(self, object):
        return object.id


class MessageDetailSerializer(GeoModelSerializer):
    #message_id = serializers.SerializerMethodField('get_message_id')
    message_id = serializers.SerializerMethodField('get_message_id')
    audio = serializers.SerializerMethodField('get_message_audio_url')
    image = serializers.SerializerMethodField('get_message_image_url')
    video = serializers.SerializerMethodField('get_message_video_url')
    address = AddressDetailSerializer(read_only=True)
    critreia = CriteriaInfoSerializer(read_only=True)
    class Meta:
        model = Message
        fields = (
            'title',
            #'user_id',
            'author',
            'store',
            'category',
            'type',
            'create_time_utc',
            'usage',
            'criteria',
            'release_expire_time_utc',
            'usage_expire_time_utc',
            'location',
            'address',
            'allowed_read_times',
            'total_scores',
            'text',
            'audio',
            'image',
            'video',
        )
        geo_field = 'location'

    def get_message_id(self, object):
        return object.id

    def get_message_audio_url(self, object):
        path = str(object.audio)
        if path is '':
            return None
        path = path.split('/')
        audio_name = path[-1]
        return settings.MEDIA_URL + 'audio/' + audio_name

    def get_message_image_url(self, object):
        path = str(object.image)
        if path is '':
            return None
        path = path.split('/')
        image_name = path[-1]
        return settings.MEDIA_URL + 'image/' + image_name

    def get_message_video_url(self, object):
        path = str(object.video)
        if path is '':
            return None
        path = path.split('/')
        video_name = path[-1]
        return settings.MEDIA_URL + 'video/' + video_name

