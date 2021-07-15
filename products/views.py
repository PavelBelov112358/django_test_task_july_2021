from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer
from .services.reports import get_report


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderModelViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ReportsView(APIView):

    def get(self, *args, **kwargs):
        response = get_report(self.kwargs.get('product'))
        for key, value in response.items():
            response[key] = value if value is not None else 0
        return Response(response)
