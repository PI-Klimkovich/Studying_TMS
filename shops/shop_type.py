from dataclasses import dataclass
from .product import Product


@dataclass  # Смотреть импорт
class Furniture(Product):
    pass


@dataclass  # Смотреть импорт
class BookEditions(Product):
    pass


@dataclass  # Смотреть импорт
class Computer(Product):
    pass
