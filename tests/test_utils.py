import json

from src.category import Category
from src.utils import load_categories_from_json


def test_load_categories_from_json(tmp_path) -> None:
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
                },
                {
                    "name": "Xiaomi Redmi Note 11",
                    "description": "1024GB",
                    "price": 31000.0,
                    "quantity": 14,
                },
            ],
        }
    ]

    file_path = tmp_path / "products.json"
    file_path.write_text(json.dumps(data), encoding="utf-8")

    categories = load_categories_from_json(str(file_path))

    assert len(categories) == 1
    assert categories[0].name == "Smartphones"
    assert "Iphone 15" in categories[0].products
    assert "Xiaomi Redmi Note 11" in categories[0].products
    assert Category.product_count == 2
