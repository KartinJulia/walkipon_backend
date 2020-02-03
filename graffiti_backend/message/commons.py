from enum import Enum
from django.conf import settings


class MessageCategory(Enum):
    TIME_LIMITED = 'time_limited'
    SCORE_LIMITED = 'score_limited'

class MessageType(Enum):
    ADVERTISEMENT_MESSAGE = 'advertisement_message'
    COUPON_MESSAGE = 'coupon_message'
    #ENCOUNTER_MESSAGE = 'encounter_message'
    EVENT_MESSAGE = 'event_message'
    #GRAFFITI_MESSAGE = 'graffiti_message'


class MessageSearchIdentifier(Enum):
    AUTHOR_ID = 'author_id'
    LOCATION = 'location'


#def upload_file_handler(self, file, filename):
#    print filename
#    with open((settings.MEDIA_ROOT)+str(filename), 'wb+') as destination:
#        for chunk in file.chunks():
#            destination.write(chunk)
#        destination.close()
