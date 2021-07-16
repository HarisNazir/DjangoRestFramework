import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf.settings')

app = Celery('drf', broker='amqp://guest@localhost//')

app.autodiscover_tasks()