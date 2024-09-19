import django_filters

from productos.models import Productos

class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(
        field_name='category__name',
        lookup_expr='icontains'
    )

    class Meta:
        model = Productos
        fields = ['category',]