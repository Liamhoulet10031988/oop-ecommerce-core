from src.category import Category
from src.category_iterator import CategoryIterator
from src.product import Product

if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, серый цвет, 200MP камера",
        180000.0,
        5,
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, синий", 31000.0, 14)

    category = Category(
        "Смартфоны",
        (
            "Смартфоны, как средство не только коммуникации, "
            "но и получения дополнительных функций"
        ),
        [product1, product2, product3],
    )

    print("Строковое представление товара:")
    print(product1)

    print("\nСтроковое представление категории:")
    print(category)

    print("\nСписок товаров категории:")
    print(category.products)

    product4 = Product(
        '55" QLED 4K',
        "Фоновая подсветка",
        123000.0,
        7,
    )
    category.add_product(product4)

    print("Список товаров после добавления нового товара:")
    print(category.products)

    total_price = product1 + product2
    print("Полная стоимость двух товаров на складе:")
    print(total_price)

    product_data = {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 220000.0,
        "quantity": 2,
    }
    updated_product = Product.new_product(
        product_data,
        category.product_objects,
    )

    print("\nТовар после обновления через new_product:")
    print(updated_product)

    updated_product.price = 230000.0
    print("\nЦена после работы setter:")
    print(updated_product.price)

    updated_product.price = -100
    print("Цена после попытки установить отрицательное значение:")
    print(updated_product.price)

    print("\nПеребор товаров категории через CategoryIterator:")
    iterator = CategoryIterator(category)

    for product in iterator:
        print(product)
