from src.order import Order
from src.product import Product


def test_order_init() -> None:
    product = Product("Bread", "local", 5.8, 10)
    order = Order(product, 3)

    assert order.product is product
    assert order.quantity == 3
    assert order.total_price == 17.4


def test_order_get_total_quantity() -> None:
    product = Product("Bread", "local", 5.8, 10)
    order = Order(product, 3)

    assert order.get_total_quantity() == 3
