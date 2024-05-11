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

def category_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        repo.create(name = name)

        return redirect(
            'category_list'
        )
    
    return render(
        request,
        'categories/create.html',
    )

def category_delete(request, id:int):
    categoria = repo.get_by_id(id=id)
    repo.delete(categoria)
    return redirect(category_list)

def category_update(request, id:int):
    categoria = repo.get_by_id(id=id)
    if request.method == "POST":
        name = request.POST.get('name')
        repo.update(categoria, name)
        return redirect(
            category_details,
            categoria.id
        )
    
    return render(
        request,
        'categories/update.html',
        {
            'category': categoria,
        }
    )

def category_details(request, id:int):
    categoria = repo.get_by_id(id=id)

    return render(
        request,
        'categories/detail.html',
        {
            'category': categoria,
        }
    )
