from tasks_lesson_12_1 import Product, Pizza, Coffee
from tasks_lesson_12_2 import AbstractShop


class NonProductError(TypeError):
    pass


class RealShop(AbstractShop):
    def __init__(self):
        self._products = []

    @staticmethod
    def is_valid(product: Product):
        """ Проверка типа передаваемых дынных """
        if not (isinstance(product, Product)):
            raise NonProductError(f'"{product}" - не является продуктом')

    def add_product(self, data: Product):
        """ Добавление нового товара"""
        self.is_valid(data)
        return self._products.append(data)

    def sell_product(self, data: Product):
        """ Продажа товара """
        for product in self._products:
            self.is_valid(data)
            if product == data:
                self._products.remove(product)
                return self._products

    def all_products(self):
        """ Перечень всех товаров """
        return self._products


products = RealShop()

p_001 = Pizza(6605, 'пицца', 12.66, ['сыр', 'ананас', 'грибы', 'креветки'], 'острая', 12)
p_003 = Coffee(8844, 'кофе', 2.66, 0.33, 'с сахаром', 'классическое')
p_01 = "666"

print(RealShop.all_products(products))
RealShop.add_product(products, p_001)
print(RealShop.all_products(products))
RealShop.add_product(products, p_003)
print(RealShop.all_products(products))
RealShop.add_product(products, p_01)
print(RealShop.all_products(products))
print()
