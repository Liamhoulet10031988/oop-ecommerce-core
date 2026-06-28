# OOP E-commerce Core

Проект описывает базовое ядро интернет-магазина. Задача проекта - показать, как через классы описывать
сущности предметной области: товары и категории товаров.

## Что реализовано

- класс `Product` для товара;
- класс `Category` для категории товаров;
- инициализация объектов через `__init__`;
- хранение свойств объекта через `self`;
- подсчет общего количества категорий;
- подсчет общего количества товаров;
- загрузка категорий и товаров из `products.json`;
- тесты для проверки классов и загрузки данных.

## Основные сущности

`Product` описывает товар:

- `name` - название;
- `description` - описание;
- `price` - цена;
- `quantity` - количество в наличии.

`Category` описывает категорию товаров:

- `name` - название;
- `description` - описание;
- `products` - список товаров категории.

У `Category` также есть атрибуты класса:

- `category_count` - общее количество созданных категорий;
- `product_count` - общее количество товаров во всех категориях.

## Структура проекта

```text
OOP_E-commerce/
├── src/
│   ├── __init__.py
│   ├── category.py
│   ├── product.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_category.py
│   ├── test_product.py
│   └── test_utils.py
├── main.py
├── products.json
├── poetry.toml
├── pyproject.toml
└── README.md
```

## Файлы проекта

- `src/product.py` - класс `Product`;
- `src/category.py` - класс `Category`;
- `src/utils.py` - функция загрузки данных из JSON;
- `main.py` - демонстрационный запуск проекта;
- `products.json` - пример данных с категориями и товарами;
- `tests/` - тесты проекта.

## Установка

```bash
poetry install
```

## Запуск

```bash
poetry run python main.py
```

## Тесты

```bash
poetry run pytest
```

Дополнительные проверки проекта:

```bash
poetry run pytest --cov=src --cov-report=term-missing --cov-report=html:coverage_html
poetry run flake8
poetry run isort .
poetry run mypy .
```