from django.contrib import admin

from .models import Product, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Product._meta.fields if f.name != 'id']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order'] + [f.name for f in Order._meta.fields if f.name != 'id']

    def order(self, object):
        return object