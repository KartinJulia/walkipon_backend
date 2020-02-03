from django.conf import settings
from django.db import models
from user_authentication.models.user import User
from message.models.message import Message

class UserCoupon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coupon_message = models.ForeignKey(Message, on_delete=models.CASCADE)
    available_status = models.BooleanField(default=True)

    #TODO: user usage infomation record for later data analysis.