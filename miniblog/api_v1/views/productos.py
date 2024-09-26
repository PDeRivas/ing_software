import csv
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

from django.http import HttpResponse

from api_v1.filters import ProductFilter
from api_v1.serializers.product_serializer import ProductSerializer
from productos.models import Category, Productos


class ProducViewSet(ModelViewSet):
    # GET(LIST); POST(CERATE); PUT(UPDATE); PATCH(PARTIAL UPDATE); DELETE(DESTROY) Y UN DETAIL(RETRIEVE)
    queryset = Productos.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'stock', 'category__name']
    filterset_class = ProductFilter

    def create(self, request, *args, **kwargs):
        # Extraemos los datos de la peticion
        data = request.data

        # Extraemos o creamos la categoria
        category_data = data.get('category')
        category_name = category_data.get('name')
        category, created = Category.objects.get_or_create(
            name=category_name
            )
    
        # Creamos el producto
        product = Productos.objects.create(
            name=data.get('name'),
            description=data.get('description', None),
            price=data.get('price'),
            stock=data.get('stock'),
            active=data.get('active', True),
            category=category or None
        )

        serializer = self.serializer_class(product)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=['get'], detail=False, url_path='download_csv')
    def download_csv(self, request):
        categoria = request.query_params.get('category', None)

        response = HttpResponse(content_type = 'text/csv')
        response['Content-Disposition'] = 'attachment; filename="products.csv"'
        
        writer = csv.writer(response)
        writer.writerow(
            [
                'Nombre', 'Descripción', 'Precio', 'Categoría', 'Stock'
            ]
        )
        products = self.get_queryset()
        
        if categoria:
            products = products.filter(category__name = categoria)

        for product in products:
            writer.writerow(
                [
                    product.name,
                    product.description,
                    product.price,
                    product.category.name if product.category else 'No posee',
                    product.stock,
                ]
            )
        return response

    @action(methods=['get'], detail=False, url_path='download_price_stock_csv')
    def download_price_stock(self, request):
        response = HttpResponse(content_type = 'text/csv')
        response['Content-Disposition'] = 'attachment; filename="price_stock.csv"'
        
        writer = csv.writer(response)
        writer.writerow(
            [
                'Nombre', 'Precio', 'Cantidad', 'Valor Total'
            ]
        )

        for product in self.get_queryset():
            writer.writerow(
                [
                    product.name,
                    product.price,
                    product.stock,
                    product.price * product.stock,
                ]
            )
        return response
    
    @action(methods=['get'], detail=False, url_path='latest_product')
    def latest_product(self, request):
        last_product = self.get_queryset().last()
        serializer = self.serializer_class(last_product)
        return Response(serializer.data)
