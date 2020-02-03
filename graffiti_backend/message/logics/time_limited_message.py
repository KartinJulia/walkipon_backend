import datetime
from message.logics.abstract_message import AbstractMessage

class TimeLimitedMessage(AbstractMessage):
    """ TODO: this type of message can expire, so it should be deleted when the message expired
    """
    def __init__(self, database_message_instance):
        #super(self.__class__, self).__init__(database_message_instance)
        super().__init__(database_message_instance)
        self.__release_expire_time_utc = database_message_instance.release_expire_time_utc
        self.__usage_expire_time_utc = database_message_instance.usage_expire_time_utc

    def set_release_expire_time_utc(self, release_expire_time_utc):
        self.__release_expire_time_utc = release_expire_time_utc

    def get_release_expire_time_utc(self, release_expire_time_utc):
        return self.__release_expire_time_utc

    def is_release_expired(self):
        now = datetime.datetime.now()
        if(now < self.__release_expire_time_utc):
            return True
        return False

    def set_usage_expire_time(self, usage_expire_time_utc):
        self.__usage_expire_time_utc = usage_expire_time_utc

    def get_usage_expire_time(self, usage_expire_time_utc):
        return self.__usage_expire_time_utc

    def is_usage_expired(self):
        now = datetime.datetime.now()
        if(now < self.__usage_expire_time_utc):
            return True
        return False

    def delete_message(self):
        Message.objects.filter(id=self.__message_id).delete()