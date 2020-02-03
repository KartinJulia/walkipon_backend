from enum import Enum
from django.conf import settings


class UserDataCategory(Enum):
    LOCATION_DATA = 'location_data'
    COUPON_DATA = 'coupon_data'
    SCORE_DATA = 'score_data'
