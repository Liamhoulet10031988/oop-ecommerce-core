from src.product import Product


class Category:
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
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только товары")

        self.__products.append(product)
        Category.product_count += 1

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
