from dataclasses import dataclass
from .product import Product


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
