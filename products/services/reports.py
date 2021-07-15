from django.db.models import Sum, Q

from products.models import Product
from ..choices import OrderStatus


def get_report(product_name: str) -> dict:
    quantity_completed = Sum('orders__quantity', filter=Q(name=product_name, orders__status=OrderStatus.COMPLETED))
    quantity_refunds = Sum('orders__quantity', filter=Q(name=product_name, orders__status=OrderStatus.REFUND))
    return Product.objects.aggregate(
        proceeds=(quantity_completed * Product.objects.get(name=product_name).cost.amount),
        profit=quantity_completed * (
                Product.objects.get(name=product_name).cost.amount -
                Product.objects.get(name=product_name).self_cost.amount
        ),
        quantity=quantity_completed,
        refunds=quantity_refunds,
    )
