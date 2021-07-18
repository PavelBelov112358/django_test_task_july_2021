from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ProductListModelViewSet,
    OrderListModelViewSet,
    ReportsView,
)

router = DefaultRouter()
router.register(r'products', ProductListModelViewSet)
router.register(r'orders', OrderListModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('reports/', ReportsView.as_view(), name='reports'),
]
