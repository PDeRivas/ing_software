from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

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
    
    # FILTROS PERSONALIZADOS CASEROS

    """ 
    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price :
            queryset = queryset.filter(price__lte=max_price)
        if category:
            queryset = queryset.filter(category__name__icontains=category)
        return queryset 
    """

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