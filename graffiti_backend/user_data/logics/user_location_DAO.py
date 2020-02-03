import os
import json
from abc import abstractmethod
from django.db.models import Q
from rest_framework.exceptions import ValidationError
from user_data.logics.abstract_user_DAO import AbstractUserDAO
from user_data.logics.user_location import UserLocation as UserLocationLogic
from user_data.models.user_location import UserLocation as UserLocationModel
from user_data.commons import UserDataCategory
from user_data.serializers.user_location_serializers import UserLocationCreateSerializer, UserLocationDetailSerializer

class UserLocationDAO(AbstractUserDAO):

    def create_data(self, data_dictionary):
        serializer = UserLocationCreateSerializer(data=data_dictionary)
        try:
            serializer.is_valid()
            database_user_location_data_instance = serializer.save()
        except Exception as detail:
            error_message = "%s" % detail
            raise ValidationError(error_message)
        return UserLocationLogic(database_user_location_data_instance)

    def read_data(self, data_id):
        database_user_location_data_instance = UserLocationModel.objects.get(data_id)
        return UserLocationLogic(database_user_location_data_instance)

    def read_multiple_data(self, object_id):
        pass

    def read_multiple_data(self, data_dictionary):
        user_id = data_dictionary['user_id']
        date_from = data_dictionary['date_from']
        date_to = data_dictionary['date_to']
        database_user_location_data_instances = UserLocationModel.objects.filter(user_id=user_id).filter(Q(time_utc__range=(date_from, date_to))).order_by('time_utc')
        for database_user_location_data_instance in database_user_location_data_instances:
            logic_user_location_data_instance = UserLocationLogic(database_user_location_data_instance)
            logic_user_location_data_instances.append(logic_user_location_data_instance)
        return logic_user_location_data_instances

    '''
    @staticmethod
    def update_data(data_dictionary, logic_data_instance):
        if 'location' in data_dictionary:
            location_data = json.loads(data_dictionary['location'])
            logic_data_instance.set_location(location_data[0], location_data[1])
        if 'time_utc' in data_dictionary:
            logic_data_instance.set_time_utc(data_dictionary['time_utc'])
        return UserLocationDAO.__write_database_handler(logic_data_instance)
    '''

    def update_data(self, data_dictionary, logic_data_instance):
        pass

    def update_file(self, data_dictionary, logic_data_instance):
        pass

    '''
    @staticmethod
    def __write_database_handler(logic_data_instance):
        database_user_location_data_instance = UserLocationModel.objects.get(logic_data_instance.data_id())
        if logic_data_instance.get_location() != None:
            database_user_location_data_instance.location = logic_data_instance.get_location()
        if logic_data_instance.get_longitude() != None:
            database_user_location_data_instance.longitude = logic_data_instance.get_longitude()
        if logic_data_instance.get_latitude() != None:
            database_user_location_data_instance.latitude = logic_data_instance.get_latitude()
        database_user_location_data_instance.save()
        return UserLocationLogic(database_user_location_data_instance)
    '''

    def __write_database_handler(self, logic_data_instance):
        pass

    def __write_file_handler(self, logic_data_instance, data_dictionary):
        pass

    def get_data_overview_json(self, logic_data_instance):
        pass

    def get_data_detail_json(self, logic_data_instance):
        pass

    def get_multiple_data_overview_json(self, logic_data_instances):
        pass

    def get_multiple_data_detail_json(self, logic_data_instances):
        for logic_data_instance in logic_data_instances:
            database_user_location_data_instances.append(logic_data_instance.get_database_user_data_instance())
        serializer = UserLocationDetailSerializer(database_user_location_data_instances, many=True)
        return serializer.data

    def get_multiple_data_detail_json(self, user_id, date_from=None, date_to=None):
        database_user_location_data_instances = UserLocationModel.objects.filter(user_id=user_id).filter(Q(time_utc__range=(date_from, date_to))).order_by('time_utc')
        serializer = UserLocationDetailSerializer(database_user_location_data_instances, many=True)
        return serializer.data

    def delete_data(self, user_id, data_id):
        '''
        TODO: need implement delete method.
        '''
        pass