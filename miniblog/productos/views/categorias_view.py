from django.shortcuts import render, redirect

from productos.repositories.categoriasRepository import CategoriasRepository

repo = CategoriasRepository

def category_list(request):
    categorias = repo.get_all()
    return render(
        request,
        'categories/list.html',
        {
            'categories': categorias
        },
    )