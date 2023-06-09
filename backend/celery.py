from celery import Celery
from . import celery_config
import os
from django.conf import settings

os.environ.setdefault('DJANAGO_SETTINGS_MODULE', 'backend.settings')

app = Celery('backend')

app.config_from_object(celery_config)

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)