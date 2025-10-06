import pytest

from src.products import Product


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


def test_product_str():
    """Проверяет __str__ для Product."""
    product = Product("Test Product", "Test Desc", 150.5, 3)
    assert str(product) == "Test Product, 150.5 руб. Остаток: 3 шт."


def test_product_add():
    """Проверяет __add__ для двух продуктов."""
    product1 = Product("Prod1", "Desc1", 100.0, 2)  # 200
    product2 = Product("Prod2", "Desc2", 200.0, 3)  # 600
    assert product1 + product2 == 800.0


def test_product_add_not_product():
    """Проверяет __add__ с не-Product (должен вызывать TypeError)."""
    product = Product("Prod", "Desc", 100.0, 1)
    with pytest.raises(TypeError):
        product + "not a product"
