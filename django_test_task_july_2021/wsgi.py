import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_test_task_july_2021.settings')

application = get_wsgi_application()
