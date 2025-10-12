from typing import List

from .products import Product


class Category:
    """Класс для представления категории товаров."""

    # Атрибуты класса
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name = name
        self.description = description  # Для PEP8, даже если строка короткая
        self.products = products

        # Авто-инкремент атрибутов класса
        Category.category_count += 1
        Category.product_count += len(products)

    def middle_price(self) -> float:
        """Подсчитывает средний ценник всех товаров в категории."""
        if not self.products:
            return 0
        total_price = sum(product.price for product in self.products)
        return total_price / len(self.products)
