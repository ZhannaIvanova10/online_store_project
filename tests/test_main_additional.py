"""
Дополнительные тесты для основного модуля.
"""

import sys
import os
import tempfile
import json

# Добавляем путь к src в PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.main import create_sample_data, print_store_info, load_and_print_json_data
from src.models import Category
from io import StringIO
import contextlib


def test_create_sample_data():
    """Тест создания примерных данных."""
    # Сбрасываем счетчики
    Category.category_count = 0
    Category.product_count = 0
    
    categories = create_sample_data()
    # Проверяем результаты
    assert len(categories) == 2
    assert categories[0].name == "Электроника"
    assert categories[1].name == "Книги"
    
    # Проверяем товары в первой категории
    products_str = categories[0].products
    assert "Ноутбук" in products_str
    assert "Смартфон" in products_str
    assert "Планшет" in products_str
    
    # Проверяем товары во второй категории
    products_str2 = categories[1].products
    assert "Python для начинающих" in products_str2
    assert "Алгоритмы и структуры данных" in products_str2
    
    # Проверяем счетчики
    assert Category.category_count == 2
    assert Category.product_count == 5
def test_print_store_info():
    """Тест вывода информации о магазине."""
    # Сбрасываем счетчики
    Category.category_count = 0
    Category.product_count = 0
    
    categories = create_sample_data()
    
    # Перенаправляем stdout
    output = StringIO()
    with contextlib.redirect_stdout(output):
        print_store_info(categories)
    
    captured_output = output.getvalue()
    
    # Проверяем вывод
    assert "ИНФОРМАЦИЯ О МАГАЗИНЕ" in captured_output
    assert "Всего категорий: 2" in captured_output
    assert "Всего товаров: 5" in captured_output
    assert "Электроника" in captured_output
    assert "Книги" in captured_output
    assert "Ноутбук" in captured_output
    assert "Python для начинающих" in captured_output

def test_load_and_print_json_data_output():
    """Тест вывода при загрузке из JSON файла."""
    # Создаем тестовый JSON файл
    test_data = [
        {
            "name": "Test Category",
            "description": "Test description",
            "products": [
                {
                    "name": "Test Product",
                    "description": "Test product description",
                    "price": 100.0,
                    "quantity": 5,
                }
            ],
        }
    ]
    temp_file = tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, encoding="utf-8"
    )
    json.dump(test_data, temp_file, ensure_ascii=False)
    temp_file.close()
    
    try:
        # Перенаправляем stdout
        output = StringIO()
        with contextlib.redirect_stdout(output):
            load_and_print_json_data(temp_file.name)
        
        captured_output = output.getvalue()
        
        # Проверяем вывод
        assert "Загрузка данных из файла" in captured_output
        assert "Test Category" in captured_output
        assert "Test description" in captured_output
        assert "Test Product" in captured_output
        assert "100.0" in captured_output
        
    finally:
        if os.path.exists(temp_file.name):
            os.unlink(temp_file.name)
