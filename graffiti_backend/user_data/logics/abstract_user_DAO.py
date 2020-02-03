from django.contrib.gis import geos
from abc import abstractmethod


class AbstractUserDAO(object):
    '''
    '''
    @abstractmethod
    def create_data(data_dictionary):
        '''
        TODO: return logic
        '''
        pass

    @abstractmethod
    def read_data(object_id):
        pass

    @abstractmethod
    def read_multiple_data(object_id):
        pass

    @abstractmethod
    def read_multiple_data(data_dictionary):
        '''
        The data_dictionary is containing the query method of database.
        '''
        pass

    @abstractmethod
    def update_data(data_dictionary, logic_data_instance):
        pass

    @abstractmethod
    def update_file(data_dictionary, logic_data_instance):
        pass

    @abstractmethod
    def __write_database_handler(logic_data_instance):
        pass

    @abstractmethod
    def __write_file_handler(logic_data_instance, data_dictionary):
        pass

    @abstractmethod
    def get_data_overview_json(logic_data_instance):
        pass

    @abstractmethod
    def get_data_detail_json(logic_data_instance):
        pass

    @abstractmethod
    def get_multiple_data_overview_json(logic_data_instances):
        pass

    @abstractmethod
    def get_multiple_data_detail_json(logic_data_instances):
        pass

    @abstractmethod
    def delete_data(user_id, data_id):
        pass