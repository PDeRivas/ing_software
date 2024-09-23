from decimal import Decimal
import pytest

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from api_v1.tests.factories import ProductFactory

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
                'id': product_1.id,
                'category': None,
                'description': 'No posee descripción',
                'name': product_1.name,
                'price': f'{product_1.price}',
                'stock': product_1.stock,
            },
            {
                'id': product_2.id,
                'category': None,
                'description': 'No posee descripción',
                'name': product_2.name,
                'price': f'{product_2.price}',
                'stock': product_2.stock,
            }
        ]
    }
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_result
