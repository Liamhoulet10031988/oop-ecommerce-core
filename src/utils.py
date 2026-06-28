import json

from src.category import Category
from src.product import Product


def load_categories_from_json(file_path: str) -> list[Category]:
    """Загружает категории и товары из JSON-файла."""
    with open(file_path, encoding="utf-8") as file:
        categories_data = json.load(file)

    categories = []

    for category_data in categories_data:
        products = []

        for product_data in category_data["products"]:
            product = Product(
                product_data["name"],
                product_data["description"],
                product_data["price"],
                product_data["quantity"],
            )
            products.append(product)

        category = Category(
            category_data["name"],
            category_data["description"],
            products,
        )
        categories.append(category)

    return categories
