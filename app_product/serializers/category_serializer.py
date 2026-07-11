from rest_framework import serializers
from app_product.models.category import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category

        fields = ["id", "title", "slug", "description", "active"]

        read_only_fields = ["id"]
