from user_data.logics.abstract_user_data import AbstractUserData
from user_data.commons import UserDataCategory

class UserLocation(AbstractUserData):
    def __init__(self, database_user_location_instance):
        super(self.__class__, self).__init__(UserDataCategory.LOCATION_DATA, database_user_location_instance)
        self.__location = database_user_location_instance.location
        self.__longitude = database_user_location_instance.longitude
        self.__latitude = database_user_location_instance.latitude
        self.__time_utc = database_user_location_instance.time_utc

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

    def set_time_utc(time_utc):
        self.__time_utc = time_utc

    def get_time_utc(self):
        return self.__time_utc