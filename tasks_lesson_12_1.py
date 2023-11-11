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
