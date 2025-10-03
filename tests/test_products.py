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
