from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from product.models import Product
from cart.user_cart import Cart
from django.http import JsonResponse


class BasketAddCart(View):
    def get(self, request, product_id):
        # Логика для обработки POST-запроса
        product = get_object_or_404(Product, id=product_id)
        cart = Cart(request)
        cart.add_product(product)
        cart.save()
        current_url = request.META.get('HTTP_REFERER', '/')
        return redirect(current_url)


class UserCart(View):
    template_name = 'cart/basket.html'

    def get(self, request):
        cart = Cart(request)
        context = {'cart_info': cart}
        return render(request, self.template_name, context)
