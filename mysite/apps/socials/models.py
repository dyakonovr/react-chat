from django.db import models
from ..authentication.models import User


class SocialsLinks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vk_token = models.CharField(max_length=500, unique=True, null=True)