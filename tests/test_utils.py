import json

from src.category import Category
from src.product import Product
from src.utils import load_categories_from_json


def test_load_categories_from_json(tmp_path) -> None:
    file_path = tmp_path / "products.json"
    data = [
        {
            "name": "Smartphones",
            "description": "Mobile phones",
            "products": [
                {
                    "name": "Iphone 15",
                    "description": "512GB",
                    "price": 210000.0,
                    "quantity": 8,
                }
            ],
        }
    ]

    file_path.write_text(json.dumps(data), encoding="utf-8")

    categories = load_categories_from_json(str(file_path))

    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert categories[0].name == "Smartphones"
    assert len(categories[0].products) == 1
    assert isinstance(categories[0].products[0], Product)
    assert categories[0].products[0].name == "Iphone 15"
    assert Category.category_count == 1
    assert Category.product_count == 1
