from django.urls import path

from productos.views import (
    product_list,
    product_create,
    product_delete,
    product_detail,
    product_update,
    )

urlpatterns = [
    path(route='', view=product_list, name='product_list'),
    path(route='create/', view=product_create, name='product_create'),
    path(route='<int:id>/delete/', view=product_delete, name='product_delete'),
    path(route='<int:id>/detail/', view=product_detail, name='product_detail'),
    path(route='<int:id>/update/', view=product_update, name='product_update'),
]