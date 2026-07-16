from rest_framework.viewsets import ModelViewSet
from app_order.models import Order
from app_order.serializers import OrderSerializer
from app_order.pagination import OrderPagination


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    pagination_class = OrderPagination

    def get_queryset(self):
        return Order.objects.all()
