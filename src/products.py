from abc import ABC, abstractmethod


class PrintMixin:
    """Миксин для печати информации при создании объекта."""

    def __init__(self, *args, **kwargs) -> None:
        class_name = self.__class__.__name__
        params = ", ".join(
            [repr(arg) for arg in args] + [f"{k}={repr(v)}" for k, v in kwargs.items()]
        )
        print(f"{class_name}({params})")
        super().__init__()  # Вызываем без аргументов, так как BaseProduct абстрактный


class BaseProduct(ABC):
    """Абстрактный базовый класс для продуктов."""

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @property
    @abstractmethod
    def quantity(self) -> int:
        pass


class Product(PrintMixin, BaseProduct):
    """Класс для представления продукта в магазине."""

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        super().__init__(
            name, description, price, quantity
        )  # Передаем аргументы в PrintMixin
        self._name = name
        self._description = description
        self._price = price
        self._quantity = quantity

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def price(self) -> float:
        return self._price

    @property
    def quantity(self) -> int:
        return self._quantity


class Smartphone(Product):
    """Класс для смартфонов, наследует от Product."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        performance: str,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для газонной травы, наследует от Product."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
