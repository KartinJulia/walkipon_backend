from django.contrib.gis import geos
from abc import abstractmethod
from user_authentication.models.user import User


class AbstractMessage(object):
    """TODO: AbstractMessage
    AbstractMessage can create and update message to database.
    """
    def __init__(self, database_message_instance):
        self.__database_message_instance = database_message_instance
        self.__message_id = database_message_instance.id
        self.__title = database_message_instance.title
        self.__author = database_message_instance.author
        self.__owners = database_message_instance.owners.all()
        self.__new_owners = list()
        self.__store = database_message_instance.store
        self.__category = database_message_instance.category
        self.__type = database_message_instance.type
        self.__create_time_utc = database_message_instance.create_time_utc
        #self.__expire_at_utc = database_message_instance.modified_at_utc
        self.__usage = database_message_instance.usage
        self.__criteria = database_message_instance.criteria
        self.__location = database_message_instance.location
        self.__longitude = database_message_instance.longitude
        self.__latitude = database_message_instance.latitude
        self.__address = database_message_instance.address
        self.__total_read_times = database_message_instance.total_read_times

    def set_database_message_instance(self, database_message_instance):
        self.__database_message_instance = database_message_instance
        self.__message_id = database_message_instance.id
        self.__title = database_message_instance.title
        self.__author = database_message_instance.author
        self.__owners = database_message_instance.owners.all()
        self.__new_owners = list()
        self.__store = database_message_instance.store
        self.__category = database_message_instance.category
        self.__type = database_message_instance.type
        self.__create_time_utc = database_message_instance.create_time_utc
        #self.__expire_at_utc = database_message_instance.modified_at_utc
        self.__usage = database_message_instance.usage
        self.__criteria = database_message_instance.criteria
        self.__location = database_message_instance.location
        self.__longitude = database_message_instance.longitude
        self.__latitude = database_message_instance.latitude
        self.__address = database_message_instance.address
        self.__total_read_times = database_message_instance.total_read_times

    def get_database_message_instance(self):
        return self.__database_message_instance

    def message_id(self):
        return self.__message_id

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_author(self, user_id):
        self.__author = User.objects.get(id=user_id)

    def get_author(self):
        return self.__author

    def add_new_owner(self, user_id):
        self.__owners.append(user_id)
        self.__new_owners.append(user_id)

    def get_new_owners(self):
        return self.__new_owners

    def get_new_owners_number(self):
        return len(self.__new_owners)

    def is_new_owners_empty(self):
        if not self.__new_owners:
            return False
        return True

    def get_current_owners(self):
        return self.__owners

    def get_current_owners_number(self):
        return len(self.__owners)

    def is_current_owners_empty(self):
        if not self.__owners:
            return False
        return True

    def set_store(self, store_id):
        self.__store = Store.objects.get(id=store_id)

    def get_store(self):
        return self.__store

    def set_category(self, category):
        self.__category = category

    def get_category(self):
        return self.__category

    def set_type(self, type):
        self.__type = type

    def get_type(self):
        return self.__type

    def set_usage(self, usage):
        self.__usage

    def get_usage(self):
        return self.__usage

    def set_criteria(self, criteria):
        self.__criteria = Criteria.objects.get(id=criteria_id)

    def get_criteria(self):
        return self.__criteria

    def set_location(self, longitude, latitude):
        self.__longitude = longitude
        self.__latitude = latitude
        point = "POINT(%s %s)" % (float(longitude), float(latitude))
        self.__location = geos.fromstr(point)

    def get_location(self):
        return self.__location

    def set_longitude(self, longitude):
        self.__longitude = longitude
        point = "POINT(%s %s)" % (float(longitude), float(self.__latitude))
        self.__location = geos.fromstr(point)

    def get_longitude(self):
        return self.__longitude

    def set_latitude(self, latitude):
        self.__latitude = latitude
        point = "POINT(%s %s)" % (float(self.__longitude), float(latitude))
        self.__location = geos.fromstr(point)

    def get_latitude(self):
        return self.__latitude

    def set_address(self, address_id):
        self.__address = Address.objects.get(id=address_id)

    def get_address(self):
        return self.__address

    def increase_total_read_times(self):
        self.__total_read_times = self.__total_read_times + 1

    def get_total_read_times(self):
        return self.__total_read_times

    '''
    @abstractmethod
    def decrease_allowed_read_times(self):
        pass

    @abstractmethod
    def get_current_allowed_read_times(self):
        pass

    @abstractmethod
    def set_total_scores(self, total_scores, scores_min_scale):
        pass

    @abstractmethod
    def get_current_scores(self):
        pass

    @abstractmethod
    def get_random_scores(self):
        pass

    @abstractmethod
    def set_audio(self, audio):
        pass

    @abstractmethod
    def get_audio(self):
        pass

    @abstractmethod
    def set_image(self, image):
        pass

    @abstractmethod
    def get_image(self):
        pass

    @abstractmethod
    def set_video(self, video):
        pass

    @abstractmethod
    def get_video(self):
        pass

    @abstractmethod
    def set_text(self, text):
        pass

    @abstractmethod
    def get_text(self):
        pass
    '''

    def create_time_utc(self):
        return self.__create_time_utc
    
    '''
    @abstractmethod
    def set_release_expire_time_utc(self, release_expire_time_utc):
        pass

    @abstractmethod
    def get_release_expire_time_utc(self):
        pass

    @abstractmethod
    def is_release_expired(self):
        pass

    @abstractmethod
    def set_usage_expire_time_utc(self, usage_expire_time_utc):
        pass

    @abstractmethod
    def get_usage_expire_date_utc(self):
        pass

    @abstractmethod
    def is_usage_expired(self):
        pass
    '''