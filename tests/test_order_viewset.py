import json
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from app_product.factories import ProductFactory, CategoryFactory
from app_order.factories import OrderFactory, UserFactory
from app_order.models import Order
from rest_framework.authtoken.models import Token


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def authenticated_user():
    return UserFactory(username="usuario_logado")


@pytest.fixture
def authenticated_client(authenticated_user):
    client = APIClient()
    token = Token.objects.create(user=authenticated_user)
    client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
    return client


@pytest.mark.django_db
class TestOrderViewSet:

    def test_get_orders_list(self, authenticated_client, authenticated_user):
        cat_tolkien = CategoryFactory(title="Universo de Tolkien")

        book_1 = ProductFactory(title="O Hobbit", price=45.00, category=[cat_tolkien])
        book_2 = ProductFactory(
            title="As Duas Torres", price=55.00, category=[cat_tolkien]
        )

        order = OrderFactory(user=authenticated_user)
        order.product.set([book_1, book_2])

        url = reverse("order-list", kwargs={"version": "v1"})
        response = authenticated_client.get(url)

        assert response.status_code == status.HTTP_200_OK

        data = response.data

        assert len(data["results"]) == 1
        assert data["results"][0]["user"] == authenticated_user.id

    def test_create_order_with_witcher_and_narnia_books(
        self, authenticated_client, authenticated_user
    ):
        cat_fantasia = CategoryFactory(title="Fantasia")

        book_1 = ProductFactory(
            title="O Sangue dos Elfos", price=50.00, category=[cat_fantasia]
        )
        book_2 = ProductFactory(
            title="O Príncipe Caspian", price=40.00, category=[cat_fantasia]
        )

        url = reverse("order-list", kwargs={"version": "v1"})

        data = {"user": authenticated_user.id, "product_ids": [book_1.id, book_2.id]}

        response = authenticated_client.post(
            url, data=json.dumps(data), content_type="application/json"
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert Order.objects.filter(user=authenticated_user).exists()
        assert float(response.data["total"]) == 90.00
