from enum import Enum
from django.conf import settings


class MessageCategory(Enum):
    ADVERTISEMENT_MESSAGE = 'AD'
    COUPON_MESSAGE = 'CU'
    ENCOUNTER_MESSAGE = 'EN'
    EVENT_MESSAGE = 'EV'
    GRAFFITI_MESSAGE = 'GM'
    MUSIC_MESSAGE = 'MM'
    TEXT_IMAGE_COMMENT = 'TI'
    VIDEO_MESSAGE = 'VM'
    VOICE_COMMENT = 'VC'
    VOICE_MESSAGE = 'VO'


class MessageSearchIdentifier(Enum):
    AUTHOR_ID = 'author_id'
    LOCATION = 'location'


#def upload_file_handler(self, file, filename):
#    print filename
#    with open((settings.MEDIA_ROOT)+str(filename), 'wb+') as destination:
#        for chunk in file.chunks():
#            destination.write(chunk)
#        destination.close()
