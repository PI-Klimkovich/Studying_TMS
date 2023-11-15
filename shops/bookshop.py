from .shop_type import BookEditions
from .abstractshop import AbstractShop
from .errors import NonProductError


class BookShop(AbstractShop):
    def __init__(self):
        self._products = []

    @staticmethod
    def is_valid(product: BookEditions):
        """ Проверка типа передаваемых дынных """
        if not (isinstance(product, BookEditions)):
            raise NonProductError(f'"представленный {product}" - не книжное издание!')

    def add_product(self, product: BookEditions):
        """ Добавление нового товара"""
        self.is_valid(product)
        return self._products.append(product)

    def sell_product(self, product: BookEditions):
        """ Продажа товара """
        self.is_valid(product)
        self._products.remove(product)
        return self._products

    def all_products(self):
        """ Перечень всех товаров """
        return self._products
