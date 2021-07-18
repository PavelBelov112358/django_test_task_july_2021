from datetime import datetime, timedelta, timezone

from django_test_task_july_2021.celery import app
from .choices import OrderStatus
from .models import Order


@app.task
def cancel_pending_orders() -> str:
    time_filter = datetime.now(tz=timezone.utc) - timedelta(days=1)
    Order.objects.filter(status=OrderStatus.PENDING, created_at__lte=time_filter).update(status=OrderStatus.CANCELED)
    return 'cancel_pending_orders'
