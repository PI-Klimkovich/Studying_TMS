from tasks_lesson_12_1 import Product, Pizza, Coffee
from tasks_lesson_12_2 import AbstractShop


class RealShop(AbstractShop):
    def __init__(self):
        self._products = []

    def add_product(self, data: Product):
        """ Добавление нового товара"""
        return self._products.append(data)

    def sell_product(self, data):
        """ Продажа товара """
        for product in self._products:
            if product.id == data:
                print(product)
                self._products.remove(product)
                return self._products

    def all_products(self):
        """ Перечень всех товаров """
        print(self._products)


products = RealShop()

p_001 = Pizza(6605, 'пицца', 12.66, ['сыр', 'ананас', 'грибы', 'креветки'], 'острая', 12)
p_002 = Pizza(6606, 'пицца', 12.66, ['сыр', 'грибы', 'креветки', 'устрицы', 'помидоры'], 'не острая', 15)
p_003 = Coffee(8844, 'кофе', 2.66, 0.33, 'с сахаром', 'классическое')
p_004 = Coffee(8845, 'кофе', 2.06, 0.05, 'без сахара', 'арабика')
p_01 = Coffee(8846, 'кофе', 2.25, 0.05, 'без сахара', 'робуста')
p_02 = Pizza(6608, 'пицца', 18.66, ['сыр', 'ветчина', 'грибы', 'сладкий перец'], 'не острая', 15)

RealShop.all_products(products)
RealShop.add_product(products, p_001)
RealShop.add_product(products, p_002)
RealShop.add_product(products, p_003)
RealShop.add_product(products, p_004)
RealShop.all_products(products)
RealShop.add_product(products, p_01)
RealShop.all_products(products)
RealShop.add_product(products, p_02)
RealShop.all_products(products)
print()
data_id = 6502
RealShop.sell_product(products, data_id)
RealShop.all_products(products)
data_id = 8846
RealShop.sell_product(products, data_id)
RealShop.all_products(products)
