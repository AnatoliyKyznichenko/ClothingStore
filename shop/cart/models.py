from django.db import models
from product.models import Product
from user.models import CustomUser


class Basket(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Корзина для {self.user.email} | Продукт: {self.product.name}'
