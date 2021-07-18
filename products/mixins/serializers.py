from django.db.models import Sum, Q
from rest_framework.exceptions import ValidationError

from products.choices import OrderStatus
from products.models import Product, Order


class ValidateEnoughQuantityFieldMixin:
    """
    Evaluate that the new total product quantity in all orders doesn't exceed current product quantity
    """

    def validate_quantity(self, quantity):
        product = self.instance.product if self.instance else self.get_initial().get('product')
        method = self._context.get('request')._request.method
        orders_quantity = product_quantity = 0
        quantity_query = Sum('quantity', filter=Q(product__name=product, status=OrderStatus.PENDING))

        if method == 'POST':
            orders_quantity = Order.objects.aggregate(res=quantity_query).get('res')
            product_quantity = Product.objects.get(name=product).quantity

        elif method in ['PUT', 'PATCH']:
            pk = self._context.get('request')._request.resolver_match.kwargs.get('pk')
            orders_quantity = Order.objects.exclude(pk=pk).aggregate(res=quantity_query).get('res')
            product_quantity = Order.objects.get(pk=pk).product.quantity

        orders_quantity = orders_quantity if orders_quantity is not None else 0
        orders_quantity += quantity

        if orders_quantity > product_quantity:
            raise ValidationError(f'Not enough product \'{product}\' in storage')

        return quantity


class ValidateZeroQuantityFieldMixin:
    """
    Evaluate quantity field that it's not equal 0
    """

    def validate_quantity(self, quantity):
        if quantity == 0:
            raise ValidationError("'quantity' shouldn't be 0")
        return super(ValidateZeroQuantityFieldMixin, self).validate_quantity(quantity)


class LimitChoiceStatusFieldMixin:
    """
    Prohibit changing order status field after 'completed', 'canceled' or 'refunded'
    """

    def validate_status(self, status_value):
        current_status = self.instance.status if self.instance else status_value
        if current_status != status_value and \
                current_status in list(filter(lambda i: i != OrderStatus.PENDING, OrderStatus.values)):
            raise ValidationError("'status' can't be changed")
        return status_value
