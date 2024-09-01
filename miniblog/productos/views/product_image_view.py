import os
import logging
import tempfile

from productos.forms import ProductImageForm

from django.views import View
from django.shortcuts import render, redirect

from productos.repositories.reviewRepository import ReviewRepository
from productos.repositories.productosRepository import ProductosRepository

from productos.models import ProductImage
from productos.forms import ProductImageForm
from productos.repositories.s3 import S3Repository
logger = logging.getLogger(__name__)

class ProductImageView(View):
    def get(self, request):
        images = ProductImage.objects.all()
        form = ProductImageForm()
        return render(
            request,
            'product_images/list.html',
            {'form': form,
             'images': images,}
        )
    
    def post(self, request):
        s3_repository = S3Repository()
        form = ProductImageForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.cleaned_data['product']
            image = form.cleaned_data['image']
            description = form.cleaned_data['description']
            image_route = form.cleaned_data['image_route']

            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                for chunk in image.chunks():
                    temp_file.write(chunk)
                    temp_file_path = temp_file.name

                    imagen_object = ProductImage.objects.create(
                        product = product,
                        image = image,
                        description = description,
                        image_route = image_route
                    )
                    imagen_object.save
                    nombre_imagen = f'imagen_producto_{imagen_object.id}'
                    s3_repository.upload_file(
                        temp_file_path,
                        'ingsoftwareitec',
                        nombre_imagen,
                    )

        return redirect('image_list')
