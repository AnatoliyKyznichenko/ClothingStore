from decimal import Decimal
from django.conf import settings
from product.models import Product
from user.models import CustomUser


class Cart:
    """request обычно представляет HTTP-запрос, который приходит от клиента (браузера)
    к вашему веб-приложению. Он содержит информацию о запросе,
    такую как HTTP-метод (GET, POST и т.д.), заголовки, параметры запроса, тело запроса и многое другое"""

    def __init__(self, request):
        self.request = request

        """self.request.user предоставляет доступ к объекту пользователя, 
        связанному с текущим запросом. В этом контексте"""
        if self.request.user.is_authenticated:
            self.cart = self.request.user.cart
            if not self.cart:
                self.cart = {}

        else:
            self.session = request.session
            self.cart = self.session.get(settings.CART_SESSION_ID, {})

    def add_product(self, product, quantity=1, update_quantity=False):
        """product: объект продукта, который вы хотите добавить в корзину.
           quantity: количество продукта для добавления в корзину (по умолчанию 1).
           update_quantity: флаг, указывающий, нужно ли обновлять количество продукта в корзине (по умолчанию False)."""
        product_id = str(product.id)
        """Этот идентификатор будет использоваться, например, 
        для проверки наличия товара в корзине или для обновления информации о конкретном товаре в корзине"""

        if product_id not in self.cart:
            """Проверяется, существует ли продукт с данным product_id в корзине
            Если продукта с product_id нет в корзине, то он 
            добавляется в корзину в виде словаря с информацией о продукте"""
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price), 'name': product.name,
                                     'descriptions': product.description}

        if update_quantity:
            self.cart[product_id]['quantity'] = int(quantity)
        else:
            self.cart[product_id]['quantity'] += int(quantity)

    def has_items(self):
        return bool(self.cart)

    def get_cart_content(self):
        return list(self.cart.values())

    def get_cart_content_dict(self):
        return dict(self.cart.items())

    def __str__(self):
        return f"{self.get_cart_content_dict()}"

    def get_cart_content_count(self):
        return len(list(self.cart.values()))

    def save(self):
        if self.request.user.is_authenticated:
            user_ = CustomUser.objects.get(id=self.request.user.id)
            """в данном контексте код пытается найти объект пользователя в базе данных, 
            у которого id совпадает с id текущего пользователя, полученного из self.request.user. 
            Если пользователь аутентифицирован и имеет id, 
            эта строка кода будет искать соответствующий объект в базе данных и возвращает его"""
            user_.cart = self.cart
            user_.save()
        else:
            self.session[settings.CART_SESSION_ID] = self.cart
            self.session.save()

    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """Перелік елементів у корзині та отримання продуктів з бази даних."""
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """Підрахувати кількість товарів у корзині."""
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """Підрахувати вартість товарів у корзині."""
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """Метод для очищення сесії корзини."""
        del self.session[settings.CART_SESSION_ID]
        self.session.save()
