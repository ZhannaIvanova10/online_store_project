"""
Дополнительные тесты для main.py.
"""

import sys
import os
import io
from contextlib import redirect_stdout

# Добавляем путь к src в PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.main import create_sample_data, print_store_info, load_and_print_json_data
from src.models import Category, Product


def test_create_sample_data():
    """Тест функции создания тестовых данных."""
    cat1, cat2 = create_sample_data()

    assert cat1.name == "Смартфоны"
    assert cat2.name == "Аксессуары"
    assert len(cat1.products) == 2
    assert len(cat2.products) == 1
    assert Category.category_count >= 2


def test_print_store_info():
    """Тест функции вывода информации о магазине."""
    # Создаем тестовые данные
    product1 = Product("Test1", "Desc1", 100, 1)
    product2 = Product("Test2", "Desc2", 200, 2)

    cat1 = Category("Category1", "Desc1", [product1])
    cat2 = Category("Category2", "Desc2", [product2])

    # Захватываем вывод
    f = io.StringIO()
    with redirect_stdout(f):
        print_store_info(cat1, cat2)

    output = f.getvalue()

    # Проверяем ключевые элементы вывода
    assert "ИНФОРМАЦИЯ О МАГАЗИНЕ" in output
    assert "Category1" in output
    assert "Category2" in output
    assert "Всего категорий в магазине:" in output


def test_load_and_print_json_data_output():
    """Тест вывода функции load_and_print_json_data."""
    # Создаем временный файл products.json для теста
    import json
    import tempfile

    test_data = [
        {
            "name": "Test Category",
            "description": "Test description",
            "products": [
                {
                    "name": "Test Product",
                    "description": "Test product desc",
                    "price": 100.0,
                    "quantity": 5,
                }
            ],
        }
    ]

    # Сохраняем оригинальный файл если существует
    original_exists = os.path.exists("products.json")
    if original_exists:
        os.rename("products.json", "products.json.backup")
    try:
        # Создаем тестовый файл
        with open("products.json", "w", encoding="utf-8") as f:
            json.dump(test_data, f, ensure_ascii=False)

        # Тестируем функцию
        f = io.StringIO()
        with redirect_stdout(f):
            load_and_print_json_data()

        output = f.getvalue()
        assert "ДАННЫЕ ИЗ JSON-ФАЙЛА" in output
        assert "Test Category" in output

    finally:
        # Восстанавливаем оригинальный файл
        if os.path.exists("products.json"):
            os.unlink("products.json")
        if original_exists:
            os.rename("products.json.backup", "products.json")
