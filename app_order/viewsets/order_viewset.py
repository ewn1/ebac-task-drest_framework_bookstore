from rest_framework.viewsets import ModelViewSet
from app_order.models import Order
from app_order.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all()
