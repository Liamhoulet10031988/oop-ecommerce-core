from src.product import Product


def test_product_init() -> None:
    product = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Gray color, 200MP camera",
        180000.0,
        5,
    )

    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Gray color, 200MP camera"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_new_product() -> None:
    product = Product.new_product(
        {
            "name": "Iphone 15",
            "description": "512GB, Gray space",
            "price": 210000.0,
            "quantity": 8,
        }
    )

    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8


def test_price_setter_updates_price() -> None:
    product = Product("Iphone 15", "512GB", 210000.0, 8)

    product.price = 220000

    assert product.price == 220000


def test_price_setter_rejects_zero_or_negative_price(capsys) -> None:
    product = Product("Iphone 15", "512GB", 210000.0, 8)
    expected_message = "Цена не должна быть нулевая или отрицательная"

    product.price = -100
    product.price = 0

    message = capsys.readouterr().out

    assert product.price == 210000.0
    assert expected_message in message


def test_price_setter_decreases_price_with_confirm(monkeypatch) -> None:
    product = Product("Iphone 15", "512GB", 210000.0, 8)

    monkeypatch.setattr("builtins.input", lambda text: "y")
    product.price = 800

    assert product.price == 800


def test_price_setter_does_not_decrease_price_without_confirm(
    monkeypatch,
) -> None:
    product = Product("Iphone 15", "512GB", 210000.0, 8)

    monkeypatch.setattr("builtins.input", lambda text: "n")
    product.price = 800

    assert product.price == 210000.0


def test_new_product_updates_existing_product() -> None:
    product = Product("Iphone 15", "512GB", 210000.0, 8)

    result = Product.new_product(
        {
            "name": "Iphone 15",
            "description": "512GB, Gray space",
            "price": 220000.0,
            "quantity": 2,
        },
        [product],
    )

    assert result is product
    assert product.quantity == 10
    assert product.price == 220000.0


def test_product_str() -> None:
    product = Product("Iphone 15", "512GB", 210000.0, 8)

    assert str(product) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_product_add() -> None:
    product1 = Product("A", "Test product", 100, 10)
    product2 = Product("B", "Test product", 200, 2)

    assert product1 + product2 == 1400
