from abc import ABC, abstractmethod


class BaseEntity(ABC):
    """Абстрактный базовый класс для сущностей с товарами."""

    @abstractmethod
    def get_total_quantity(self) -> int:
        """Возвращает общее количество товаров."""
        pass
