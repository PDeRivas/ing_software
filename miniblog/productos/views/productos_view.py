# Create your views here.
from django.shortcuts import render, redirect

from productos.repositories.productosRepository import ProductosRepository
from django.contrib.auth.decorators import login_required
from productos.forms import ProductForm

repo = ProductosRepository()

def product_list(request):
    products = repo.get_all()
    return render(
        request,
        'product/list.html',
        {
            'productos': products,
        }
    )

@login_required(login_url='login')
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            producto_nuevo = repo.create(
                nombre = form.cleaned_data['name'],
                precio = form.cleaned_data['price'],
                descripcion = form.cleaned_data['description'],
                cantidad = form.cleaned_data['stock'],
                categoria = form.cleaned_data['category'],
            )
            return redirect(
                'product_list',
                )

    form = ProductForm()
    return render(
        request,
        'product/create.html',
        {'form': form}
    )

def product_detail(request, id:int):
    producto = repo.get_by_id(id=id)
    return render(
        request,
        'product/detail.html',
        {'producto': producto}
    )

@login_required(login_url='login')
def product_delete(request, id:int):
    producto = repo.get_by_id(id=id)
    repo.delete(producto=producto)
    return redirect(product_list)

@login_required(login_url='login')
def product_update(request, id:int):
    product = repo.get_by_id(id=id)
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        number = request.POST.get('price')
        category_id = request.POST.get('category')
        category = repo.get_category_by_id(category_id=category_id)
        stock = request.POST.get('stock')

        repo.update(
            producto = product,
            nombre = name,
            precio = number,
            descripcion = description,
            categoria = category,
            cantidad = stock
        )

        return redirect(
            'product_detail',
            product.id
        )
    
    categorias = repo.get_all_categories()
    return render(
        request,
        'product/update.html',
        {'product': product,
         'categories': categorias}
    )
