from .shop_type import Computer
from .abstractshop import AbstractShop
from .errors import NonProductError


class ComputerShop(AbstractShop):
    def __init__(self):
        self._products = []

    @staticmethod
    def is_valid(product: Computer):
        """ Проверка типа передаваемых дынных """
        if not (isinstance(product, Computer)):
            raise NonProductError(f'"представленный {product}" - не комплектующее компьютера!')

    def add_product(self, product: Computer):
        """ Добавление нового товара"""
        self.is_valid(product)
        return self._products.append(product)

    def sell_product(self, product: Computer):
        """ Продажа товара """
        self.is_valid(product)
        self._products.remove(product)
        return self._products

    def all_products(self):
        """ Перечень всех товаров """
        return self._products
