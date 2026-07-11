from rest_framework import serializers
from app_order.models import Order
from app_product.models import Product
from app_product.serializers.product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)

    product_ids = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source="product",
        many=True,
        write_only=True,
    )

    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total

    class Meta:
        model = Order
        fields = ["id", "user", "product", "product_ids", "total"]
        read_only_fields = ["id"]
