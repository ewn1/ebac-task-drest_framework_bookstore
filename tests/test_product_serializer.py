import pytest
from app_product.factories import ProductFactory, CategoryFactory
from app_product.serializers.product_serializer import ProductSerializer

pytestmark = pytest.mark.django_db


def test_product_serializer_fields_output():
    category = CategoryFactory(title="Alta Fantasia", slug="alta-fantasia")
    product = ProductFactory(title="O Silmarillion", price=59.90, category=[category])

    serializer = ProductSerializer(product)
    data = serializer.data

    assert data["id"] == product.id
    assert data["title"] == "O Silmarillion"
    assert float(data["price"]) == 59.90
    assert data["active"] is True
    assert data["category"][0]["title"] == "Alta Fantasia"
    assert data["category"][0]["slug"] == "alta-fantasia"
