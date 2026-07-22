from rest_framework.viewsets import ModelViewSet
from app_order.models import Order
from app_order.serializers import OrderSerializer
from app_order.pagination import OrderPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    pagination_class = OrderPagination
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by("-id")
