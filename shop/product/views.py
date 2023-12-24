from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from product.models import ProductCategory, Product


# Create your views here.

class HelloWorldView(View):
    template_name = 'product/main.html'

    def get(self, request):
        return render(request, self.template_name)


class ProductCategoryShop(View):
    model = ProductCategory
    template_name = 'product/category_shop.html'

    def get(self, request):
        categories = ProductCategory.objects.all()
        print(categories)
        return render(request, self.template_name, {'categories': categories})


class ProductShop(View):
    template_name = 'product/product_shop.html'  # Название вашего шаблона

    def get(self, request, category_name):
        # Получаем категорию
        category = get_object_or_404(ProductCategory, name=category_name)

        # Получаем все товары в выбранной категории
        products = Product.objects.filter(category=category)

        # Передаем категорию и товары в контекст для отображения в шаблоне
        context = {'category': category, 'products': products}
        return render(request, self.template_name, context)







