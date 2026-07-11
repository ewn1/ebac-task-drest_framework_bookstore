import pytest
from app_product.factories import ProductFactory
from app_order.factories import OrderFactory
from app_order.serializers.order_serializer import OrderSerializer

pytestmark = pytest.mark.django_db


def test_order_serializer_calculates_total_correctly():
    product1 = ProductFactory(
        title="O Senhor dos Anéis: A Sociedade do Anel", price=79.90
    )
    product2 = ProductFactory(title="O Hobbit", price=45.00)

    order = OrderFactory(product=[product1, product2])

    serializer = OrderSerializer(order)
    data = serializer.data

    assert float(data["total"]) == 124.90
    assert data["id"] == order.id
    assert data["user"] == order.user.id
