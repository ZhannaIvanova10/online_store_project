"""
Тесты для проверки загрузки JSON с исключениями.
"""
import pytest
import json
import os
from src.models import load_categories_from_json
def test_load_valid_json():
    """Тест загрузки валидного JSON файла."""
    # Создаем временный файл
    test_data = [
        {
            "name": "Электроника",
            "description": "Электронные устройства",
            "products": [
                {
                    "name": "Смартфон",
                    "description": "Мощный смартфон",
                    "price": 29999.99,
                    "quantity": 10
                }
            ]
        }
    ]
    
    with open("test_valid.json", "w", encoding="utf-8") as f:
        json.dump(test_data, f)
    try:
        categories = load_categories_from_json("test_valid.json")
        assert len(categories) == 1
        assert categories[0].name == "Электроника"
        assert categories[0].get_products_count() == 1
    finally:
        os.remove("test_valid.json")


def test_load_nonexistent_file():
    """Тест загрузки несуществующего файла."""
    with pytest.raises(FileNotFoundError):
        load_categories_from_json("nonexistent.json")


def test_load_invalid_json():
    """Тест загрузки невалидного JSON."""
    with open("test_invalid.json", "w", encoding="utf-8") as f:
        f.write("{ это не валидный json }")
    try:
        with pytest.raises(json.JSONDecodeError):
            load_categories_from_json("test_invalid.json")
    finally:
        os.remove("test_invalid.json")


def test_load_json_missing_fields():
    """Тест загрузки JSON с отсутствующими полями."""
    test_data = [
        {
            "name": "Тест",
            # Нет description
            "products": []
        }
    ]
    with open("test_missing.json", "w", encoding="utf-8") as f:
        json.dump(test_data, f)
    
    try:
        categories = load_categories_from_json("test_missing.json")
        # Должен создаться с пустым описанием
        assert len(categories) == 1
        assert categories[0].description == ""
    finally:
        os.remove("test_missing.json")


def test_load_json_zero_quantity():
    """Тест загрузки JSON с товаром quantity=0."""
    test_data = [
        {
            "name": "Тест",
            "description": "Описание",
            "products": [
                {
                    "name": "Товар",
                    "description": "Описание",
                    "price": 100,
                    "quantity": 0  # Должно вызвать ValueError
                }
            ]
        }
    ]
    
    with open("test_zero.json", "w", encoding="utf-8") as f:
        json.dump(test_data, f)
    
    try:
        with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
            load_categories_from_json("test_zero.json")
    finally:
        os.remove("test_zero.json")
