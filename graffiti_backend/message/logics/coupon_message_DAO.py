import os
import json
from django.conf import settings
from django.contrib.gis import geos
from django.core.exceptions import ValidationError
from message.commons import MessageType
from message.models.message import Message
from message.logics.coupon_message import CouponMessage
from message.logics.abstract_message_DAO import AbstractMessageDAO
from message.serializers.coupon_message_serializers import CouponMessageCreateSerializer, CouponMessageOverviewSerializer, CouponMessageDetailSerializer


class CouponMessageDAO(AbstractMessageDAO):
    '''
    '''
    def create_message(self, data_dictionary):
        serializer = CouponMessageCreateSerializer(data=data_dictionary)
        try:
            serializer.is_valid()
            database_message_instance = serializer.save()
        except Exception as detail:
            error_message = "%s" % detail
            raise ValidationError(error_message)
        return CouponMessage(database_message_instance)

    def read_message(self, message_id):
        database_message_instance = Message.objects.get(pk=message_id)
        return CouponMessage(database_message_instance)

    def get_message_count_by_user(self, user_id):
        return Message.objects.filter(author_id=user_id, type=MessageType.COUPON_MESSAGE.value).count()

    def get_message_count_by_location(self, location, radius):
        return Message.objects.filter(author_id=user_id, type=MessageType.COUPON_MESSAGE.value).count()

    def read_messages_by_user(self, data_dictionary):
        user_id = data_dictionary['user_id']
        logic_messages_instances = list()
        if data_dictionary['offset'] == None and data_dictionary['limit'] == None:
            database_messages_instances = Message.objects.filter(author_id=user_id, type=MessageType.COUPON_MESSAGE.value).order_by('created_time_utc')
        else:
            offset = data_dictionary['offset']
            limit = data_dictionary['limit']
            offset = int(offset)
            limit = int(limit) + int(offset)
            database_messages_instances = Message.objects.filter(author_id=user_id, type=MessageType.COUPON_MESSAGE.value).order_by('created_time_utc')[offset:limit]
        for database_message_instance in database_messages_instances:
            logic_message_instance = CouponMessage(database_message_instance)
            logic_messages_instances.append(logic_message_instance)
        return logic_messages_instances

    def read_messages_by_user(self, user_id, offset, limit):
        offset = int(offset)
        limit = int(limit) + int(offset)
        database_messages_instances = Message.objects.filter(author_id=user_id, type=MessageType.COUPON_MESSAGE.value).order_by('created_time_utc')[offset:limit]
        logic_messages_instances = list()
        for database_message_instance in database_messages_instances:
            logic_message_instance = CouponMessage(database_message_instance)
            logic_messages_instances.append(logic_message_instance)
        return logic_messages_instances

    def read_messages_by_location(self, data_dictionary):
        location = data_dictionary['location']
        radius = data_dictionary['radius']
        location_data = json.loads(location)
        point = "POINT(%s %s)" % (float(location_data[0]), float(location_data[1]))
        location_geos = geos.fromstr(point, srid = 4326)
        logic_messages_instances = list()
        if data_dictionary['offset'] == None and data_dictionary['limit'] == None:
            database_messages_instances = Message.objects.filter(location__distance_lte=(location_geos, Distance(m = radius)), type=MessageType.COUPON_MESSAGE.value).order_by('distance')
        else:
            offset = data_dictionary['offset']
            limit = data_dictionary['limit']
            offset = int(offset)
            limit = int(limit) + int(offset)
            database_messages_instances = Message.objects.filter(location__distance_lte=(location_geos, Distance(m = radius)), type=MessageType.COUPON_MESSAGE.value).order_by('distance')[offset:limit]
        for database_message_instance in database_messages_instances:
            logic_message_instance = CouponMessage(database_message_instance)
            logic_messages_instances.append(logic_message_instance)
        return logic_messages_instances

    def read_messages_by_location(self, location, radius, offset, limit):
        offset = int(offset)
        limit = int(limit) + int(offset)
        database_messages_instances = Message.objects.filter(location__distance_lte=(location_geos, Distance(m = radius)), type=MessageType.COUPON_MESSAGE.value).order_by('distance')[offset:limit]
        logic_messages_instances = list()
        for database_message_instance in database_messages_instances:
            logic_message_instance = CouponMessage(database_message_instance)
            logic_messages_instances.append(logic_message_instance)
        return logic_messages_instances

    def update_message(self, data_dictionary, logic_message_instance):
        if 'title' in data_dictionary:
            logic_message_instance.set_title(data_dictionary['title'])
        if 'author' in data_dictionary:
            logic_message_instance.set_author(data_dictionary['author'])
        if 'owner' in data_dictionary:
            logic_message_instance.add_owner(data_dictionary['owner'])
        if 'location' in data_dictionary:
            location_data = json.loads(data_dictionary['location'])
            logic_message_instance.set_location(location_data[0], location_data[1])
        if 'text' in data_dictionary:
            logic_message_instance.set_text(data_dictionary['text'])
        self.__write_database_handler(logic_message_instance, data_dictionary)
        self.__write_file_handler(logic_message_instance, data_dictionary)

    #@staticmethod
    #def update_file(data_dictionary, logic_message_instance):
    #   pass

    def __write_database_handler(self, logic_message_instance, data_dictionary):
        database_message_instance = logic_message_instance.get_database_message_instance()
        if 'title' in data_dictionary:
            database_message_instance.title = logic_message_instance.get_title()
        if 'author' in data_dictionary:
            database_message_instance.author = logic_message_instance.get_author()
        if 'location' in data_dictionary:
            database_message_instance.location = logic_message_instance.get_location()
        if 'text' in data_dictionary:
            database_message_instance.text = logic_message_instance.get_text()
        database_message_instance.save()
    '''
    def __write_database_handler(self, logic_message_instance):
        database_message_instance = logic_message_instance.get_database_message_instance()
        if logic_message_instance.get_title() != None:
            database_message_instance.title = logic_message_instance.get_title()
        if logic_message_instance.get_author() != None:
            database_message_instance.author = logic_message_instance.get_author()
        if logic_message_instance.get_new_owners() != None:
            new_owners = logic_message_instance.get_new_owners()
            for new_owner in new_owners:
                database_message_instance.owners.add(new_owner)
        if logic_message_instance.get_location() != None:
            database_message_instance.location = logic_message_instance.get_location()
        if logic_message_instance.get_text() != None:
            database_message_instance.text = logic_message_instance.get_text()
        database_message_instance.save()
    '''

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
            database_message_instance.save()

    def get_message_overview_json(self, logic_message_instance):
        logic_message_instance.increase_total_read_times()
        serializer = CouponMessageOverviewSerializer(logic_message_instance.get_database_message_instance())
        return serializer.data

    def get_message_detail_json(self, logic_message_instance):
        logic_message_instance.increase_total_read_times()
        serializer = CouponMessageDetailSerializer(logic_message_instance.get_database_message_instance())
        return serializer.data

    def get_messages_overview_json(self, logic_messages_instances):
        database_messages_instances = list()
        for logic_message_instance in logic_message_instances:
            database_messages_instances.append(logic_message_instance.get_database_message_instance())
        serializer = CouponMessageOverviewSerializer(database_messages_instances, many=True)
        return serializer.data

    def get_messages_detail_json(self, logic_messages_instances):
        database_messages_instances = list()
        for logic_message_instance in logic_message_instances:
            logic_message_instance.increase_total_read_times()
            database_messages_instances.append(logic_message_instance.get_database_message_instance())
        serializer = CouponMessageDetailSerializer(database_messages_instances, many=True)
        return serializer.data

    def get_messages_overview_json_by_user(self, user_id, offset, limit):
        total_message_count = self.get_message_count_by_user(user_id)
        if int(offset) > total_message_count or int(offset)+int(limit) > total_message_count:
            raise ValueError('Your request messages more than record.')
        logic_messages_instances = self.read_messages_by_user(user_id, offset, limit)
        database_messages_instances = list()
        for logic_message_instance in logic_messages_instances:
            database_messages_instances.append(logic_message_instance.get_database_message_instance())
        serializer = CouponMessageOverviewSerializer(database_messages_instances, many=True)
        return json.dumps({"total_message_count": total_message_count, "offset": offset, "limit": limit, "messages_overview": serializer.data})

    def get_messages_detail_json_by_user(self, user_id, offset, limit):
        total_message_count = self.get_message_count_by_user(user_id)
        if int(offset) > total_message_count or int(offset)+int(limit) > total_message_count:
            raise ValueError('Your request messages more than record.')
        logic_messages_instances = self.read_messages_by_user(user_id, offset, limit)
        database_messages_instances = list()
        for logic_message_instance in logic_messages_instances:
            database_messages_instances.append(logic_message_instance.get_database_message_instance())
        serializer = CouponMessageDetailSerializer(database_messages_instances, many=True)
        return json.dumps({"total_message_count": total_message_count, "offset": offset, "limit": limit, "messages_detail": serializer.data})

    def get_messages_overview_json_by_location(self, location, radius, offset, limit):
        total_message_count = self.get_message_count_by_location(location, radius)
        if int(offset) > total_message_count or int(offset)+int(limit) > total_message_count:
            raise ValueError('Your request messages more than record.')
        logic_messages_instances = self.read_messages_by_location(location, radius, offset, limit)
        database_messages_instances = list()
        for logic_message_instance in logic_messages_instances:
            database_messages_instances.append(logic_message_instance.get_database_message_instance())
        serializer = CouponMessageOverviewSerializer(database_messages_instances, many=True)
        return json.dumps({"total_message_count": total_message_count, "offset": offset, "limit": limit, "messages_overview": serializer.data})
    
    def get_messages_detail_json_by_location(self, location, radius, offset, limit):
        total_message_count = self.get_message_count_by_location(location, radius)
        if int(offset) > total_message_count or int(offset)+int(limit) > total_message_count:
            raise ValueError('Your request messages more than record.')
        logic_messages_instances = self.read_messages_by_location(location, radius, offset, limit)
        database_messages_instances = list()
        for logic_message_instance in logic_messages_instances:
            database_messages_instances.append(logic_message_instance.get_database_message_instance())
        serializer = CouponMessageDetailSerializer(database_messages_instances, many=True)
        return json.dumps({"total_message_count": total_message_count, "offset": offset, "limit": limit, "messages_detail": serializer.data})

    def delete_data(self, user_id, message_id):
        pass