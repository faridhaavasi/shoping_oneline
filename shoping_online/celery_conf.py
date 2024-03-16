from celery import Celery
from datetime import timedelta
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shoping_online.settings')

app_celery = Celery('shoping_online')
app_celery.autodiscover_tasks()

app_celery.conf.broker_url = 'redis://redis'
app_celery.conf.result_backend = 'redis://redis'
app_celery.conf.task_serializer = 'json'
app_celery.conf.result_serializer = 'pickle'
app_celery.conf.accept_content = ['json', 'pickle']
app_celery.conf.result_expires = timedelta(days=1)
app_celery.conf.task_always_eager = False
app_celery.conf.worker_prefetch_multiplier = 4
