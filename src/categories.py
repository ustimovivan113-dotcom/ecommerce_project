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

    def __str__(self) -> str:
        """Строковое представление категории: 'Название категории, количество продуктов:
        X шт.'"""
        total_quantity = sum(product.quantity for product in self.products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __iter__(self) -> 'CategoryIterator':
        """Возвращает итератор по продуктам категории."""
        return CategoryIterator(self)


class CategoryIterator:
    """Итератор для продуктов в категории."""

    def __init__(self, category: Category) -> None:
        self._products = category.products
        self._index = 0

    def __iter__(self) -> 'CategoryIterator':
        return self

    def __next__(self) -> Product:
        if self._index < len(self._products):
            product = self._products[self._index]
            self._index += 1
            return product
        raise StopIteration
