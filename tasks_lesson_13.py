from shops import FurnitureShop, Table, Chair, Closet
from shops import RealShop, Pizza, Coffee


products = FurnitureShop()

p_001 = Table(6605, 'столик', 12.66)
p_002 = Chair(8844, 'стульчик', 2.66)
p_003 = Closet(6644, 'шкафчик', 22.66)
# p_01 = "666"

print(FurnitureShop.all_products(products))
FurnitureShop.add_product(products, p_001)
print(FurnitureShop.all_products(products))
FurnitureShop.add_product(products, p_002)
print(FurnitureShop.all_products(products))
FurnitureShop.add_product(products, p_003)
print(FurnitureShop.all_products(products))
FurnitureShop.sell_product(products, p_002)
print(FurnitureShop.all_products(products))
# FurnitureShop.add_product(products, p_01)
# print(FurnitureShop.all_products(products))
print()


products = RealShop()

p_001 = Pizza(6605, 'пицца', 12.66, ['сыр', 'ананас', 'грибы', 'креветки'], 'острая', 12)
p_003 = Coffee(8844, 'кофе', 2.66, 0.33, 'с сахаром', 'классическое')
# p_01 = "666"

print(RealShop.all_products(products))
RealShop.add_product(products, p_001)
print(RealShop.all_products(products))
RealShop.add_product(products, p_003)
print(RealShop.all_products(products))
# RealShop.add_product(products, p_01)
# print(RealShop.all_products(products))
print()
