from django.db import models
from apps.authentication.models import Registered_user
class User_in_list(models.Model):
    registered_id = models.ForeignKey(Registered_user, on_delete=models.CASCADE)
    user_id = models.IntegerField(primary_key=True, auto_created=True)
    username = models.TextField()
    from_soc = models.TextField()
    avatar = models.TextField()


class Message(models.Model):
    user_id = models.ForeignKey(User_in_list, on_delete=models.CASCADE)
    message_id = models.IntegerField(primary_key=True, auto_created=True)
    message = models.TextField()
    date = models.DateTimeField()
    media_type = models.TextField()
    media_id = models.IntegerField()
    from_who = models.TextField()

class Media(models.Model):
    media_id = models.ForeignKey(Message, on_delete=models.CASCADE)
    media = models.URLField()