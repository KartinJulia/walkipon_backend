import os
import json
from django.conf import settings
from django.contrib.gis import geos
from django.core.exceptions import ValidationError
from message.commons import MessageType
from message.models.message import Message as MessageModel
from message.logics.message import Message as MessageLogic
from message.logics.abstract_message_DAO import AbstractMessageDAO
from message.serializers.message_serializers import MessageCreateSerializer, MessageOverviewSerializer, MessageDetailSerializer


class MessageDAO(AbstractMessageDAO):
    '''
    '''
    def create_message(self, data_dictionary):
        serializer = MessageCreateSerializer(data=data_dictionary)
        try:
            serializer.is_valid()
            database_message_instance = serializer.save()
        except Exception as detail:
            error_message = "%s" % detail
            raise ValidationError(error_message)
        return MessageLogic(database_message_instance)

    def read_message(self, message_id):
        database_message_instance = Message.objects.get(pk=message_id)
        return MessageLogic(database_message_instance)

    def read_messages_by_user(self, data_dictionary):
        user_id = data_dictionary['user_id']
        if data_dictionary['offset'] == None and data_dictionary['limit'] == None:
            database_messages_instances = Message.objects.filter(author_id=user_id).order_by('created_time_utc')
        else:
            offset = data_dictionary['offset']
            limit = data_dictionary['limit']
            database_messages_instances = Message.objects.filter(author_id=user_id).order_by('created_time_utc')[offset:limit]
        for database_message_instance in database_messages_instances:
            logic_message_instance = MessageLogic(database_message_instance)
            logic_messages_instances.append(logic_message_instance)
        return logic_messages_instances

    def read_messages_by_location(self, data_dictionary):
        location = data_dictionary['location']
        radius = data_dictionary['radius']
        location_data = json.loads(location)
        point = "POINT(%s %s)" % (float(location_data[0]), float(location_data[1]))
        location_geos = geos.fromstr(point, srid = 4326)
        if data_dictionary['offset'] == None and data_dictionary['limit'] == None:
            database_messages_instances = Message.objects.filter(location__distance_lte=(location_geos, Distance(m = radius)), category=MessageType.COUPON_MESSAGE).order_by('distance')
        else:
            offset = data_dictionary['offset']
            limit = data_dictionary['limit']
            database_messages_instances = Message.objects.filter(location__distance_lte=(location_geos, Distance(m = radius)), category=MessageType.COUPON_MESSAGE).order_by('distance')[offset:limit]
        for database_message_instance in database_messages_instances:
            logic_message_instance = MessageLogic(database_message_instance)
            logic_messages_instances.append(logic_message_instance)
        return logic_messages_instances

    def update_message(self, data_dictionary, logic_message_instance):
        if 'title' in data_dictionary:
            logic_message_instance.set_title(data_dictionary['title'])
        if 'author' in data_dictionary:
            logic_message_instance.set_author(data_dictionary['author'])
        if 'owner' in data_dictionary:
            logic_message_instance.add_owner(data_dictionary['owner'])
        if 'store' in data_dictionary:
            logic_message_instance.set_store(data_dictionary['store'])
        if 'category' in data_dictionary:
            logic_message_instance.set_category(data_dictionary['category'])
        if 'type' in data_dictionary:
            logic_message_instance.set_type(data_dictionary['type'])
        #if 'create_time_utc' in data_dictionary:
        if 'usage' in data_dictionary:
            logic_message_instance.set_usage(data_dictionary['usage'])
        if 'criteria' in data_dictionary:
            logic_message_instance.set_criteria(data_dictionary['criteria'])
        if 'release_expire_time_utc' in data_dictionary:
            logic_message_instance.set_release_expire_time_utc(data_dictionary['release_expire_time_utc'])
        if 'usage_expire_time_utc' in data_dictionary:
            logic_message_instance.set_usage_expire_time(data_dictionary['usage_expire_time_utc'])
        if 'location' in data_dictionary:
            location_data = json.loads(data_dictionary['location'])
            logic_message_instance.set_location(location_data[0], location_data[1])
        if 'address' in data_dictionary:
            logic_message_instance.set_address(data_dictionary['address'])
        #if 'allowed_read_times' in data_dictionary:
        '''
        TODO: need to implement a message which only allow some spcific read time.
        '''
        if 'total_scores' in data_dictionary:
            logic_message_instance.set_total_scores(data_dictionary['total_scores'])
        #if 'audio' in data_dictionary:
        '''
        if 'image' in data_dictionary:
            logic_message_instance.set_image(data_dictionary['image'])
        if 'video' in data_dictionary:
            logic_message_instance.set_video(data_dictionary['video'])
        '''
        if 'text' in data_dictionary:
            logic_message_instance.set_text(data_dictionary['text'])
        self.__write_database_handler(logic_message_instance, data_dictionary)
        self.__write_file_handler(logic_message_instance, data_dictionary)

    def __write_database_handler(self, logic_message_instance, data_dictionary):
        database_message_instance = logic_message_instance.get_database_message_instance()
        if 'title' in data_dictionary:
            database_message_instance.title = logic_message_instance.get_title()
        if 'author' in data_dictionary:
            database_message_instance.author = logic_message_instance.get_author()
        '''
        if logic_message_instance.get_new_owners() != None:
            new_owners = logic_message_instance.get_new_owners
            for new_owner in new_owners:
                database_message_instance.owners.add(new_owner)
        '''
        if 'store' in data_dictionary:
            database_message_instance.store = logic_message_instance.get_store()
        if 'category' in data_dictionary:
            database_message_instance.category = logic_message_instance.get_category()
        if 'type' in data_dictionary:
            database_message_instance.type = logic_message_instance.get_type()
        if 'usage' in data_dictionary:
            database_message_instance.usage = logic_message_instance.get_usage()
        if 'criteria' in data_dictionary:
            database_message_instance.criteria = logic_message_instance.get_criteria()
        if 'release_expire_time_utc' in data_dictionary:
            database_message_instance.release_expire_time_utc = logic_message_instance.get_release_expire_time_utc()
        if 'usage_expire_time_utc' in data_dictionary:
            database_message_instance.usage_expire_time_utc = logic_message_instance.get_usage_expire_time()
        if 'location' in data_dictionary:
            database_message_instance.location = logic_message_instance.get_location()
        if 'address' in data_dictionary:
            database_message_instance.address = logic_message_instance.get_address()
        if 'total_scores' in data_dictionary:
            database_message_instance.total_scores = logic_message_instance.get_total_scores()
        if 'text' in data_dictionary:
            database_message_instance.text = logic_message_instance.get_text()
        database_message_instance.save()

    def __write_file_handler(self, logic_message_instance, data_dictionary):
        database_message_instance = logic_message_instance.get_database_message_instance()
        if 'image' in data_dictionary:
            if database_message_instance.image != None:
                os.remove(settings.MEDIA_ROOT+'/'+str(database_message_instance.image))
            if data_dictionary['image'] == 'null':
                database_message_instance.image = None
            else:
                database_message_instance.image = data_dictionary['image']
            logic_message_instance.set_image(data_dictionary['image'])
        if 'video' in data_dictionary:
            if database_message_instance.image != None:
                os.remove(settings.MEDIA_ROOT+'/'+str(database_message_instance.video))
            if data_dictionary['video'] == 'null':
                database_message_instance.video = None
            else:
                database_message_instance.video = data_dictionary['video']
            logic_message_instance.set_image(data_dictionary['video'])
        database_message_instance.save()

    def get_message_overview_json(self, logic_message_instance):
        logic_message_instance.increase_total_read_times()
        serializer = MessageOverviewSerializer(logic_message_instance.get_database_message_instance())
        return serializer.data

    def get_message_detail_json(self, logic_message_instance):
        logic_message_instance.increase_total_read_times()
        serializer = MessageDetailSerializer(logic_message_instance.get_database_message_instance())
        return serializer.data

    def get_messages_overview_json(self, logic_messages_instances):
        database_messages_instances = list()
        for logic_message_instance in logic_message_instances:
            logic_message_instance.increase_total_read_times()
            database_messages_instances.append(logic_message_instance.get_database_message_instance())
        serializer = MessageOverviewSerializer(database_messages_instances, many=True)
        return serializer.data

    def get_messages_detail_json(self, logic_messages_instances):
        database_messages_instances = list()
        for logic_message_instance in logic_message_instances:
            logic_message_instance.increase_total_read_times()
            database_messages_instances.append(logic_message_instance.get_database_message_instance())
        serializer = MessageDetailSerializer(database_messages_instances, many=True)
        return serializer.data

    '''
    TODO: delete
    '''