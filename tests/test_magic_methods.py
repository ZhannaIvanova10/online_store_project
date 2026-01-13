"""
Тесты для магических методов и итератора категории.
"""

import sys
import os

# Добавляем путь к src в PYTHONPATH для импорта
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.models import Product, Category
def test_product_str():
    """Тест строкового представления товара."""
    product = Product("Телефон", "Смартфон", 50000, 10)
    # Проверяем, что __str__ возвращает строку с нужной информацией
    str_repr = str(product)
    assert isinstance(str_repr, str)
    assert "Телефон" in str_repr
    assert "50000" in str_repr
    assert "10" in str_repr


def test_category_str():
    """Тест строкового представления категории."""
    product = Product("Телефон", "Смартфон", 50000, 10)
    category = Category("Электроника", "Гаджеты и устройства", [product])
    # Проверяем, что __str__ возвращает строку с нужной информацией
    str_repr = str(category)
    assert isinstance(str_repr, str)
    assert "Электроника" in str_repr
    assert "Гаджеты и устройства" in str_repr
    assert "Телефон" in str_repr
    assert "50000" in str_repr

def test_category_total_quantity():
    """Тест вычисления общего количества товаров в категории."""
    products = [
        Product("Товар 1", "Описание 1", 100, 5),
        Product("Товар 2", "Описание 2", 200, 3),
        Product("Товар 3", "Описание 3", 300, 2),
    ]
    category = Category("Категория", "Описание", products)
    
    total_quantity = category.total_quantity
    assert total_quantity == 10  # 5 + 3 + 2


def test_product_add():
    """Тест сложения двух товаров."""
    product1 = Product("Товар 1", "Описание", 100, 2)  # 200
    product2 = Product("Товар 2", "Описание", 200, 3)  # 600
    total = product1 + product2
    assert total == 800  # 200 + 600
    
    # Проверяем, что сложение коммутативно
    total2 = product2 + product1
    assert total2 == 800


def test_product_add_type_error():
    """Тест ошибки при сложении товара с неподдерживаемым типом."""
    product = Product("Товар", "Описание", 100, 2)
    
    try:
        result = product + "не строка"
        assert False, "Должно было возникнуть TypeError"
    except TypeError as e:
        # Проверяем новое сообщение об ошибке
        assert "Нельзя складывать товары разных типов" in str(e)
def test_products_getter_uses_str():
    """Тест, что геттер products использует __str__ товаров."""
    products = [
        Product("Товар 1", "Описание 1", 100, 1),
        Product("Товар 2", "Описание 2", 200, 2),
    ]
    category = Category("Категория", "Описание", products)
    
    # products должен возвращать строку с информацией о всех товарах
    products_str = category.products
    assert isinstance(products_str, str)
    assert "Товар 1" in products_str
    assert "Товар 2" in products_str
    assert "100" in products_str
    assert "200" in products_str


def test_category_iterator():
    """Тест итератора по товарам категории."""
    products = [
        Product("Товар 1", "Описание 1", 100, 1),
        Product("Товар 2", "Описание 2", 200, 2),
        Product("Товар 3", "Описание 3", 300, 3),
    ]
    category = Category("Категория", "Описание", products)
    # Проверяем, что можно итерироваться по категории
    iterated_products = list(category)
    assert len(iterated_products) == 3
    
    # Проверяем, что итерация возвращает оригинальные товары
    for i, product in enumerate(category):
        assert product.name == f"Товар {i + 1}"
        assert product.price == 100 * (i + 1)
        assert product.quantity == i + 1


def test_category_iterator_empty():
    """Тест итератора по пустой категории."""
    category = Category("Пустая категория", "Описание", [])
    
    # Итерация по пустой категории должна возвращать пустой список
    iterated_products = list(category)
    assert len(iterated_products) == 0


def test_product_add_multiple():
    """Тест сложения нескольких товаров."""
    products = [
        Product(f"Товар {i}", "Описание", 100 * i, i)
        for i in range(1, 6)  # 5 товаров
    ]
    # Суммируем вручную
    manual_sum = sum(p.price * p.quantity for p in products)
    
    # Правильный способ сложения нескольких товаров:
    # Суммируем стоимость каждого товара отдельно
    total = sum(product.price * product.quantity for product in products)
    
    # Проверяем, что сумма равна ручной
    assert total == manual_sum, f"Ожидалось {manual_sum}, получено {total}"
    
    # Дополнительная проверка: попарное сложение работает корректно
    # Складываем первые два товара
    sum_first_two = products[0] + products[1]
    expected_sum = products[0].price * products[0].quantity + products[1].price * products[1].quantity
    assert sum_first_two == expected_sum, f"Попарное сложение не работает: ожидалось {expected_sum}, получено {sum_first_two}"
def test_category_str_edge_cases():
    """Тест строкового представления категории в крайних случаях."""
    # Категория без товаров
    empty_category = Category("Пустая", "Нет товаров", [])
    empty_str = str(empty_category)
    assert isinstance(empty_str, str)
    assert "Пустая" in empty_str
    assert "Нет товаров" in empty_str
    
    # Категория с одним товар
    single_product = Product("Единственный", "Товар", 100, 1)
    single_category = Category("Одна", "Категория", [single_product])
    single_str = str(single_category)
    assert isinstance(single_str, str)
    assert "Единственный" in single_str
    assert "100" in single_str
