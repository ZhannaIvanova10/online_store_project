"""
Тесты для загрузки данных из JSON.
"""

import sys
import os
import json
import tempfile

# Добавляем путь к src в PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.models import Product, Category, load_categories_from_json


def create_test_json_file():
    """Создает временный JSON файл для тестирования."""
    test_data = [
        {
            "name": "Test Category",
            "description": "Test category description",
            "products": [
                {
                    "name": "Test Product 1",
                    "description": "Test product 1 description",
                    "price": 100.50,
                    "quantity": 10,
                },
                {
                    "name": "Test Product 2",
                    "description": "Test product 2 description",
                    "price": 200.75,
                    "quantity": 5,
                },
            ],
        }
    ]
    # Создаем временный файл с явным указанием кодировки
    temp_file = tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, encoding="utf-8"
    )
    json.dump(test_data, temp_file, ensure_ascii=False)
    temp_file.close()

    return temp_file.name


def test_load_categories_from_json():
    """Тест загрузки категорий из JSON файла."""
    # Создаем тестовый JSON файл
    json_file = create_test_json_file()

    try:
        # Сбрасываем счетчики
        Category.category_count = 0
        Category.product_count = 0
        # Загружаем категории из файла
        categories = load_categories_from_json(json_file)

        # Проверяем результаты
        assert len(categories) == 1
        assert categories[0].name == "Test Category"
        assert categories[0].description == "Test category description"
        
        # Теперь products - это строка, проверяем содержимое
        products_str = categories[0].products
        assert "Test Product 1" in products_str
        assert "Test Product 2" in products_str
        assert "100.5" in products_str or "100.50" in products_str
        assert "200.75" in products_str
        
        # Проверяем счетчики
        assert Category.category_count == 1
        assert Category.product_count == 2
    finally:
        # Удаляем временный файл
        if os.path.exists(json_file):
            os.unlink(json_file)


def test_load_categories_from_json_with_empty_products():
    """Тест загрузки категории с пустым списком товаров."""
    test_data = [
        {
            "name": "Empty Category",
            "description": "Category without products",
            "products": [],
        }
    ]
    # Создаем временный файл
    temp_file = tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, encoding="utf-8"
    )
    json.dump(test_data, temp_file, ensure_ascii=False)
    temp_file.close()
    try:
        Category.category_count = 0
        Category.product_count = 0

        categories = load_categories_from_json(temp_file.name)

        assert len(categories) == 1
        assert categories[0].name == "Empty Category"
        assert categories[0].products == ""  # Пустая строка для пустого списка
        assert Category.category_count == 1
        assert Category.product_count == 0

    finally:
        if os.path.exists(temp_file.name):
            os.unlink(temp_file.name)


def test_load_categories_from_json_file_not_found():
    """Тест обработки случая, когда файл не найден."""
    import pytest
    # Пытаемся загрузить несуществующий файл
    with pytest.raises(FileNotFoundError):
        load_categories_from_json("non_existent_file_12345.json")


def test_load_categories_from_invalid_json():
    """Тест обработки невалидного JSON."""
    import pytest

    # Создаем файл с невалидным JSON
    temp_file = tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, encoding="utf-8"
    )
    temp_file.write("{invalid json")
    temp_file.close()
    try:
        with pytest.raises(json.JSONDecodeError):
            load_categories_from_json(temp_file.name)
    finally:
        if os.path.exists(temp_file.name):
            os.unlink(temp_file.name)
def test_load_real_json_file():
    """Тест загрузки из реального файла products.json."""
    if os.path.exists("products.json"):
        # Сбрасываем счетчики
        Category.category_count = 0
        Category.product_count = 0

        categories = load_categories_from_json("products.json")

        # Проверяем, что что-то загрузилось
        assert len(categories) > 0

        # Проверяем структуру первой категории
        if len(categories) > 0:
            assert hasattr(categories[0], "name")
            assert hasattr(categories[0], "description")
            assert hasattr(categories[0], "products")
            # Теперь products - это строка
            assert isinstance(categories[0].products, str)
