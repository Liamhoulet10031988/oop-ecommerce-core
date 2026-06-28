from src.category import Category
from src.product import Product


def test_category_init() -> None:
    product1 = Product("Iphone 15", "512GB", 210000.0, 8)
    product2 = Product("Xiaomi Redmi Note 11", "1024GB", 31000.0, 14)
    category = Category("Smartphones", "Mobile phones", [product1, product2])

    assert category.name == "Smartphones"
    assert category.description == "Mobile phones"
    assert category.products == [product1, product2]


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
