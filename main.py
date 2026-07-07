from src.base_product import BaseProduct
from src.category import Category
from src.category_iterator import CategoryIterator
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone

if __name__ == "__main__":
    print("Создание объектов:")
    print("PrintMixin автоматически печатает repr объекта.")

    product = Product(
        "55 QLED 4K",
        "Фоновая подсветка",
        123000.0,
        7,
    )
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "серый",
    )
    smartphone2 = Smartphone(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
        98.2,
        "15",
        512,
        "gray space",
    )
    lawn_grass1 = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "зеленый",
    )
    lawn_grass2 = LawnGrass(
        "Газонная трава 2",
        "Быстрорастущая газонная трава",
        700.0,
        15,
        "Германия",
        "5 дней",
        "темно-зеленый",
    )

    category = Category(
        "Товары для дома",
        "Смартфоны и товары для участка",
        [product, smartphone1],
    )
    category.add_product(smartphone2)
    category.add_product(lawn_grass1)
    category.add_product(lawn_grass2)

    print("\nПроверка абстрактного класса BaseProduct:")
    print(isinstance(product, BaseProduct))
    print(isinstance(smartphone1, BaseProduct))
    print(isinstance(lawn_grass1, BaseProduct))

    print("\nПорядок поиска методов Product через MRO:")
    print(Product.__mro__)

    print("\nСписок товаров категории:")
    print(category.products)

    print("Строковое представление категории:")
    print(category)

    print("\nСложение смартфонов:")
    print(smartphone1 + smartphone2)

    print("\nСложение газонной травы:")
    print(lawn_grass1 + lawn_grass2)

    print("\nПроверка, что Smartphone является Product:")
    print(isinstance(smartphone1, Product))

    print("\nПроверка, что LawnGrass является Product:")
    print(isinstance(lawn_grass1, Product))

    print("\nПроверка точного класса для сложения:")
    print(type(smartphone1) is type(smartphone2))
    print(type(smartphone1) is type(lawn_grass1))

    print("\nПеребор товаров категории через CategoryIterator:")
    iterator = CategoryIterator(category)

    for product_item in iterator:
        print(product_item)
