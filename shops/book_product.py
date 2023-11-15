from dataclasses import dataclass
from .shop_type import BookEditions


@dataclass  # Смотреть импорт
class Book(BookEditions):
    pass


@dataclass  # Смотреть импорт
class Magazine(BookEditions):
    pass
