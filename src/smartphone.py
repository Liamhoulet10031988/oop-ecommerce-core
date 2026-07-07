from src.product import Product


class Smartphone(Product):
    """Класс для описания смартфона."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

    def __repr__(self) -> str:
        """Возвращает техническое представление смартфона."""
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.description!r}, "
            f"{self.price}, {self.quantity}, "
            f"{self.efficiency}, {self.model!r}, "
            f"{self.memory}, {self.color!r})"
        )
