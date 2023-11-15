from .shop_type import Furniture
from .abstractshop import AbstractShop
from .errors import NonProductError


class FurnitureShop(AbstractShop):
    def __init__(self):
        self._products = []

    @staticmethod
    def is_valid(product: Furniture):
        """ Проверка типа передаваемых дынных """
        if not (isinstance(product, Furniture)):
            raise NonProductError(f'"представленный {product}" - не мебель!')

    def add_product(self, product: Furniture):
        """ Добавление нового товара"""
        self.is_valid(product)
        return self._products.append(product)

    def sell_product(self, product: Furniture):
        """ Продажа товара """
        self.is_valid(product)
        self._products.remove(product)
        return self._products

    def all_products(self):
        """ Перечень всех товаров """
        return self._products
