import pytest

from src.categories import Category
from src.products import Product


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
    assert len(sample_category.products) == 2
    assert sample_category.products[0].name == "Prod1"  # Доп. покрытие


def test_category_counts():
    """Проверяет подсчет категорий и продуктов."""
    cat1 = Category(
        name="Cat1",
        description="Desc1",
        products=[Product(name="P1", description="D1", price=1.0, quantity=1)],
    )
    assert cat1.name == "Cat1"
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
    assert cat2.name == "Cat2"
    assert Category.category_count == 2
    assert Category.product_count == 3  # 1 + 2


def test_category_no_products():
    """Проверяет категорию без продуктов."""
    cat = Category(name="Empty Cat", description="Empty Desc", products=[])
    assert cat.name == "Empty Cat"
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_add_product(sample_category):
    """Проверяет добавление продукта в категорию."""
    new_product = Product("New Prod", "New Desc", 50.0, 3)
    sample_category.add_product(new_product)
    assert len(sample_category.products) == 3
    assert sample_category.products[-1].name == "New Prod"
    assert Category.product_count == 3


def test_add_invalid_product(sample_category):
    """Проверяет добавление некорректного продукта."""
    with pytest.raises(
        ValueError, match="Можно добавлять только объекты класса Product"
    ):
        sample_category.add_product("Not a product")
