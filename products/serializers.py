from rest_framework import serializers

from .models import Product, Order
from .mixins.serializers import (
    ValidateEnoughQuantityFieldMixin,
    ValidateZeroQuantityFieldMixin,
    LimitChoiceStatusFieldMixin,
)


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(
    LimitChoiceStatusFieldMixin,
    ValidateZeroQuantityFieldMixin,
    ValidateEnoughQuantityFieldMixin,
    serializers.ModelSerializer
):
    product = serializers.SlugRelatedField(slug_field='name', queryset=Product.objects.all())

    class Meta:
        model = Order
        fields = '__all__'


class ReportSerializer(serializers.Serializer):
    product = serializers.CharField()
    currency = serializers.CharField()
    proceeds = serializers.DecimalField(max_digits=14, decimal_places=2)
    profit = serializers.DecimalField(max_digits=14, decimal_places=2)
    amount = serializers.IntegerField()
    refunds = serializers.IntegerField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
