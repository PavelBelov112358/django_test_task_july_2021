from datetime import datetime

import pytz
from django.conf import settings
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from .mixins.views import CreateListModelMixin
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer, ReportSerializer
from .services import reports


class ProductListModelViewSet(CreateListModelMixin, ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderListModelViewSet(CreateListModelMixin, ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ReportsView(ListAPIView):
    serializer_class = ReportSerializer

    def get_queryset(self):
        selected_date = self.request.query_params.get('date')
        limit_day = datetime.strptime(selected_date, '%m-%d-%Y')\
            if selected_date\
            else datetime(year=1970, month=1, day=1, tzinfo=pytz.timezone(settings.TIME_ZONE))

        self.queryset = reports.get_reports(limit_day)
        queryset = super(ReportsView, self).get_queryset()

        queryset = reports.replace_none_to_0(queryset)

        return queryset
