import os
import json
from django.contrib.gis import geos
from django.contrib.gis.measure import Distance, D
from rest_framework.exceptions import ValidationError
from user_data.commons import UserDataCategory
from user_data.logics.user_location_DAO import UserLocationDAO
from user_data.logics.user_location import UserLocation

class UserDAOFactory(object):
    @staticmethod
    def create_data(data_dictionary, user_data_category):
        if 'user_data_category' in data_dictionary:
            del data_dictionary['user_data_category']
        if user_data_category == UserDataCategory.LOCATION_DATA:
            user_DAO = UserLocationDAO()
            logic_user_data_instance = user_DAO.create_data(data_dictionary)
        '''
        TODO: implement other DAO for different data type.
        '''
        return logic_user_data_instance

    @staticmethod
    def get_logic_data(object_id, user_data_category):
        if user_data_category == UserDataCategory.LOCATION_DATA:
            user_DAO = UserLocationDAO()
            logic_user_data_instance = user_DAO.read_data(object_id)
        '''
        TODO: implement other DAO for different data type.
        '''
        return logic_user_data_instance

    '''
    TODO: get multiple data.
    '''
    @staticmethod
    def get_multiple_data(data_dictionary, user_data_category):
        if user_data_category == UserDataCategory.LOCATION_DATA:
            user_DAO = UserLocationDAO()
            logic_user_data_instances = user_DAO.read_multiple_data(data_dictionary)
        return logic_user_data_instances

    @staticmethod
    def update_data(data_dictionary, logic_user_data_instance):
        '''
        TODO: update user data.
        '''
        pass

    @staticmethod
    def get_data_overview_json(logic_user_data_instance):
        '''
        TODO: return user data overview in json format.
        '''
        pass

    @staticmethod
    def get_data_detail_json(logic_user_data_instance):
        '''
        TODO: return user data detail in json format.
        '''
        pass

    @staticmethod
    def get_multiple_data_overview_json(logic_user_data_instances, user_data_category):
        '''
        TODO: return multiple user data overview in json format.
        '''
        pass

    @staticmethod
    def get_multiple_data_detail_json(logic_user_data_instances, user_data_category):
        '''
        TODO: return multiple user data detail in json format.
        '''
        if user_data_category == UserDataCategory.LOCATION_DATA:
            user_DAO = UserLocationDAO()
            return user_DAO.get_multiple_data_detail_json(logic_user_data_instances)

    @staticmethod
    def write_database_handler(logic_user_data_instance):
        pass

    @staticmethod
    def write_file_handler(logic_user_data_instance, data_dictionary):
        pass