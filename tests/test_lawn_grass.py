from src.lawn_grass import LawnGrass
from src.product import Product


def test_lawn_grass_init() -> None:
    lawn_grass = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "зеленый",
    )

    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.description == "Элитная трава для газона"
    assert lawn_grass.price == 500.0
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "7 дней"
    assert lawn_grass.color == "зеленый"


def test_lawn_grass_is_product() -> None:
    lawn_grass = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "зеленый",
    )

    assert isinstance(lawn_grass, Product)


def test_lawn_grass_print_mixin(capsys) -> None:
    LawnGrass(
        "Grass",
        "local",
        5.8,
        2,
        "China",
        "2 days",
        "green",
    )

    message = capsys.readouterr().out

    assert (
        "LawnGrass('Grass', 'local', 5.8, 2, "
        "'China', '2 days', 'green')"
        in message
    )
