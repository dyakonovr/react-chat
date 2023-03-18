from django.db import models
from django.contrib.auth.models import AbstractUser


class Registered_user(AbstractUser):
    registered_id = models.IntegerField(
        primary_key=True, auto_created=True)
    username = models.CharField(max_length=319, unique=True, error_messages={
                                'unique': "This username has already been registered."})
    password = models.CharField(max_length=255, unique=False)
    email = models.EmailField(unique=True, error_messages={
                              'unique': "This email has already been registered."})
    phone = models.CharField(max_length=255, unique=True, error_messages={
        'unique': "This phone number has already been registered."})
    first_name = None
    last_name = None
