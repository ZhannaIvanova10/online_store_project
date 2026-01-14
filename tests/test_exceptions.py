"""
Тесты для обработки исключений.
"""

import sys
import os
import io
import contextlib

# Добавляем путь к src в PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.models import Product, Category, ZeroQuantityError, OrderItem
import pytest


def test_product_zero_quantity_exception():
    """Тест исключения при создании товара с нулевым количеством."""
    # Задание 1: ValueError при quantity=0
    with pytest.raises(ValueError) as exc_info:
        Product("Тестовый товар", "Описание", 100, 0)
    
    assert "Товар с нулевым количеством не может быть добавлен" in str(exc_info.value)
def test_product_valid_quantity():
    """Тест создания товара с корректным количеством."""
    # Товар с положительным количеством должен создаваться успешно
    product = Product("Тестовый товар", "Описание", 100, 5)
    assert product.name == "Тестовый товар"
    assert product.price == 100
    assert product.quantity == 5


def test_get_average_price_with_products():
    """Тест метода get_average_price с товарами в категории."""
    # Задание 2: Метод подсчета средней цены
    products = [
        Product("Товар 1", "Описание", 100, 2),
        Product("Товар 2", "Описание", 200, 3),
        Product("Товар 3", "Описание", 300, 1),
    ]
    
    category = Category("Тестовая категория", "Описание", products)
    
    # Средняя цена: (100 + 200 + 300) / 3 = 200
    average_price = category.get_average_price()
    assert average_price == 200.0

def test_get_average_price_empty_category():
    """Тест метода get_average_price для пустой категории."""
    # Задание 2: Обработка пустой категории
    empty_category = Category("Пустая категория", "Нет товаров")
    
    # Должен вернуть 0 для пустой категории
    average_price = empty_category.get_average_price()
    assert average_price == 0


def test_get_average_price_zero_division_handling():
    """Тест обработки деления на ноль в get_average_price."""
    # Даже если по какой-то причине len(self._products) == 0
    category = Category("Категория", "Описание")
    
    # Убедимся, что список товаров пуст
    assert len(category._products) == 0
    
    # Метод должен вернуть 0, а не вызвать ZeroDivisionError
    average_price = category.get_average_price()
    assert average_price == 0
def test_category_add_product_zero_quantity():
    """Тест добавления товара с нулевым количеством в категорию."""
    # Дополнительное задание: ZeroQuantityError
    category = Category("Тестовая категория", "Описание")
    
    # Создаем товар, затем меняем количество на 0
    product = Product("Товар", "Описание", 100, 1)
    product.quantity = 0
    
    with pytest.raises(ZeroQuantityError) as exc_info:
        category.add_product(product)
    
    assert "Нельзя добавить товар" in str(exc_info.value)
    assert "с нулевым количеством" in str(exc_info.value)
def test_category_add_product_valid():
    """Тест добавления товара с корректным количеством в категорию."""
    category = Category("Тестовая категория", "Описание")
    product = Product("Товар", "Описание", 100, 5)
    
    # Товар должен добавляться успешно
    category.add_product(product)
    assert len(category._products) == 1
    assert category._products[0] == product


def test_order_item_zero_quantity():
    """Тест создания OrderItem с нулевым количеством."""
    # Дополнительное задание: ZeroQuantityError для OrderItem
    product = Product("Товар", "Описание", 100, 5)
    
    with pytest.raises(ZeroQuantityError) as exc_info:
        OrderItem(product, 0)
    
    assert "Нельзя создать заказ" in str(exc_info.value)
    assert "с нулевым количеством" in str(exc_info.value)
def test_order_item_valid_quantity():
    """Тест создания OrderItem с корректным количеством."""
    product = Product("Товар", "Описание", 100, 5)
    
    # Заказ должен создаваться успешно
    order_item = OrderItem(product, 2)
    
    assert order_item.product == product
    assert order_item.quantity == 2
    assert order_item.total_cost == 200  # 100 * 2


def test_zero_quantity_error_inheritance():
    """Тест, что ZeroQuantityError наследуется от ValueError."""
    # Проверяем иерархию наследования
    assert issubclass(ZeroQuantityError, ValueError)
    
    # Можно поймать как ZeroQuantityError, так и ValueError
    product = Product("Товар", "Описание", 100, 5)
    try:
        OrderItem(product, 0)
    except ZeroQuantityError:
        # Ловим как ZeroQuantityError
        assert True
    except ValueError:
        # Или как ValueError (поскольку ZeroQuantityError наследует от ValueError)
        assert True


def test_get_average_price_various_scenarios():
    """Тест метода get_average_price в различных сценариях."""
    # Сценарий 1: Один товар
    category1 = Category("Категория 1", "Описание", [
        Product("Товар", "Описание", 100, 1)
    ])
    assert category1.get_average_price() == 100.0
    # Сценарий 2: Несколько товаров с разными ценами
    category2 = Category("Категория 2", "Описание", [
        Product("Т1", "Описание", 10, 1),
        Product("Т2", "Описание", 20, 1),
        Product("Т3", "Описание", 30, 1),
    ])
    assert category2.get_average_price() == 20.0  # (10+20+30)/3
    
    # Сценарий 3: Товары с нулевой ценой (если такое возможно)
    category3 = Category("Категория 3", "Описание", [
        Product("Т1", "Описание", 0, 1),
        Product("Т2", "Описание", 0, 1),
    ])
    assert category3.get_average_price() == 0.0


def test_backward_compatibility():
    """Тест обратной совместимости."""
    # Старый код должен работать
    product = Product("Старый товар", "Описание", 100, 5)
    assert product.name == "Старый товар"
    assert product.price == 100
    assert product.quantity == 5
    # Методы должны работать как раньше
    category = Category("Старая категория", "Описание", [product])
    assert category.name == "Старая категория"
    assert len(category._products) == 1
    
    # get_average_price должен работать
    assert category.get_average_price() == 100.0
