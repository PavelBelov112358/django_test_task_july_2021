from datetime import datetime, timedelta, timezone

from celery import shared_task

from .models import Order
from .choices import OrderStatus


@shared_task
def cancel_pending_orders():
    time_step = datetime.now(tz=timezone.utc) - timedelta(weeks=1, hours=1)
    Order.objects.filter(status=OrderStatus.PENDING, created_at__gte=time_step).update(status=OrderStatus.CANCELED)
    return 'cancel_pending_orders'
