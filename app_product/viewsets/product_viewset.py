from rest_framework.viewsets import ModelViewSet
from app_product.models import Product
from app_product.serializers.product_serializer import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
