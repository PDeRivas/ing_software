from django.db import models
from django.contrib import admin

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Productos(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField(null = True)
    price = models.DecimalField(max_digits = 12,
                                decimal_places = 2)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
        )
    stock = models.IntegerField(default = 0)

    @admin.display(description = 'Rango de Precios')
    def get_price_range(self):
        if self.price > 90000:
            return 'Alto'
        elif 1600 < self.price < 90000:
            return 'Medio'
        else:
            return 'Bajo' 

    def save(self, *args, **kwargs):
        if self.price>0:
            super().save()
        else:
            print('error')

    def __str__(self):
        return self.name
