from typing import List

from .products import Product  # Исправлено ранее


class Category:
    """Класс для представления категории товаров."""

    # Атрибуты класса
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name = name
        self.description = description  # Разбиваем для PEP8, даже если description <79, для безопасности
        self.products = products

        # Авто-инкремент атрибутов класса
        Category.category_count += 1
        Category.product_count += len(products)
