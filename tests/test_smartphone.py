from src.product import Product
from src.smartphone import Smartphone


def test_smartphone_init() -> None:
    smartphone = Smartphone(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
        98.2,
        "15",
        512,
        "gray space",
    )

    assert smartphone.name == "Iphone 15"
    assert smartphone.description == "512GB, Gray space"
    assert smartphone.price == 210000.0
    assert smartphone.quantity == 8
    assert smartphone.efficiency == 98.2
    assert smartphone.model == "15"
    assert smartphone.memory == 512
    assert smartphone.color == "gray space"


def test_smartphone_is_product() -> None:
    smartphone = Smartphone(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
        98.2,
        "15",
        512,
        "gray space",
    )

    assert isinstance(smartphone, Product)


def test_smartphone_print_mixin(capsys) -> None:
    Smartphone(
        "Samsung",
        "local",
        5.8,
        2,
        95.5,
        "S20FE",
        64,
        "white",
    )

    message = capsys.readouterr().out

    assert (
        "Smartphone('Samsung', 'local', 5.8, 2, "
        "95.5, 'S20FE', 64, 'white')"
        in message
    )
