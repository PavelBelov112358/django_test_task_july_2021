from django.db import models
from djmoney.models.fields import MoneyField
from django.conf import settings
from .choices import OrderStatus


class Product(models.Model):
    name = models.CharField(max_length=50)
    self_cost = MoneyField(max_digits=14, decimal_places=2, default_currency=settings.DEFAULT_CURRENCY)
    cost = MoneyField(max_digits=14, decimal_places=2, default_currency=settings.DEFAULT_CURRENCY)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=OrderStatus.choices, default=OrderStatus.PENDING)

    def __str__(self):
        return f'{self.product} - {self.quantity}'
