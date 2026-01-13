"""
Тесты для проверки новой функциональности с приватными атрибутами.
"""

import sys
import os
import io
from contextlib import redirect_stdout

# Добавляем путь к src в PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models import Product, Category


def test_product_private_price():
    """Тест приватного атрибута цены."""
    product = Product("Тест", "Описание", 100, 5)
    
    # Проверяем что атрибут приватный
    assert hasattr(product, '_Product__price'), "Атрибут __price должен быть приватным"
    assert product.price == 100, "Геттер должен возвращать цену"
def test_price_setter_validation():
    """Тест сеттера цены с валидацией."""
    product = Product("Тест", "Описание", 100, 5)
    
    # Захватываем вывод
    f = io.StringIO()
    with redirect_stdout(f):
        # Пытаемся установить отрицательную цену
        product.price = -50
    
    output = f.getvalue()
    assert "Цена не должна быть нулевая или отрицательная" in output
    assert product.price == 100, "Цена не должна измениться при отрицательном значении"
    
    # Устанавливаем корректную цену
    product.price = 150
    assert product.price == 150, "Цена должна измениться при корректном значении"
def test_category_private_products():
    """Тест приватного атрибута продуктов в категории."""
    category = Category("Тест", "Описание")
    
    # Проверяем что атрибут приватный
    assert hasattr(category, '_Category__products'), "Атрибут __products должен быть приватным"


def test_add_product_method():
    """Тест метода add_product."""
    category = Category("Тест", "Описание")
    product = Product("Тест", "Описание", 100, 5)
    
    # Изначально категория пустая
    assert category.products == ""
    
    # Добавляем продукт
    category.add_product(product)
    
    # Проверяем через геттер
    products_str = category.products
    assert "Тест, 100 руб. Остаток: 5 шт." in products_str
def test_products_getter():
    """Тест геттера products в Category."""
    product1 = Product("Товар 1", "Описание 1", 100, 5)
    product2 = Product("Товар 2", "Описание 2", 200, 10)
    
    category = Category("Тест", "Описание", [product1, product2])
    
    # Проверяем формат вывода
    products_str = category.products
    assert "Товар 1, 100 руб. Остаток: 5 шт." in products_str
    assert "Товар 2, 200 руб. Остаток: 10 шт." in products_str


def test_new_product_classmethod():
    """Тест класс-метода new_product."""
    product_data = {
        "name": "Новый товар",
        "description": "Описание",
        "price": 100.0,
        "quantity": 5
    }
    
    product = Product.new_product(product_data)
    assert isinstance(product, Product)
    assert product.name == "Новый товар"
    assert product.price == 100.0
    assert product.quantity == 5


def test_new_product_with_duplicates():
    """Тест класс-метода new_product с проверкой дубликатов."""
    # Создаем список существующих товаров
    existing_product = Product("Товар 1", "Описание", 100, 5)
    products_list = [existing_product]
    
    # Пытаемся создать дубликат
    duplicate_data = {
        "name": "Товар 1",
        "description": "Другое описание",
        "price": 150,
        "quantity": 3
    }
    
    result = Product.new_product(duplicate_data, products_list)
    # Проверяем что вернулся существующий товар
    assert result is existing_product
    # Количество должно сложиться
    assert existing_product.quantity == 8
    # Цена должна быть выбрана максимальная
    assert existing_product.price == 150


def test_product_counter_in_add_product():
    """Тест счетчика продуктов в методе add_product."""
    # Сбрасываем счетчики
    Category.category_count = 0
    Category.product_count = 0
    
    category = Category("Тест", "Описание")
    product1 = Product("Товар 1", "Описание", 100, 5)
    product2 = Product("Товар 2", "Описание", 200, 10)
    
    # Добавляем продукты
    category.add_product(product1)
    assert Category.product_count == 1
    
    category.add_product(product2)
    assert Category.product_count == 2
def test_product_str_representation():
    """Тест строкового представления товара."""
    product = Product("Тест", "Описание", 100, 5)
    str_repr = str(product)
    
    assert "Тест, 100 руб. Остаток: 5 шт." in str_repr


def test_category_str_representation():
    """Тест строкового представления категории."""
    product = Product("Тест", "Описание", 100, 5)
    category = Category("Категория", "Описание", [product])
    
    str_repr = str(category)
    assert "Категория, количество продуктов: 1" in str_repr


if __name__ == "__main__":
    # Запуск тестов вручную
    test_product_private_price()
    print("✓ test_product_private_price пройден")
    test_price_setter_validation()
    print("✓ test_price_setter_validation пройден")
    
    test_category_private_products()
    print("✓ test_category_private_products пройден")
    
    test_add_product_method()
    print("✓ test_add_product_method пройден")
    
    test_products_getter()
    print("✓ test_products_getter пройден")
    
    test_new_product_classmethod()
    print("✓ test_new_product_classmethod пройден")
    
    test_new_product_with_duplicates()
    print("✓ test_new_product_with_duplicates пройден")
    
    test_product_counter_in_add_product()
    print("✓ test_product_counter_in_add_product пройден")
    
    test_product_str_representation()
    print("✓ test_product_str_representation пройден")
    test_category_str_representation()
    print("✓ test_category_str_representation пройден")
    
    print("\n✅ Все тесты пройдены!")
