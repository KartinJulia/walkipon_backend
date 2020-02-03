import os
from abc import abstractmethod

class AbstractUser(object):
    def __init__(self, database_user_instance):
        self.__database_user_instance = database_user_instance
        self.__user_id = database_user_instance.id
        self.__email = database_user_instance.email
        self.__username = database_user_instance.username
        self.__password = database_user_instance.password
        self.__created_at_utc = database_user_instance.created_at_utc
        self.__user_type = database_user_instance.user_type
        self.__profile_image = database_user_instance.profile_image

    def set_database_user_instance(self, database_user_instance):
        self.__database_user_instance = database_user_instance
        self.__user_id = database_user_instance.id
        self.__email = database_user_instance.email
        self.__username = database_user_instance.username
        self.__password = database_user_instance.password
        self.__created_at_utc = database_user_instance.created_at_utc
        self.__user_type = database_user_instance.user_type
        self.__profile_image = database_user_instance.profile_image

    def get_database_user_instance(self):
        return self.__database_user_instance

    def user_id(self):
        return self.__user_id

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_username(self, username):
        self.__username = username

    def get_username(self):
        return self.__username

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

    def created_at_utc(self):
        return self.__created_at_utc

    def set_user_type(self, user_type):
        self.__user_type = user_type

    def get_user_type(self):
        return self.__user_type

    def set_profile_image_by_request(self, request):
        if self.__profile_image != '':
            os.remove(str(self.__profile_image))
        if request.data['profile_image'] == 'null':
            self.__database_user_instance.profile_image = None
        else:
            self.__database_user_instance.profile_image = request.data['profile_image']
        self.__database_user_instance.save()
        self.__profile_image = self.__database_user_instance.profile_image

    def set_profile_image(self, profile_image):
        self.__profile_image = profile_image

    def get_profile_image(self):
        return self.__profile_image

    @abstractmethod
    def get_message_overview_json(self, offset, limit,  message_type=None):
        pass

    @abstractmethod
    def get_message_detail_json(self, offset, limit,  message_type=None):
        pass
