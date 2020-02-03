import os
from rest_framework.exceptions import ValidationError
from user_authentication.logics.personal_user import PersonalUser
from user_authentication.logics.commerical_user import CommericalUser
from user_authentication.models import User
from user_authentication.commons import UserType, UserSearchIdentifier
from user_authentication.serializers.user_serializers import UserCreateSerializer, UserDetailSerializer

class UserFactory(object):
    @staticmethod
    def create_user(data_dictionary):
        logic_user_instance = UserFactory.__create_database_user(data_dictionary)
        ################# TODO: commercial user ###################
        ################# TODO: super user ########################
        return logic_user_instance

    @staticmethod
    def get_logic_user(search_identifier, value):
        if search_identifier == UserSearchIdentifier.USER_ID.value:
            database_user_instance = UserFactory.read_database_handler(UserSearchIdentifier.USER_ID.value, value)
        elif search_identifier == UserSearchIdentifier.USER_EMAIL.value:
            database_user_instance = UserFactory.read_database_handler(UserSearchIdentifier.USER_EMAIL.value, value)
        else:
            return None
        
        if database_user_instance.user_type == UserType.PERSONAL_USER.value:
            logic_user_instance = UserFactory.__logic_personal_user_instance(database_user_instance)
        if database_user_instance.user_type == UserType.COMMERCIAL_USER.value:
            logic_user_instance = UserFactory.__logic_commercial_user_instance(database_user_instance)
        ################# TODO: commercial user ###################
        ################# TODO: super user ########################
        return logic_user_instance

    @staticmethod
    def update_user(data_dictionary, logic_user_instance):
        if 'email' in data_dictionary:
            logic_user_instance.set_email(data_dictionary['email'])
        if 'username' in data_dictionary:
            logic_user_instance.set_username(data_dictionary['username'])
        if 'password' in data_dictionary:
            logic_user_instance.set_password(data_dictionary['password'])
        if 'user_type' in data_dictionary:
            logic_user_instance.set_user_type(data_dictionary['user_type'])
        UserFactory.write_database_handler(UserSearchIdentifier.USER_ID, logic_user_instance, data_dictionary)
        UserFactory.write_image_handler(UserSearchIdentifier.USER_ID, logic_user_instance, data_dictionary)

    @staticmethod
    def get_user_type(user_id):
        database_user_instance = UserFactory.read_database_handler(UserSearchIdentifier.USER_ID.value, user_id)
        return database_user_instance.user_type

    @staticmethod
    def get_user_json(logic_user_instance):
        #if logic_user_instance.get_user_type() == UserType.PERSONAL_USER.value:
        serializer = UserDetailSerializer(logic_user_instance.get_database_user_instance())
        return serializer.data

    @staticmethod
    def __create_database_user(data_dictionary):
        #print(data_dictionary['user_type'])
        #if not UserType.has_value(data_dictionary['user_type']):
        #    raise ValueError('Need provide user type or user type not exisit.')
        if (data_dictionary['user_type'] == None or 
            (data_dictionary['user_type'] != UserType.PERSONAL_USER.value and 
                data_dictionary['user_type'] != UserType.COMMERCIAL_USER.value and
                data_dictionary['user_type'] != UserType.SUPER_USER.value)):
            raise ValueError('Need provide user type or user type not exisit.')
        serializer = UserCreateSerializer(data=data_dictionary)
        try:
            serializer.is_valid()
            database_user_instance = serializer.save()
        except Exception as detail:
            error_message = "%s" % detail
            raise ValidationError(error_message)
        return PersonalUser(database_user_instance)

    @staticmethod
    def __logic_personal_user_instance(database_user_instance):
        return PersonalUser(database_user_instance);

    @staticmethod
    def __logic_commercial_user_instance(database_user_instance):
        return CommericalUser(database_user_instance)

    @staticmethod
    def read_database_handler(search_identifier, value):
        if search_identifier == UserSearchIdentifier.USER_ID.value:
            return User.objects.get(id=value)
        if search_identifier == UserSearchIdentifier.USER_EMAIL.value:
            return User.objects.get(email=str(value))

    #@staticmethod
    #def read_database_handler_by_id(user_id):
    #    return User.objects.get(id=user_id)

    #@staticmethod
    #def read_database_handler_by_email(email):
    #    return User.objects.get(email=email)

    @staticmethod
    def write_database_handler(search_identifier, logic_user_instance, data_dictionary):
        if search_identifier == UserSearchIdentifier.USER_ID.value:
            database_user_instance = UserFactory.read_database_handler(UserSearchIdentifier.USER_ID, logic_user_instance.user_id())
        elif search_identifier == UserSearchIdentifier.USER_EMAIL.value:
            database_user_instance = UserFactory.read_database_handler(UserSearchIdentifier.USER_EMAIL, logic_user_instance.get_email())
        if 'email' in data_dictionary:
            database_user_instance.email = logic_user_instance.get_email()
        if 'username' in data_dictionary:
            database_user_instance.username = logic_user_instance.get_username()
        if 'password' in data_dictionary:
            database_user_instance.set_password(logic_user_instance.get_password())
        if 'user_type' in data_dictionary:
            database_user_instance.user_type = logic_user_instance.get_user_type()
        database_user_instance.save()

    @staticmethod
    def write_image_handler(search_identifier, logic_user_instance, data_dictionary):
        if 'profile_image' in data_dictionary:
            if search_identifier == UserSearchIdentifier.USER_ID.value:
                database_user_instance = UserFactory.read_database_handler(UserSearchIdentifier.USER_ID, logic_user_instance.user_id())
            elif search_identifier == UserSearchIdentifier.USER_EMAIL.value:
                database_user_instance = UserFactory.read_database_handler(UserSearchIdentifier.USER_EMAIL, logic_user_instance.get_email())
            if database_user_instance.profile_image != None:
                os.remove(settings.MEDIA_ROOT+'/'+str(database_user_instance.profile_image))
            if data_dictionary['profile_image'] == 'null':
                database_user_instance.profile_image = None
            else:
                database_user_instance.profile_image = data_dictionary['profile_image']
            logic_user_instance.set_profile_image(database_user_instance.profile_image)
            database_user_instance.save()
