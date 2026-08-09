from src.base_entity import BaseEntity
from src.product import Product


class Order(BaseEntity):
    """Класс для описания заказа одного товара."""

    def __init__(self, product: Product, quantity: int) -> None:
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

    def get_total_quantity(self) -> int:
        return self.quantity
