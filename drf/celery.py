import os
import celeryconfig
from celery import Celery



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf.settings')

app = Celery('drf', broker='redis://redis:6379/0')

app.config_from_object(celeryconfig)

app.autodiscover_tasks()