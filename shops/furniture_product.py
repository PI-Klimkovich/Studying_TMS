from dataclasses import dataclass
from .shop_type import Furniture


@dataclass  # Смотреть импорт
class Table(Furniture):
    pass


@dataclass  # Смотреть импорт
class Chair(Furniture):
    pass


@dataclass  # Смотреть импорт
class Closet(Furniture):
    pass
