from abc import ABC, abstractmethod
from .product import Product


class AbstractShop(ABC):
    @abstractmethod
    def add_product(self, product: Product):
        """ Добавление нового товара"""

    @abstractmethod
    def sell_product(self, product: Product):
        """ Продажа товара """

    @abstractmethod
    def all_products(self):
        """ Перечень всех товаров """
