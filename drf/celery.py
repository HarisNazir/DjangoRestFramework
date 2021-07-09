from celery import Celery

app = Celery('drf', broker='amqp://guest@localhost//')