from django.urls import path, include
from rest_framework import routers
from app_order import viewsets

router = routers.SimpleRouter()

router.register(r"orders", viewsets.OrderViewSet, basename="order")

urlpatterns = [
    path("", include(router.urls)),
]
