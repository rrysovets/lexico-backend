import os
import time
from celery import Celery
from django.conf import settings



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.config.settings')

app = Celery('celery_app',broker='redis://redis:6379/0')

app.config_from_object('django.conf:settings')


app.conf.broker_url = settings.CELERY_BROKER_URL


app.autodiscover_tasks()



