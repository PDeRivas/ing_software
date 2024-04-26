# Create your views here.
from django.shortcuts import render, redirect

from productos.repositories.productosRepository import ProductosRepository

repository = ProductosRepository()

def product_list(request):
    products = repository.get_all()
    return render(
        request,
        'product/list.html',
        dict(
            productos = products,
        )
    )

def product_create(request):
    ...

def product_detail(request, id:int):
    producto = repository.get_by_id(id=id)
    return render(request, 'product/detail.html', dict(producto = producto))

def product_delete(request, id):
    repository.delete_by_id(id=id)
    return redirect(product_list)

def product_update(request, id):
    ...
