class Product:
    """Класс для представления продукта в магазине."""

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __add__(self, other):
        """Переопределяем сложение для продуктов одинакового типа."""
        if type(self) != type(other):  # noqa: E721
            raise TypeError("Нельзя складывать продукты разных классов")
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    """Класс для смартфонов, наследник Product."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для газонной травы, наследник Product."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
