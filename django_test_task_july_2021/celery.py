import os

from celery import Celery

from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_test_task_july_2021.settings')

app = Celery('django_test_task_july_2021')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'create_order': {
        'task': 'products.tasks.cancel_pending_orders',
        'schedule': crontab(day_of_week='monday', hour=4, minute=0),
    }
}
