from message.logics.abstract_message import AbstractMessage
from message.logics.time_limited_message import TimeLimitedMessage

class CouponMessage(TimeLimitedMessage):
    """
    User can post a message with text and image
    """
    def __init__(self, database_message_instance):
        """Constructor
        """
        #super(self.__class__, self).__init__(database_message_instance)
        super().__init__(database_message_instance)
        #self.__title = database_message_instance.title
        self.__text = database_message_instance.text
        self.__image = database_message_instance.image
        #self.__until_at_utc = database_message_instance.until_at_utc

    '''
    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title
    '''
    

    def set_text(self, text):
        self.__text = text

    def get_text(self):
        return self.__text
    
    def set_image(self, image):
        """Set Image
        Set image object to database.
        """
        self.__image = image

    def get_image(self):
        """Get Image
        Get image's URL.
        """
        return self.__image

    #def set_until_at_utc(self, until_at_utc):
    #    self.__until_at_utc = until_at_utc

    #def get_until_at_utc(self):
    #    return self.__until_at_utc
