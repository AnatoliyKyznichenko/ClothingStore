from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    img = models.ImageField('product_img')
    category = models.ForeignKey(to='ProductCategory', on_delete=models.CASCADE)

    def __str__(self):
        return f'Продукт {self.name}, Категория {self.category}'