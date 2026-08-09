from src.exceptions import ZeroQuantityProductError


def test_zero_quantity_product_error_message() -> None:
    error = ZeroQuantityProductError()

    assert str(error) == "Товар с нулевым количеством не может быть добавлен"
