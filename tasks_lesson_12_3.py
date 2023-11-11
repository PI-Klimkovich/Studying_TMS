from tasks_lesson_12_0 import products
from tasks_lesson_12_1 import Product, Pizza, Coffee
from tasks_lesson_12_2 import AbstractShop


class RealShop(AbstractShop):
    def __init__(self, products: list):
        self.products = products

    def add_product(self, data: Product):
        """ Добавление нового товара"""
        return products.append(data)

    def sell_product(self, data):
        """ Продажа товара """
        for product in products:
            if product.id == data:
                print(product)
                products.remove(product)
                return products

    def all_products(self):
        """ Перечень всех товаров """
        print(products)


p_01 = Product(6503, 'табурет', 15.66)
p_02 = Coffee(8846, 'кофе', 2.25, 0.05, 'без сахара', 'робуста')
p_03 = Pizza(6608, 'пицца', 18.66, ['сыр', 'ветчина', 'грибы', 'сладкий перец'], 'не острая', 15)

RealShop.all_products(products)
RealShop.add_product(products, p_01)
RealShop.all_products(products)
RealShop.add_product(products, p_02)
RealShop.all_products(products)
RealShop.add_product(products, p_03)
RealShop.all_products(products)
print()

data_id = 6502
RealShop.sell_product(products, data_id)
RealShop.all_products(products)
data_id = 8846
RealShop.sell_product(products, data_id)
RealShop.all_products(products)
