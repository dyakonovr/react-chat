from django.apps import AppConfig
import threading
from scripts import runAll


class ChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.chat'
