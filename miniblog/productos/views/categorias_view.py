from django.views import View
from django.shortcuts import render, redirect

from productos.repositories.categoriasRepository import CategoriasRepository
from django.contrib.auth.decorators import login_required

repo = CategoriasRepository()

class CategoryView(View):
    def get(self, request):
        repo = CategoriasRepository()
        categorias = repo.get_all()

        return render(
            request,
            'category/list.html',
            {
                'categories': categorias,
            }
        )

class CategoryCreate(View):
    def get(self, request):
        return render(
            request,
            'category/create.html'
        )
    
    def post(self, request):
        repo = CategoriasRepository()
        name = request.POST.get('name')
        newCategory = repo.create(nombre=name)

        newCategoryId = newCategory.id

        return redirect('category_detail', newCategoryId)

class CategoryDetail(View):
    def get(self, request, id):
        repo = CategoriasRepository()
        categoria = repo.get_by_id(id=id)

        return render(
            request,
            'category/detail.html',
            {
                'category': categoria,
            }
        )

class CategoryDelete(View):
    def get(self, request, id):
        repo = CategoriasRepository()
        categoria = repo.get_by_id(id=id)
        repo.delete(categoria=categoria)
        return redirect('category_list')

class CategoryUpdate(View):
    def get(self, request, id):
        repo = CategoriasRepository()
        categoria = repo.get_by_id(id)

        return render(
            request,
            'category/update.html',
            {
                'category': categoria,
            }
        )
    
    def post(self, request, id):
        repo = CategoriasRepository()

        categoria = repo.get_by_id(id)
        name = request.POST.get('name')
        repo.update(categoria=categoria,
                    nombre=name)

        return redirect('category_detail', id)
