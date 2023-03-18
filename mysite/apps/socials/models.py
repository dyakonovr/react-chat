from django.db import models
from apps.authentication.models import Registered_user


class Soc_vars(models.Model):
    registered_id = models.OneToOneField(Registered_user, on_delete=models.CASCADE, primary_key=True)
    vk_api_token = models.TextField(unique=True, null=True)
    green_api_id = models.TextField(unique=True)
    green_api_token = models.TextField(unique=True)
    telegram_session_path = models.TextField(unique=True)
