from django.urls import path
from .views import BasketAddCart, UserCart

app_name = 'cart'

urlpatterns = [
    path('add_to_cart/<int:product_id>/', BasketAddCart.as_view(), name='add_to_cart'),
    path('user_cart/', UserCart.as_view(), name='get_user_cart'),

]