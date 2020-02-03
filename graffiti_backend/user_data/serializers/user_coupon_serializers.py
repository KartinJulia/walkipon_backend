from rest_framework import serializers
from user_authentication.models import User
from message.models.message import Message
from user_data.models.user_coupon import UserCoupon
from message.serializers.coupon_message_serializers import CouponMessageOverviewSerializer, CouponMessageDetailSerializer

class UserCouponCreateSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    message_id = serializers.IntegerField()
    class Meta:
        model = UserCoupon
        fields = (
            'user_id',
            'message_id',
        )

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user = User.objects.get(id=user_id)
        coupon_message_id = validated_data.pop('message_id')
        coupon_message = Message.objects.get(id=coupon_message_id)
        user_coupon = UserCoupon(
            user = user,
            coupon_message = coupon_message
        )


class UserCouponOverviewSerializer(serializers.ModelSerializer):
    user_id = serializers.SerializerMethodField('get_user_id')
    user_coupon_id = serializers.SerializerMethodField('get_user_coupon_id')
    coupon_message = CouponMessageOverviewSerializer(read_only=True)
    class Meta:
        model = UserCoupon
        fields = (
            'user_id',
            'user_coupon_id',
            'coupon_message'
        )

    def get_user_id(serf, object):
        return object.user.id

    def get_user_coupon_id(self, object):
        return object.id


class UserCouponDetailSerializer(serializers.ModelSerializer):
    user_id = serializers.SerializerMethodField('get_user_id')
    user_coupon_id = serializers.SerializerMethodField('get_user_coupon_id')
    coupon_message = CouponMessageDetailSerializer(read_only=True)
    class Meta:
        model = UserCoupon
        fields = (
            'user_id',
            'user_coupon_id',
            'coupon_message'
        )

    def get_user_id(serf, object):
        return object.user.id

    def get_user_coupon_id(self, object):
        return object.id