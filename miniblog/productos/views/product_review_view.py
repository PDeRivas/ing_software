from django.views import View
from django.shortcuts import render, redirect

from productos.repositories.reviewRepository import ReviewRepository
from productos.repositories.productosRepository import ProductosRepository

class ProductReviewView(View):
    def get(self, request):
        repo = ReviewRepository()
        reviews = repo.get_all()
        
        return render(
            request,
            'product_review/list.html',
            {'reviews': reviews}
        )
    
class ProductReviewCreate(View):
    def get(self, request):
        repo = ProductosRepository()
        products = repo.get_all()
        return render(
            request,
            'product_review/create.html',
            {'products': products},
        )
    
    def post(self, request):
        repo = ReviewRepository()
        id_producto = request.POST.get('id_producto')
        opinion = request.POST.get('opinion')
        rating =  request.POST.get('rating')
        user = request.user
        repo.create(id_producto, user, opinion, rating)
        return redirect('reivew_list')