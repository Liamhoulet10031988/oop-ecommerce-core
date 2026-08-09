from src.product import Product


class LawnGrass(Product):
    """Класс для описания газонной травы."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)

    def __repr__(self) -> str:
        """Возвращает техническое представление газонной травы."""
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.description!r}, "
            f"{self.price}, {self.quantity}, "
            f"{self.country!r}, {self.germination_period!r}, "
            f"{self.color!r})"
        )
