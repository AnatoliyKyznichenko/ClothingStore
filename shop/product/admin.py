from django.contrib import admin
from product.models import ProductCategory, Product

admin.site.register(ProductCategory)
admin.site.register(Product)