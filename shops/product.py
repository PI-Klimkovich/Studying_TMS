from dataclasses import dataclass


@dataclass  # Смотреть импорт
class Product:
    id: int
    name: str
    price: float
