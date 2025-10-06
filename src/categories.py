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
        self.__products = products  # Сделаем приватным для контроля доступа

        # Авто-инкремент атрибутов класса
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self) -> str:
        """Возвращает строковое представление продуктов для печати."""
        return "\n".join(
            f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
            for p in self.__products
        )

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию, если это Product или наследник."""
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты класса Product или его наследников"
            )
        self.__products.append(product)
        Category.product_count += 1
