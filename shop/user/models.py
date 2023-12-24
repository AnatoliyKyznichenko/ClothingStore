from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    cart = models.JSONField(default=dict, null=True, blank=True)  # Используйте JSONField для хранения корзины в виде словаря


