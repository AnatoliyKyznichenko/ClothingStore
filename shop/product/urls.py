from django.urls import path
from .views import HelloWorldView, ProductCategoryShop, ProductShop

app_name = 'product'

urlpatterns = [
    path('', HelloWorldView.as_view(), name='index'),
    path('product/', ProductCategoryShop.as_view(), name='products_many'),
    path('product/<str:category_name>/', ProductShop.as_view(), name='products_shop'),
]