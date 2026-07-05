import pytest

from src.category import Category
from src.category_iterator import CategoryIterator
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_category_init() -> None:
    product1 = Product("Iphone 15", "512GB", 210000.0, 8)
    product2 = Product("Xiaomi Redmi Note 11", "1024GB", 31000.0, 14)
    category = Category("Smartphones", "Mobile phones", [product1, product2])

    assert category.name == "Smartphones"
    assert category.description == "Mobile phones"
    assert (
        "Iphone 15, 210000.0 руб. Остаток: 8 шт."
        in category.products
    )
    assert (
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
        in category.products
    )


def test_category_count() -> None:
    product = Product("55 QLED 4K", "Smart TV", 123000.0, 7)

    Category("TV", "Modern TVs", [product])
    Category("Accessories", "Useful accessories", [])

    assert Category.category_count == 2


def test_product_count() -> None:
    product1 = Product("Iphone 15", "512GB", 210000.0, 8)
    product2 = Product("Xiaomi Redmi Note 11", "1024GB", 31000.0, 14)
    product3 = Product("55 QLED 4K", "Smart TV", 123000.0, 7)

    Category("Smartphones", "Mobile phones", [product1, product2])
    Category("TV", "Modern TVs", [product3])

    assert Category.product_count == 3


def test_add_product() -> None:
    product1 = Product("Iphone 15", "512GB", 210000.0, 8)
    product2 = Product("Xiaomi Redmi Note 11", "1024GB", 31000.0, 14)
    category = Category("Smartphones", "Mobile phones", [product1])

    category.add_product(product2)

    assert (
        "Iphone 15, 210000.0 руб. Остаток: 8 шт."
        in category.products
    )
    assert (
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
        in category.products
    )
    assert Category.product_count == 2


def test_category_str() -> None:
    product1 = Product("Iphone 15", "512GB", 210000.0, 8)
    product2 = Product("Xiaomi Redmi Note 11", "1024GB", 31000.0, 14)
    category = Category("Smartphones", "Mobile phones", [product1, product2])

    assert str(category) == "Smartphones, количество продуктов: 22 шт."


def test_category_iterator() -> None:
    product1 = Product("Iphone 15", "512GB", 210000.0, 8)
    product2 = Product("Xiaomi Redmi Note 11", "1024GB", 31000.0, 14)
    category = Category("Smartphones", "Mobile phones", [product1, product2])

    iterator = CategoryIterator(category)
    products = []

    for product in iterator:
        products.append(product)

    assert products == [product1, product2]


def test_add_product_accepts_product_children() -> None:
    smartphone = Smartphone(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
        98.2,
        "15",
        512,
        "gray space",
    )
    lawn_grass = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "зеленый",
    )
    category = Category("Разное", "Разные товары", [])

    category.add_product(smartphone)
    category.add_product(lawn_grass)

    assert "Iphone 15" in category.products
    assert "Газонная трава" in category.products


def test_add_product_rejects_not_product() -> None:
    category = Category("Разное", "Разные товары", [])

    with pytest.raises(TypeError):
        category.add_product("не товар")  # type: ignore[arg-type]
