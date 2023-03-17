from celery.schedules import crontab
from django.conf import settings
from datetime import timedelta

broker_url = settings.BROKER_URL
accept_content = ['json']

beat_schedule = {
        'fetch_video_data': {
            'task': 'api.tasks.fetch_coin_market_data',
            'schedule': timedelta(seconds=5),
        }
    }