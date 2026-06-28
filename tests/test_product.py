from src.product import Product


def test_product_init() -> None:
    product = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Gray color, 200MP camera",
        180000.0,
        5,
    )

    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Gray color, 200MP camera"
    assert product.price == 180000.0
    assert product.quantity == 5
