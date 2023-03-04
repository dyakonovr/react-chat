from django.core.management.base import BaseCommand
from scripts import runAll
import threading

thread = threading.Thread(target=runAll.main)

class Command(BaseCommand):
    def handle(self,*args, **kwargs):
        thread.start()