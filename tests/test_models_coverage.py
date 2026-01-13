"""
Дополнительные тесты для увеличения покрытия models.py.
"""

import sys
import os

# Добавляем путь к src в PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.models import Product, Category
import json
import tempfile


def test_product_str_representation():
    """Тест строкового представления Product (неявно через отладку)."""
    product = Product("Test", "Description", 100.0, 5)
    # Проверяем, что атрибуты доступны
    assert product.name == "Test"
    assert product.description == "Description"
    assert product.price == 100.0
    assert product.quantity == 5
    # Проверяем, что объект можно преобразовать в строку
    str_repr = str(product)
    assert str_repr is not None


def test_category_str_representation():
    """Тест строкового представления Category."""
    product = Product("Test", "Desc", 50, 2)
    category = Category("Test Category", "Description", [product])

    assert category.name == "Test Category"
    assert category.description == "Description"
    # products теперь строка
    products_str = category.products
    assert "Test" in products_str
    assert "50 руб." in products_str
def test_category_with_multiple_products():
    """Тест категории с несколькими товарами."""
    products = [
        Product("P1", "D1", 10, 1),
        Product("P2", "D2", 20, 2),
        Product("P3", "D3", 30, 3),
    ]

    category = Category("Multi", "Multi products", products)

    # Проверяем содержимое строки
    products_str = category.products
    assert "P1" in products_str
    assert "P2" in products_str
    assert "P3" in products_str
    assert Category.product_count >= 3
def test_load_categories_edge_cases():
    """Тест edge cases для загрузки из JSON."""
    from src.models import load_categories_from_json

    # Тест 1: JSON с одной категорией и одним товаром
    data1 = [
        {
            "name": "Single",
            "description": "Single category",
            "products": [
                {
                    "name": "Single Product",
                    "description": "Desc",
                    "price": 100.0,
                    "quantity": 1,
                }
            ],
        }
    ]
    temp_file = tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, encoding="utf-8"
    )
    json.dump(data1, temp_file, ensure_ascii=False)
    temp_file.close()

    try:
        Category.category_count = 0
        Category.product_count = 0

        categories = load_categories_from_json(temp_file.name)
        assert len(categories) == 1
        # products теперь строка
        products_str = categories[0].products
        assert "Single Product" in products_str
        assert "100.0 руб." in products_str
    finally:
        if os.path.exists(temp_file.name):
            os.unlink(temp_file.name)
    # Тест 2: Пустой список категорий
    data2 = []

    temp_file2 = tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, encoding="utf-8"
    )
    json.dump(data2, temp_file2, ensure_ascii=False)
    temp_file2.close()

    try:
        Category.category_count = 0
        Category.product_count = 0

        categories = load_categories_from_json(temp_file2.name)
        assert len(categories) == 0
        assert Category.category_count == 0
        assert Category.product_count == 0

    finally:
        if os.path.exists(temp_file2.name):
            os.unlink(temp_file2.name)
