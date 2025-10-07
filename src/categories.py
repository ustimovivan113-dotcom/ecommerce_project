from typing import List

from .products import Product


class Category:
    """Класс для представления категории товаров."""

    # Атрибуты класса
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name = name
        self.description = description
        self.products = products

        # Авто-инкремент атрибутов класса
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию."""
        if not isinstance(product, Product):
            raise ValueError(
                "Можно добавлять только объекты класса Product или его наследников"
            )
        self.products.append(product)
        Category.product_count += 1
