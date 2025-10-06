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


def test_new_product():
    """Проверяет создание продукта через classmethod."""
    data = {
        "name": "New Prod",
        "description": "New Desc",
        "price": 400.0,
        "quantity": 4,
    }
    prod = Product.new_product(data)
    assert prod.name == "New Prod"
    assert prod.description == "New Desc"
    assert prod.price == 400.0
    assert prod.quantity == 4


def test_price_setter(sample_product):
    """Проверяет setter цены."""
    sample_product.price = 150.0
    assert sample_product.price == 150.0

    # Проверка отрицательной цены (не меняет, но print - мы не тестируем print)
    old_price = sample_product.price
    sample_product.price = -50.0
    assert sample_product.price == old_price  # Не изменилось

    sample_product.price = 0
    assert sample_product.price == old_price  # Не изменилось
