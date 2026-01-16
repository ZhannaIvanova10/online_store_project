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


def test_load_categories_from_json():
    """Тест загрузки категорий из JSON файла."""
    # Создаем временный JSON файл
    test_data = {
        "categories": [
            {
                "name": "Test Category",
                "description": "Test Description",
                "products": [
                    {
                        "name": "Test Product",
                        "description": "Test Product Description",
                        "price": 100.0,
                        "quantity": 10
                    }
                ]
            }
        ]
    }
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(test_data, f)
        temp_file = f.name
    
    try:
        # Загружаем категории
        categories = load_categories_from_json(temp_file)
        
        # Проверяем результат
        assert len(categories) == 1
        assert isinstance(categories[0], Category)
        assert categories[0].name == "Test Category"
        assert len(categories[0].products) == 1
        assert isinstance(categories[0].products[0], Product)
        assert categories[0].products[0].name == "Test Product"
        assert categories[0].products[0].price == 100.0
    finally:
        # Удаляем временный файл
        os.unlink(temp_file)


def test_load_categories_from_json_file_not_found():
    """Тест загрузки из несуществующего файла."""
    categories = load_categories_from_json("non_existent_file.json")
    assert categories == []


def test_load_categories_from_json_invalid_format():
    """Тест загрузки из файла с неверным форматом."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        f.write('{ invalid json }')
        temp_file = f.name
    
    try:
        categories = load_categories_from_json(temp_file)
        assert categories == []
    finally:
        os.unlink(temp_file)
