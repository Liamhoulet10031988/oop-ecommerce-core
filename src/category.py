from src.base_entity import BaseEntity
from src.exceptions import ZeroQuantityProductError
from src.product import Product


class Category(BaseEntity):
    """Класс для описания категории товаров интернет-магазина."""

    category_count = 0
    product_count = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: list[Product],
    ) -> None:
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию."""
        try:
            if not isinstance(product, Product):
                raise TypeError("Можно добавлять только товары")

            if product.quantity == 0:
                raise ZeroQuantityProductError()

        except ZeroQuantityProductError as error:
            print(error)

        else:
            self.__products.append(product)
            Category.product_count += 1
            print("Товар добавлен")

        finally:
            print("Обработка добавления товара завершена")

    @property
    def products(self) -> str:
        """Возвращает товары категории в виде строки."""
        result = ""

        for product in self.__products:
            result += str(product) + "\n"

        return result

    @property
    def product_objects(self) -> list[Product]:
        """Возвращает список объектов товаров категории."""
        return self.__products

    def __str__(self) -> str:
        """Возвращает строковое представление категории."""
        total_quantity = 0

        for product in self.__products:
            total_quantity += product.quantity

        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def get_total_quantity(self) -> int:
        total_quantity = 0

        for product in self.product_objects:
            total_quantity += product.quantity

        return total_quantity

    def middle_price(self) -> float:
        """Возвращает среднюю цену товаров в категории."""
        total_price = 0.0

        for product in self.__products:
            total_price += product.price

        try:
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0
