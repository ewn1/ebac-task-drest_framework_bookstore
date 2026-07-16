from rest_framework.viewsets import ModelViewSet
from app_product.models import Product
from app_product.serializers.product_serializer import ProductSerializer
from app_product.pagination import ProductPagination


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    def get_queryset(self):
        return Product.objects.all()
