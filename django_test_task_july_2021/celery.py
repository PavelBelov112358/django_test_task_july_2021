import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_test_task_july_2021.settings')

app = Celery('products_schedule')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'cancel_pending_orders': {
        'task': 'products.tasks.cancel_pending_orders',
        'schedule': crontab(minute=0, hour='*/1'),
    }
}
