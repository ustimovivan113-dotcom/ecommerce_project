import pytest

from src.products import BaseProduct, LawnGrass, Product, Smartphone


@pytest.fixture
def sample_product():
    return Product("Test Phone", "Test Desc", 100.0, 10)


def test_product_init(sample_product):
    """Проверяет инициализацию Product."""
    assert sample_product.name == "Test Phone"
    assert sample_product.description == "Test Desc"
    assert sample_product.price == 100.0
    assert sample_product.quantity == 10


def test_product_zero_quantity():
    """Проверяет создание продукта с нулевым количеством."""
    product = Product("Test Zero", "Desc Zero", 50.0, 0)
    assert product.quantity == 0
    assert product.name == "Test Zero"


def test_print_mixin(capsys):
    """Проверяет печать от PrintMixin."""
    Product("Mixin Test", "Desc", 10.0, 1)
    captured = capsys.readouterr()
    assert "Product('Mixin Test', 'Desc', 10.0, 1)" in captured.out


def test_smartphone_init():
    """Проверяет инициализацию Smartphone."""
    smartphone = Smartphone(
        "Samsung S23",
        "High end",
        1500.0,
        5,
        "Exynos",
        "S23",
        256,
        "Black",
    )
    assert smartphone.name == "Samsung S23"
    assert smartphone.description == "High end"
    assert smartphone.price == 1500.0
    assert smartphone.quantity == 5
    assert smartphone.performance == "Exynos"
    assert smartphone.model == "S23"
    assert smartphone.memory == 256
    assert smartphone.color == "Black"
    assert isinstance(smartphone, Product)  # Проверка наследования


def test_lawn_grass_init():
    """Проверяет инициализацию LawnGrass."""
    grass = LawnGrass(
        "Green Grass",
        "Fast grow",
        20.0,
        50,
        "Russia",
        5,
        "Green",
    )
    assert grass.name == "Green Grass"
    assert grass.description == "Fast grow"
    assert grass.price == 20.0
    assert grass.quantity == 50
    assert grass.country == "Russia"
    assert grass.germination_period == 5
    assert grass.color == "Green"
    assert isinstance(grass, Product)  # Проверка наследования


def test_base_product_cannot_instantiate():
    """Проверяет, что BaseProduct нельзя инстанцировать."""
    with pytest.raises(TypeError, match="Can't instantiate abstract class"):
        BaseProduct()
