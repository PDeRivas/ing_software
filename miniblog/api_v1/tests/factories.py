import factory

from factory.django import DjangoModelFactory

from productos.models import Productos, Category

class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Productos
    
    name = factory.Sequence(lambda n: 'Product_%d' %n)
    price = factory.Faker('pyfloat', left_digits=2, right_digits=1, positive=True)
    category = factory.SubFactory(CategoryFactory)
