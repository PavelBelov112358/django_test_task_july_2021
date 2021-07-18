from datetime import datetime

from django.db.models import Sum, Q, F

from products.models import Product
from ..choices import OrderStatus


def get_reports(limit_date: datetime) -> list[dict]:
    completed = Sum(
        'orders__quantity',
        filter=Q(
            name=F('name'),
            orders__created_at__gte=limit_date,
            orders__status=OrderStatus.COMPLETED,
        )
    )
    refunded = Sum(
        'orders__quantity',
        filter=Q(
            name=F('name'),
            orders__created_at__gte=limit_date,
            orders__status=OrderStatus.REFUNDED,
        )
    )
    res = Product.objects\
        .annotate(
            product=F('name'),
            currency=F('cost_currency'),
            proceeds=(completed - refunded) * F('cost'),
            profit=(completed - refunded) * (F('cost') - F('self_cost')),
            amount=completed - refunded,
            refunds=refunded,
        )\
        .values(
            'product',
            'currency',
            'proceeds',
            'profit',
            'amount',
            'refunds',
        )
    return res


def replace_none_to_0(queryset: list[dict]) -> list[dict]:
    for item in queryset:
        for key, value in item.items():
            item[key] = value if value is not None else 0
    return queryset
