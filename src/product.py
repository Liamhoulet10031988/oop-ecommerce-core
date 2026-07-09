from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(PrintMixin, BaseProduct):
    """Класс для описания товара интернет-магазина."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        self.name = name
        self.description = description
        self.__price = price

        if quantity == 0:
            raise ValueError(
                "Товар с нулевым количеством не может быть добавлен"
            )

        self.quantity = quantity
        super().__init__()

    @classmethod
    def new_product(
        cls,
        product_data: dict,
        products: list["Product"] | None = None,
    ) -> "Product":
        """Создает товар из словаря с данными."""
        if products is not None:
            for product in products:
                if product.name == product_data["name"]:
                    product.quantity += product_data["quantity"]
                    product.price = max(product.price, product_data["price"])
                    return product

        return cls(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"],
        )

    @property
    def price(self) -> float:
        """Возвращает цену товара."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Устанавливает новую цену товара."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            user_answer = input("Цена снижается. Подтвердить? y/n: ")

            if user_answer != "y":
                return

        self.__price = new_price

    def __str__(self) -> str:
        """Возвращает строковое представление товара."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Возвращает полную стоимость двух товаров одного класса."""
        if type(self) is not type(other):
            raise TypeError("Складывать можно только товары одного типа")

        return self.price * self.quantity + other.price * other.quantity

    def __repr__(self) -> str:
        """Возвращает техническое представление товара."""
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.description!r}, "
            f"{self.price}, {self.quantity})"
        )
