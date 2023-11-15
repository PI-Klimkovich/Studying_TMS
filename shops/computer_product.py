from dataclasses import dataclass
from .shop_type import Computer


@dataclass  # Смотреть импорт
class Motherboard(Computer):
    pass


@dataclass  # Смотреть импорт
class VideoCard(Computer):
    pass


@dataclass  # Смотреть импорт
class Cooler(Computer):
    pass


@dataclass  # Смотреть импорт
class Keyboard(Computer):
    pass


@dataclass  # Смотреть импорт
class Mouse(Computer):
    pass
