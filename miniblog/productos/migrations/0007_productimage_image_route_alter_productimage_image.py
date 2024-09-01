# Generated by Django 5.1 on 2024-08-30 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_supplier_pricehistory_productimage_productreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='image_route',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(null=True, upload_to='product_images/'),
        ),
    ]