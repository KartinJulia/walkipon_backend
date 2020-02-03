from user_authentication.logics.abstract_user import AbstractUser
from user_data.commons import UserDataCategory
from user_data.logics.user_DAO_factory import UserDAOFactory

class PersonalUser(AbstractUser):
    def __init__(self, database_user_instance):
        super(self.__class__, self).__init__(database_user_instance)

    def create_user_current_location(self, data_dictionary):
    	UserDAOFactory.create_data(data_dictionary, UserDataCategory.LOCATION_DATA)

    ############ TODO: add friend ############
    #def add_a_friend(self, user_id)

    ############ TODO: get a friend ##########

    ############ TODO: families or friends shopping together ##############
