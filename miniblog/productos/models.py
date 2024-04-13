from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Productos(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    price = models.DecimalField(max_digits = 12,
                                decimal_places = 2)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
        )

    def save(self, *args, **kwargs):
        if self.price>0:
            super().save()
        else:
            print('error')

    