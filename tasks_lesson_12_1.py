from dataclasses import dataclass


@dataclass  # Смотреть импорт
class Product:
    id: int
    name: str
    price: float


@dataclass  # Смотреть импорт
class Pizza(Product):
    topping: list
    spicy: str
    diameter: int


@dataclass  # Смотреть импорт
class Coffee(Product):
    volume: float
    sugar: str
    coffee_type: str


product_01 = Product(6501, 'стул', 26.50)
product_02 = Pizza(6605, 'пицца', 12.66, ['сыр', 'ананас', 'грибы', 'креветки'], 'острая', 12)
product_03 = Coffee(8844, 'кофе', 2.66, 0.33, 'без сахара', 'классическое')

print(product_01)
print(product_02)
print(product_03)
