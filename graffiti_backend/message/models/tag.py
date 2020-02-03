from django.db import models
#from message_app.models.message import Message

class Tag(models.Model):
    tag = models.CharField(max_length=30)
    messages = models.ManyToManyField('message_app.Message')
