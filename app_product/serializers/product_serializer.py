from rest_framework import serializers
from app_product.models.product import Product
from app_product.serializers.category_serializer import CategorySerializer
from app_product.models.category import Category


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)

    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        many=True,
        write_only=True,
    )

    class Meta:
        model = Product

        fields = [
            "id",
            "title",
            "description",
            "price",
            "active",
            "category",
            "category_ids",
        ]

        read_only_fields = ["id"]
