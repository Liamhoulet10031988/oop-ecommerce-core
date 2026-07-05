from src.category import Category
from src.product import Product


class CategoryIterator:
    """Итератор для перебора товаров одной категории."""

    def __init__(self, category: Category) -> None:
        self.category = category
        self.index = 0

    def __iter__(self) -> "CategoryIterator":
        self.index = 0
        return self

    def __next__(self) -> Product:
        if self.index < len(self.category.product_objects):
            product = self.category.product_objects[self.index]
            self.index += 1
            return product

        raise StopIteration
