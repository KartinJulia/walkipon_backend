from message_app.logics.abstract_message import AbstractMessage
from message_app.models.address import Address

class EventMessage(AbstractMessage):
    """
    User can post a message with text and image
    """
    def __init__(self, database_message_instance):
        """Constructor
        """
        super(self.__class__, self).__init__(database_message_instance)
        self.__title = database_message_instance.title
        self.__total_read_times = database_message_instance.total_read_times
        self.__total_liked_times = database_message_instance.total_liked_times
        self.__image = database_message_instance.image
        self.__video = database_message_instance.video
        self.__text = database_message_instance.text
        self.__until_at_utc = database_message_instance.until_at_utc

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_address(self, address_id):
        self.__address = Address.objects.get(id=address_id)

    def get_address(self):
        return self.__address

    def increase_total_read_times(self):
        self.__total_read_times = self.__total_read_times + 1

    def get_total_read_times(self):
        return self.__total_read_times

    def increase_total_liked_times(self):
        self.__total_liked_times = self.__total_liked_times + 1

    def get_total_liked_times(self):
        return self.__total_liked_times

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
        """Set Video
        Set video object to database.
        """
        self.__video = video

    def get_video(self):
        """Get Video
        Get image's URL.
        """
        return self.__video

    def set_text(self, text):
        self.__text = text

    def get_text(self):
        return self.__text

    def set_until_at_utc(self, until_at_utc):
        self.__until_at_utc = until_at_utc

    def get_until_at_utc(self):
        return self.__until_at_utc
