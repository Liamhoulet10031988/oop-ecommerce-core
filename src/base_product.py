from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для продуктов."""

    @classmethod
    @abstractmethod
    def new_product(
        cls,
        product_data: dict,
        products: list | None = None,
    ) -> "BaseProduct":
        """Создает продукт из словаря с данными."""
        pass
