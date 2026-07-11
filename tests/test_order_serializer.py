import pytest
from django.contrib.auth.models import User
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


def test_order_serializer_creation_with_product_ids():
    comprador = User.objects.create_user(username="frodo_bolseiro")
    livro_1 = ProductFactory(title="O Retorno do Rei", price=79.90)
    livro_2 = ProductFactory(title="As Duas Torres", price=79.90)

    payload = {
        "user": comprador.id,
        "product_ids": [livro_1.id, livro_2.id],
    }

    serializer = OrderSerializer(data=payload)

    assert serializer.is_valid() is True

    order = serializer.save()

    assert order.user == comprador
    assert order.product.count() == 2
    assert float(OrderSerializer(order).data["total"]) == 159.80
