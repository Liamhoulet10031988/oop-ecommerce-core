import pytest

from src.category import Category


@pytest.fixture(autouse=True)
def reset_category_counts() -> None:
    Category.category_count = 0
    Category.product_count = 0
