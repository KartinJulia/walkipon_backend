from django.conf import settings
from rest_framework import serializers
from user_authentication.models import User

class UserCreateSerializer(serializers.ModelSerializer):
    #user_id = serializers.SerializerMethodField(get_user_id)
    class Meta:
        model = User
        fields = ('username',
                  'user_type',
                  'email',
                  'password',
                  'created_at_utc',
                  'profile_image'
        )

    def create(self, validated_data):
        #user = User(**validated_data)
        #user.save()
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
        if password is not None:
            user.set_password(password)
            user.save()
            return user

    #def get_user_id(self, object):
    #    return object.id

class UserDetailSerializer(serializers.ModelSerializer):
    #user_id = serializers.SerializerMethodField('get_user_id')
    user_id = serializers.SerializerMethodField()
    profile_image = serializers.SerializerMethodField('get_profile_image_url')
    class Meta:
        model = User
        fields = (
            'user_id',
            'email',
            'username',
            'created_at_utc',
            'user_type',
            'profile_image',
        )

    def get_user_id(self, object):
        return object.id

    def get_profile_image_url(self, object):
        path = str(object.profile_image)
        if path is '':
            return None
        path = path.split('/')
        image_name = path[-1]
        return settings.MEDIA_URL + 'image/profile_image/' + image_name
