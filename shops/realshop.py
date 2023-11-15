from .product import Product
from .abstractshop import AbstractShop
from .errors import NonProductError


class RealShop(AbstractShop):
    def __init__(self):
        self._products = []

    @staticmethod
    def is_valid(product: Product):
        """ Проверка типа передаваемых дынных """
        if not (isinstance(product, Product)):
            raise NonProductError(f'"{product}" - не является продуктом!')

    def add_product(self, product: Product):
        """ Добавление нового товара"""
        self.is_valid(product)
        return self._products.append(product)

    def sell_product(self, product: Product):
        """ Продажа товара """
        self.is_valid(product)
        self._products.remove(product)
        return self._products

    def all_products(self):
        """ Перечень всех товаров """
        return self._products
