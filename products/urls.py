from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductModelViewSet, OrderModelViewSet, ReportsView

router = DefaultRouter()
router.register(r'products', ProductModelViewSet)
router.register(r'orders', OrderModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('reports/<str:product>/', ReportsView.as_view(), name='reports')
]
