import pytest
from app_product.factories import CategoryFactory
from app_product.serializers.category_serializer import CategorySerializer

pytestmark = pytest.mark.django_db


def test_category_serializer_fields_output():
    category = CategoryFactory(
        title="Contos de Valinor",
        slug="contos-de-valinor",
        description="Livros que narram os dias antigos dos Elfos na terra abençoada.",
        active=True,
    )

    serializer = CategorySerializer(category)
    data = serializer.data

    assert data["id"] == category.id
    assert data["title"] == "Contos de Valinor"
    assert data["slug"] == "contos-de-valinor"
    assert (
        data["description"]
        == "Livros que narram os dias antigos dos Elfos na terra abençoada."
    )
    assert data["active"] is True


def test_category_serializer_validation():
    payload = {
        "title": "Poesia Épica",
        "slug": "poesia-epica",
        "description": "Baladas e poemas rimados da Primeira Era.",
        "active": True,
    }

    serializer = CategorySerializer(data=payload)

    assert serializer.is_valid() is True

    nova_categoria = serializer.save()
    assert nova_categoria.title == "Poesia Épica"
    assert nova_categoria.slug == "poesia-epica"
