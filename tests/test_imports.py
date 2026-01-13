"""
Тесты для проверки импортов.
"""
import sys
import os

# Добавляем путь к src в PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_import_product():
    """Тест импорта класса Product."""
    from src.models import Product
    assert Product is not None
    
    # Проверяем, что класс можно инстанцировать
    product = Product("Test", "Description", 100.0, 5)
    assert product.name == "Test"
    assert product.price == 100.0
def test_import_category():
    """Тест импорта класса Category."""
    from src.models import Category
    assert Category is not None
    
    # Проверяем, что класс можно инстанцировать
    from src.models import Product
    product = Product("Test", "Desc", 50.0, 2)
    category = Category("Test Category", "Desc", [product])
    assert category.name == "Test Category"


def test_import_load_function():
    """Тест импорта функции load_categories_from_json."""
    from src.models import load_categories_from_json
    assert load_categories_from_json is not None
    assert callable(load_categories_from_json)


def test_import_main_functions():
    """Тест импорта функций из main.py."""
    from src.main import main, load_and_print_json_data
    assert main is not None
    assert load_and_print_json_data is not None
    assert callable(main)
    assert callable(load_and_print_json_data)
