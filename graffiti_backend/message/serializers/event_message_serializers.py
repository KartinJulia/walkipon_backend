import json
from django.conf import settings
from django.contrib.gis import geos
from rest_framework import serializers
from rest_framework_gis.serializers import GeoModelSerializer
from user_authentication.models import User
from message.models.message import Message
from message.commons import MessageType
from store.models.address import Address
from store.serializers.address_serializers import AddressCreateSerializer, AddressDetailSerializer


class EventMessageCreateSerializer(GeoModelSerializer):
    user_id = serializers.IntegerField()
    location = serializers.CharField()
    address = AddressCreateSerializer(required=False)
    class Meta:
        model = Message
        fields = (
            'user_id',
            #'author',
            'anonymous',
            'location',
            'address',
            'title',
            'message_type',
            'text',
            'image',
            'video',
            'created_at_utc',
            'modified_at_utc',
            'until_at_utc',
        )
        geo_field = 'location'

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user = GraffitiUser.objects.get(id=user_id)
        location_data = json.loads(validated_data.pop('location'))
        point = "POINT(%s %s)" % (float(location_data[0]), float(location_data[1]))
        location = geos.fromstr(point)
        if 'address' in validated_data:
            address_data = validated_data.pop('address')
            address = Address.objects.create(**address_data)
            message = Message(
                author=user,
                location=location,
                longitude=location_data[0],
                latitude=location_data[1],
                message_type=MessageType.EVENT_MESSAGE,
                address=address,
                **validated_data
            )
        else:
            message = Message(
                author=user,
                location=location,
                longitude=location_data[0],
                latitude=location_data[1],
                message_type=MessageType.EVENT_MESSAGE,
                **validated_data
            )
        message.save()
        return message


class EventMessageOverviewSerializer(GeoModelSerializer):
    message_id = serializers.SerializerMethodField()
    class Meta:
        model = Message
        fields = (
            'message_id',
            'location',
            'title',
            'message_type',
            'created_at_utc',
            'until_at_utc',
            'total_read_times',
            'total_liked_times',
        )
        geo_field = 'location'

    def get_message_id(self, object):
        return object.id


class EventMessageDetailSerializer(GeoModelSerializer):
    message_id = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField('get_message_image_url')
    video = serializers.SerializerMethodField('get_message_video_url')
    address = AddressDetailSerializer(read_only=True)
    class Meta:
        model = Message
        fields = (
            'message_id',
            'author',
            'anonymous',
            'location',
            'address',
            'title',
            'message_type',
            'text',
            'image',
            'video',
            'created_at_utc',
            'total_read_times',
            'total_liked_times',
            'modified_at_utc',
            'until_at_utc',
        )
        geo_field = 'location'

    def get_message_id(self, object):
        return object.id

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

