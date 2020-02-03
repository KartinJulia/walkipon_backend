import datetime
from message.logics.abstract_message import AbstractMessage
from message.logics.time_limited_message import TimeLimitedMessage
from message.logics.score_limited_message import ScoreLimitedMessage

class Message(AbstractMessage):
    def __init__(self, database_message_instance):
        super(self.__class__, self).__init__(database_message_instance)
        
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

    def set_video(self, video):
        self.__video = video

    def get_video(self):
        return self.__video

    def set_text(self, text):
        self.__text = text

    def get_text(self):
        return self.__text