import factory
from app_product.models import Product
from app_product.models import Category


class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("word")
    slug = factory.Faker("slug")
    description = factory.Faker("sentence")

    active = factory.Iterator([True, False])

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.Faker("pydecimal", left_digits=3, right_digits=2, positive=True)
    title = factory.Faker("word")

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.category.add(category)
        else:
            nova_categoria = CategoryFactory()
            self.category.add(nova_categoria)

    class Meta:
        model = Product
