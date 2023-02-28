from django.apps import AppConfig
import threading
from scripts import runAll

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    verbose_name = "My Application"
    # def ready(self):
    #     thread = threading.Thread(target=runAll.main)
    #     thread.start()