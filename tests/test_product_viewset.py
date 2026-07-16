import json
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from app_product.factories import ProductFactory, CategoryFactory
from app_product.models import Product


@pytest.fixture
def client():
    return APIClient()


@pytest.mark.django_db
class TestProductViewSet:

    def test_get_all_products_from_fantasy_universes(self, client):
        cat_tolkien = CategoryFactory(title="Universo de Tolkien")
        cat_witcher = CategoryFactory(title="Universo de The Witcher")
        cat_narnia = CategoryFactory(title="As Crônicas de Nárnia")

        ProductFactory(
            title="O Senhor dos Anéis: A Sociedade do Anel",
            price=59.90,
            category=[cat_tolkien],
        )
        ProductFactory(title="O Último Desejo", price=49.90, category=[cat_witcher])
        ProductFactory(
            title="O Leão, a Feiticeira e o Guarda-Roupa",
            price=39.90,
            category=[cat_narnia],
        )

        url = reverse("product-list", kwargs={"version": "v1"})
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK

        data = response.data

        assert len(data["results"]) == 3
        titles = [product["title"] for product in data["results"]]

        assert "O Senhor dos Anéis: A Sociedade do Anel" in titles
        assert "O Último Desejo" in titles
        assert "O Leão, a Feiticeira e o Guarda-Roupa" in titles

    def test_create_product_of_tolkien(self, client):
        cat_tolkien = CategoryFactory(title="Universo de Tolkien")
        url = reverse("product-list", kwargs={"version": "v1"})

        data = {
            "title": "O Silmarillion",
            "price": "69.90",
            "category_ids": [cat_tolkien.id],
            "active": True,
        }

        response = client.post(
            url, data=json.dumps(data), content_type="application/json"
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["title"] == "O Silmarillion"
        assert Product.objects.filter(title="O Silmarillion").exists()
