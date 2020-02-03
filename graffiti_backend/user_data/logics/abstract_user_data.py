from django.contrib.gis import geos

class AbstractUserData(object):
	def __init__(self, data_category, database_user_data_instance):
		self.__data_id = database_user_data_instance.id
		self.__data_category = data_category
		self.__user_id = database_user_data_instance.user.id
		self.__database_user_data_instance = database_user_data_instance

	def set_database_user_data_instance(self, data_type, database_user_data_instance):
		self.__data_type = data_type
		self.__user_id = database_user_data_instance.user.id
		self.__database_user_data_instance = database_user_data_instance

	def get_database_user_data_instance(self):
	    return self.__database_user_data_instance

	def data_id(self):
		return self.__data_id

	def user_id(self):
		return self.__user_id

	def set_data_category(self, data_category):
		self.__data_category = data_category

	def get_data_category(self):
		return self.__data_category