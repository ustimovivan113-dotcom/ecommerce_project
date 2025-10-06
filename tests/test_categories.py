import pytest

from src.categories import Category
from src.products import Product, Smartphone


@pytest.fixture(autouse=True)
def reset_counts():
    """Автоматический reset для изоляции тестов."""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def sample_products():
    return [
        Product(name="Prod1", description="Desc1", price=100.0, quantity=1),
        Product(name="Prod2", description="Desc2", price=200.0, quantity=2),
    ]


@pytest.fixture
def sample_category(sample_products):
    return Category("Test Cat", "Test Cat Desc", sample_products)


def test_category_init(sample_category):
    """Проверяет инициализацию Category."""
    assert sample_category.name == "Test Cat"
    assert sample_category.description == "Test Cat Desc"
    assert "Prod1, 100.0 руб. Остаток: 1 шт." in sample_category.products


def test_category_counts():
    """Проверяет подсчет категорий и продуктов."""
    cat1 = Category(
        name="Cat1",
        description="Desc1",
        products=[Product(name="P1", description="D1", price=1.0, quantity=1)],
    )
    assert cat1.name == "Cat1"  # Используем cat1
    assert Category.category_count == 1
    assert Category.product_count == 1

    cat2 = Category(
        name="Cat2",
        description="Desc2",
        products=[
            Product(name="P2", description="D2", price=2.0, quantity=1),
            Product(name="P3", description="D3", price=3.0, quantity=1),
        ],
    )
    assert cat2.name == "Cat2"  # Используем cat2
    assert Category.category_count == 2
    assert Category.product_count == 3  # 1 + 2


def test_category_no_products():
    """Проверяет категорию без продуктов."""
    cat = Category(name="Empty Cat", description="Empty Desc", products=[])
    assert cat.name == "Empty Cat"  # Используем cat
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_add_product(sample_category):
    """Проверяет добавление продукта."""
    new_product = Smartphone(
        "New Phone", "New Desc", 150.0, 3, 90.0, "ModelX", 128, "Black"
    )
    sample_category.add_product(new_product)
    assert "New Phone, 150.0 руб. Остаток: 3 шт." in sample_category.products
    assert Category.product_count == 3  # Было 2, +1


def test_add_invalid_product(sample_category):
    """Проверяет ошибку при добавлении не-продукта."""
    with pytest.raises(TypeError):
        sample_category.add_product("Not a product")
