import pytest

from django.urls import reverse

def test_first_test():
    assert 3 == 2

def test_list_products(client: APIClient):
    url = reverse('product_list')
    response = client.get(path=url)