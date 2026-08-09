import pytest

from src.base_product import BaseProduct


def test_base_product_cannot_be_created() -> None:
    with pytest.raises(TypeError):
        BaseProduct()  # type: ignore[abstract]
