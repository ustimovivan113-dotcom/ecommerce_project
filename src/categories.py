from typing import List

from .products import Product  # Исправлено ранее


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name = name
        self.description = description  # Разбиваем для соответствия PEP8
        # и безопасности
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)
