from django.contrib import admin

# Register your models here.
from productos.models import(
    Category,
    Productos,
)

@admin.register(Category)
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    ordering = ('name', 'price',)
    search_fields = ('price', 'name',)
    list_filter = ('category',)

    list_display = ('name',
                    'price',
                    'description',
                    'category',
                    )