import pytest

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from api_v1.tests.factories import ProductFactory, CategoryFactory
from productos.models import Productos

def test_first_test():
    assert 3 == 3

@pytest.mark.django_db
def test_list_products(client: APIClient):
    product_1 = ProductFactory()
    product_2 = ProductFactory()

    url = reverse('products-list')
    response = client.get(path=url)

    expected_result = {
        'count': 2,
        'next': None,
        'previous': None,
        'results': [
            {
                'active': True,
                'id': product_1.id,
                'category': {
                    'name': product_1.category.name,
                    'pk': product_1.category.pk,
                    },
                'description': 'No posee descripción',
                'name': product_1.name,
                'price': f'{product_1.price}0',
                'stock': product_1.stock,
            },
            {
                'active': True,
                'id': product_2.id,
                'category': {
                    'name': product_2.category.name,
                    'pk': product_2.category.pk,
                    },
                'description': 'No posee descripción',
                'name': product_2.name,
                'price': f'{product_2.price}0',
                'stock': product_2.stock,
            }
        ]
    }
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_result

@pytest.mark.django_db
def test_detail_products(client: APIClient):
    # Arrange
    product_1 = ProductFactory()
    product_2 = ProductFactory()
    product_3 = ProductFactory()
    product_4 = ProductFactory()

    url = reverse('products-detail', args=(product_2.pk,))
    response = client.get(path=url)

    expected_result = dict(
        active=True,
        name=product_2.name,
        description="No posee descripción",
        stock=0,
        price=f'{product_2.price}0',
        category=dict(
            name=product_2.category.name,
            pk=product_2.category.id
        ),
        id=product_2.id
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_result

@pytest.mark.django_db

def test_delete_products(client: APIClient):

    product_1 = ProductFactory()
    product_2 = ProductFactory()
    product_3 = ProductFactory()
    product_4 = ProductFactory()

    url = reverse('products-detail', args=(product_2.pk,))
    response = client.delete(path=url)

    products = Productos.objects.all()
    assert products.count() == 3
    assert product_2 not in products

@pytest.mark.django_db
def test_create_products(client: APIClient):
    for x in range(10):
        ProductFactory()

    data = {
        "category":{
            'name': 'category test'
        },
        "name":"product test name",
        "price": 1234,
        "stock": 1234,
    }

    url = reverse('products-list')
    response = client.post(
        path=url,
        data=data,
        content_type='application/json'
    )

    assert response.status_code == status.HTTP_201_CREATED

    assert Productos.objects.count() == 11
