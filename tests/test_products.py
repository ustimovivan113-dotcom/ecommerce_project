import pytest

from src.products import LawnGrass, Product, Smartphone


@pytest.fixture
def sample_product():
    return Product("Test Phone", "Test Desc", 100.0, 10)


@pytest.fixture
def sample_smartphone():
    return Smartphone("Samsung S23", "Ultra", 180000.0, 5, 95.5, "S23", 256, "Gray")


@pytest.fixture
def sample_lawngrass():
    return LawnGrass("Grass1", "Green", 500.0, 20, "Russia", "7 days", "Green")


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


def test_smartphone_init(sample_smartphone):
    """Проверяет инициализацию Smartphone."""
    assert sample_smartphone.name == "Samsung S23"
    assert sample_smartphone.efficiency == 95.5
    assert sample_smartphone.model == "S23"
    assert sample_smartphone.memory == 256
    assert sample_smartphone.color == "Gray"


def test_lawngrass_init(sample_lawngrass):
    """Проверяет инициализацию LawnGrass."""
    assert sample_lawngrass.name == "Grass1"
    assert sample_lawngrass.country == "Russia"
    assert sample_lawngrass.germination_period == "7 days"
    assert sample_lawngrass.color == "Green"


def test_add_same_type(sample_smartphone):
    """Проверяет сложение продуктов одного типа."""
    smartphone2 = Smartphone(
        "Iphone 15", "Pro", 210000.0, 8, 98.2, "15", 512, "Space Gray"
    )
    total = sample_smartphone + smartphone2
    assert total == (180000.0 * 5 + 210000.0 * 8)


def test_add_different_type(sample_smartphone, sample_lawngrass):
    """Проверяет ошибку при сложении разных типов."""
    with pytest.raises(TypeError):
        sample_smartphone + sample_lawngrass
