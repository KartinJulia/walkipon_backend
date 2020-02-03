from django.contrib.gis import geos
from abc import abstractmethod


class AbstractMessageDAO(object):
    '''
    '''
    @abstractmethod
    def create_message(self, data_dictionary):
        '''
        TODO: return logic
        '''
        pass

    @abstractmethod
    def read_message(self, object_id):
        pass

    @abstractmethod
    def get_message_count_by_user(self, user_id):
        pass

    @abstractmethod
    def get_message_count_by_location(self, location, radius):
        pass

    #@staticmethod
    #@abstractmethod
    #def read_messages(object_id):
    #    pass

    @abstractmethod
    def read_messages_by_user(self, data_dictionary):
        '''
        The data_dictionary is containing the query method of database.
        '''
        pass

    @abstractmethod
    def read_messages_by_user(self, user_id, offset, limit):
        pass

    @abstractmethod
    def read_messages_by_location(self, data_dictionary):
        '''
        The data_dictionary is containing the query method of database.
        '''
        pass

    @abstractmethod
    def read_messages_by_location(self, location, radius, offset, limit):
        pass

    @abstractmethod
    def update_message(self, data_dictionary, logic_message_instance):
        pass

    #@abstractmethod
    #@staticmethod
    #def update_file(data_dictionary, logic_message_instance):
    #   pass

    @abstractmethod
    def __write_database_handler(self, logic_message_instance):
        pass

    @abstractmethod
    def __write_file_handler(self, logic_message_instance, data_dictionary):
        pass

    @abstractmethod
    def get_message_overview_json(self, logic_message_instance):
        pass

    @abstractmethod
    def get_message_detail_json(self, logic_message_instance):
        pass

    @abstractmethod
    def get_messages_overview_json(self, logic_messages_instances):
        pass

    @abstractmethod
    def get_messages_detail_json(self, logic_messages_instances):
        pass

    @abstractmethod
    def get_messages_overview_json_by_user(self, user_id, offset, limit):
        pass

    @abstractmethod
    def get_messages_detail_json_by_user(self, user_id, offset, limit):
        pass

    @abstractmethod
    def get_messages_overview_json_by_location(self, location, radius, offset, limit):
        pass

    @abstractmethod
    def get_messages_detail_json_by_location(self, location, radius, offset, limit):
        pass

    @abstractmethod
    def delete_data(self, user_id, message_id):
        pass