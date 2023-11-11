from abc import ABC, abstractmethod
from tasks_lesson_12_1 import Product


class AbstractShop(ABC):
    @abstractmethod
    def add_product(self, product: Product):
        """ Добавление нового товара"""

    @abstractmethod
    def sell_product(self, product: Product):
        """ Продажа товара """

    @abstractmethod
    def all_products(self: Product):
        """ Перечень всех товаров """
