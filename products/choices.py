from django.db import models
from django.utils.translation import gettext_lazy as _


class OrderStatus(models.TextChoices):
    PENDING = 'pending', _('Pending')
    COMPLETED = 'completed', _('Completed')
    CANCELED = 'canceled', _('Canceled')
    REFUNDED = 'refunded', _('Refunded')
