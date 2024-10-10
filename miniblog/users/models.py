from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.CharField(
        max_length=30,
        choices=[
            ('es', 'Español'),
            ('en', 'English'),
        ],
        default='es'
        )