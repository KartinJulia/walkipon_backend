import os
import json
from django.contrib.gis import geos
from django.contrib.gis.measure import Distance, D
from rest_framework.exceptions import ValidationError
from message.commons import MessageCategory, MessageType, MessageSearchIdentifier
from message.models import Message
from message.logics.coupon_message_DAO import CouponMessageDAO
from message.logics.message_DAO import MessageDAO


class MessageDAOFactory(object):
    @staticmethod
    def create_message(data_dictionary, message_type):
        if 'message_type' in data_dictionary:
            del data_dictionary['message_type']
        if message_type == MessageType.COUPON_MESSAGE.value:
            message_DAO = CouponMessageDAO()
            logic_message_instance = message_DAO.create_message(data_dictionary)
        '''
        TODO: create other kind of messages
        '''
        
        return logic_message_instance

    @staticmethod
    def get_logic_message(message_id, message_type):
        #database_message_instance = MessageDAOFactory.read_database_handler(message_id)
        if message_type == MessageType.COUPON_MESSAGE.value:
            message_DAO = CouponMessageDAO()
            logic_message_instance = message_DAO.read_message(message_id)
        '''
        TODO: read other kind of message
        '''
        
        return logic_message_instance

    @staticmethod
    def get_logic_messages_by_user(data_dictionary, message_type=None):
        logic_message_instances = list()
        if message_type != None:
            if message_type == MessageType.COUPON_MESSAGE.value:
                message_DAO = CouponMessageDAO()
                logic_message_instances = CouponMessageDAO.read_messages_by_user(data_dictionary)
            '''
            TODO: read other kind of messages
            '''
        else:
            logic_message_instances = MessageDAO.read_messages_by_user(data_dictionary)
      
        return logic_message_instances

    @staticmethod
    def get_logic_messages_by_location(data_dictionary, message_type=None):
        '''
        TODO: serarch identifier
        '''
        logic_message_instances = list()
        if message_type != None:
            if message_type == MessageType.COUPON_MESSAGE.value:
                message_DAO = CouponMessageDAO()
                logic_message_instances = CouponMessageDAO.read_messages_by_location(data_dictionary)
            '''
            TODO: read other kind of messages
            '''
        else:
            logic_message_instances = MessageDAO.read_messages_by_location(data_dictionary)
      
        return logic_message_instances

    @staticmethod
    def update_message(data_dictionary, logic_message_instance, message_type):
        if message_type == MessageType.COUPON_MESSAGE.value:
            message_DAO = CouponMessageDAO()
            message_DAO.update_message(data_dictionary, logic_message_instance)
        '''
        TODO: update other kind of messages
        '''
        

    ################################# TODO: delete message. #############################################
    #@staticmethod
    #def delete_message(message_id):
    #####################################################################################################

    @staticmethod
    def get_message_overview_json(logic_message_instance):
        if logic_message_instance.get_message_type() == MessageType.COUPON_MESSAGE.value:
            message_DAO = CouponMessageDAO()
            return message_DAO.get_message_overview_json(logic_message_instance)

    @staticmethod
    def get_message_detail_json(logic_message_instance):
        if logic_message_instance.get_message_type() == MessageType.COUPON_MESSAGE.value:
            message_DAO = CouponMessageDAO()
            return message_DAO.get_message_detail_json(logic_message_instance)

    @staticmethod
    def get_messages_overview_json(logic_message_instances, message_type=None):
        if message_type != None:
            if message_type == MessageType.COUPON_MESSAGE.value:
                message_DAO = CouponMessageDAO()
                return message_DAO.get_messages_overview_json(logic_message_instances)
            #TODO: different type of message
        else:
            message_DAO = MessageDAO()
            return message_DAO.get_messages_overview_json(logic_message_instances)

    @staticmethod
    def get_messages_detail_json(logic_message_instances, message_type=None):
        database_message_instances = list()
        if message_type != None:
            if message_type == MessageType.COUPON_MESSAGE.value:
                message_DAO = CouponMessageDAO()
                return message_DAO.get_messages_detail_json(logic_message_instances)
            #TODO: different type of message
        else:
            return MessageDAO.get_messages_detail_json(logic_message_instances)

    @staticmethod
    def get_messages_overview_json_by_user(user_id, offset, limit, message_type=None):
        if message_type != None:
            if message_type == MessageType.COUPON_MESSAGE.value:
                message_DAO = CouponMessageDAO()
                return message_DAO.get_messages_overview_json_by_user(user_id, offset, limit)
            #TODO: different type of message
        else:
            #TODO: return all kind of messages json.
            pass

    @staticmethod
    def get_messages_detail_json_by_user(user_id, offset, limit, message_type=None):
        if message_type != None:
            if message_type == MessageType.COUPON_MESSAGE.value:
                message_DAO = CouponMessageDAO()
                return message_DAO.get_messages_detail_json_by_user(user_id, offset, limit)
            #TODO: different type of message
        else:
            #TODO: return all kind of messages json.
            pass

    @staticmethod
    def get_messages_overview_json_by_location(location, radius, offset, limit, message_type=None):
        if message_type != None:
            if message_type == MessageType.COUPON_MESSAGE.value:
                message_DAO = CouponMessageDAO()
                return message_DAO.get_messages_overview_json_by_location(location, radius, offset, limit)
            #TODO: different type of message
        else:
            #TODO: return all kind of messages json.
            pass

    @staticmethod
    def get_messages_detail_json_by_location(location, radius, offset, limit):
        if message_type != None:
            if message_type == MessageType.COUPON_MESSAGE.value:
                message_DAO = CouponMessageDAO()
                return message_DAO.get_messages_detail_json_by_location(location, radius, offset, limit)
            #TODO: different type of message
        else:
            #TODO: return all kind of messages json.
            pass
