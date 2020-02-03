from user_authentication.logics.abstract_user import AbstractUser
from message.logics.message_DAO_factory import MessageDAOFactory
from message.commons import MessageType, MessageSearchIdentifier

class CommericalUser(AbstractUser):
    def __init__(self, database_user_instance):
        super(self.__class__, self).__init__(database_user_instance)

    def create_coupon_message(self, data_dictionary):
        MessageDAOFactory.create_message(data_dictionary, MessageType.COUPON_MESSAGE.value)

    def update_coupon_message(self, message_id, data_dictionary):
        logic_message = MessageDAOFactory.get_logic_message(message_id, MessageType.COUPON_MESSAGE.value)
        if logic_message.get_type() != MessageType.COUPON_MESSAGE.value:
            raise ValueError('Method not allow.')
        MessageDAOFactory.update_message(data_dictionary, logic_message, MessageType.COUPON_MESSAGE.value)

    def get_message_overview_json(self, offset, limit, message_type=None):
        return MessageDAOFactory.get_messages_overview_json_by_user(self._AbstractUser__user_id, offset, limit, message_type)

    def get_message_detail_json(self, offset, limit, message_type=None):
        return MessageDAOFactory.get_messages_detail_json_by_user(self._AbstractUser__user_id, offset, limit, message_type)
