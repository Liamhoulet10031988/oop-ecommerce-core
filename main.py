from src.category import Category
from src.product import Product
from src.utils import load_categories_from_json


if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Gray color, 200MP camera",
        180000.0,
        5,
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Blue", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category(
        "Smartphones",
        "Smartphones for communication and daily tasks",
        [product1, product2, product3],
    )

    print(category1.name == "Smartphones")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55 QLED 4K", "Background lighting", 123000.0, 7)
    category2 = Category(
        "TV",
        "Modern TV for comfortable watching",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)

    categories_from_json = load_categories_from_json("products.json")

    print(len(categories_from_json))
    print(len(categories_from_json[0].products))
