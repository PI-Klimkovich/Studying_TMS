from dataclasses import dataclass
from tasks_lesson_12_1 import Product
from tasks_lesson_12_2 import AbstractShop


class NonProductError(TypeError):
    pass


@dataclass  # Смотреть импорт
class Furniture(Product):
    pass


@dataclass  # Смотреть импорт
class Table(Furniture):
    pass


@dataclass  # Смотреть импорт
class Chair(Furniture):
    pass


@dataclass  # Смотреть импорт
class Closet(Furniture):
    pass


class FurnitureShop(AbstractShop):
    def __init__(self):
        self._products = []

    @staticmethod
    def is_valid(product: Furniture):
        """ Проверка типа передаваемых дынных """
        if not (isinstance(product, Furniture)):
            raise NonProductError(f'"представленный {product}" - не мебель')

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


products = FurnitureShop()

p_001 = Table(6605, 'столик', 12.66)
p_002 = Chair(8844, 'стульчик', 2.66)
p_003 = Closet(6644, 'шкафчик', 22.66)
p_01 = "666"

print(FurnitureShop.all_products(products))
FurnitureShop.add_product(products, p_001)
print(FurnitureShop.all_products(products))
FurnitureShop.add_product(products, p_002)
print(FurnitureShop.all_products(products))
FurnitureShop.add_product(products, p_003)
print(FurnitureShop.all_products(products))
FurnitureShop.sell_product(products, p_002)
print(FurnitureShop.all_products(products))
FurnitureShop.add_product(products, p_01)
print(FurnitureShop.all_products(products))
print()
