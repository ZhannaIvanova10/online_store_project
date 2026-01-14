"""
Тесты для абстрактных классов и миксинов.
"""

import sys
import os
import io
import contextlib

# Добавляем путь к src в PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.models import BaseProduct, Product, Smartphone, LawnGrass, LoggingMixin, OrderItem
import pytest


def test_base_product_is_abstract():
    """Тест, что BaseProduct является абстрактным классом."""
    # Нельзя создать экземпляр абстрактного класса
    with pytest.raises(TypeError):
        BaseProduct("Test", "Description", 100, 5)


def test_product_inherits_from_base_product():
    """Тест, что Product наследует от BaseProduct."""
    product = Product("Тест", "Описание", 100, 5)
    
    assert isinstance(product, BaseProduct)
    assert isinstance(product, Product)
    # Проверяем наличие методов абстрактного класса
    assert hasattr(product, 'get_total_cost')
    assert hasattr(product, 'increase_quantity')
    assert hasattr(product, 'decrease_quantity')


def test_logging_mixin_functionality():
    """Тест функциональности миксина LoggingMixin."""
    # Перенаправляем stdout для захвата вывода
    output = io.StringIO()
    
    with contextlib.redirect_stdout(output):
        product = Product("Тестовый товар", "Описание", 1000, 10)
    
    captured_output = output.getvalue()
    
    # Проверяем, что вывод содержит информацию о создании объекта
    assert "Создан объект: Product" in captured_output
    assert "name='Тестовый товар'" in captured_output
    assert "price=1000" in captured_output
    assert "quantity=10" in captured_output
def test_logging_mixin_with_smartphone():
    """Тест миксина LoggingMixin со смартфоном."""
    output = io.StringIO()
    
    with contextlib.redirect_stdout(output):
        smartphone = Smartphone(
            name="Тестовый смартфон",
            description="Описание",
            price=50000,
            quantity=3,
            efficiency="Высокая",
            model="Model X",
            memory=128,
            color="Черный"
        )
    
    captured_output = output.getvalue()
    
    assert "Создан объект: Smartphone" in captured_output
    assert "name='Тестовый смартфон'" in captured_output
    assert "model='Model X'" in captured_output
    assert "memory=128" in captured_output
def test_logging_mixin_with_lawn_grass():
    """Тест миксина LoggingMixin с газонной травой."""
    output = io.StringIO()
    
    with contextlib.redirect_stdout(output):
        lawn_grass = LawnGrass(
            name="Тестовая трава",
            description="Описание",
            price=1500,
            quantity=20,
            country="Россия",
            germination_period=10,
            color="Зеленый"
        )
    
    captured_output = output.getvalue()
    
    assert "Создан объект: LawnGrass" in captured_output
    assert "name='Тестовая трава'" in captured_output
    assert "country='Россия'" in captured_output
    assert "germination_period=10" in captured_output
def test_base_product_methods():
    """Тест методов абстрактного класса BaseProduct."""
    product = Product("Товар", "Описание", 100, 10)
    
    # Тест get_total_cost
    assert product.get_total_cost() == 1000  # 100 * 10
    
    # Тест increase_quantity
    assert product.increase_quantity(5) == True
    assert product.quantity == 15
    
    # Тест decrease_quantity
    assert product.decrease_quantity(3) == True
    assert product.quantity == 12
    
    # Тест decrease_quantity с некорректным значением
    assert product.decrease_quantity(20) == False  # Нельзя уменьшить на больше, чем есть
    assert product.quantity == 12  # Количество не изменилось
    
    assert product.decrease_quantity(0) == False  # Нельзя уменьшить на 0
    assert product.decrease_quantity(-5) == False  # Нельзя уменьшить на отрицательное число
def test_repr_methods():
    """Тест методов __repr__ для классов."""
    product = Product("Товар", "Описание", 100, 5)
    smartphone = Smartphone(
        name="Смартфон",
        description="Описание",
        price=50000,
        quantity=2,
        efficiency="Высокая",
        model="Model X",
        memory=128,
        color="Черный"
    )
    
    product_repr = repr(product)
    smartphone_repr = repr(smartphone)
    
    assert "Product(" in product_repr
    assert "name='Товар'" in product_repr
    assert "price=100" in product_repr
    
    assert "Smartphone(" in smartphone_repr
    assert "model='Model X'" in smartphone_repr
    assert "memory=128" in smartphone_repr
def test_order_item_class():
    """Тест класса OrderItem (дополнительное задание)."""
    product = Product("Товар", "Описание", 100, 10)
    order_item = OrderItem(product, 3)
    
    assert order_item.product == product
    assert order_item.quantity == 3
    assert order_item.total_cost == 300  # 100 * 3
    
    # Проверяем строковое представление
    order_str = str(order_item)
    assert "Товар x 3 = 300 руб." in order_str
    
    # Проверяем представление для отладки
    order_repr = repr(order_item)
    assert "OrderItem(" in order_repr
    assert "quantity=3" in order_repr


def test_inheritance_hierarchy():
    """Тест иерархии наследования."""
    product = Product("Тест", "Описание", 100, 1)
    smartphone = Smartphone(
        name="Тест", 
        description="Тест", 
        price=100, 
        quantity=1,
        efficiency="A", 
        model="X", 
        memory=64, 
        color="Black"
    )
    # Проверяем наследование
    assert isinstance(product, BaseProduct)
    assert isinstance(smartphone, BaseProduct)
    assert isinstance(smartphone, Product)
    
    # Product должен иметь LoggingMixin в цепочке наследования
    assert LoggingMixin in Product.__bases__ or any(LoggingMixin in cls.__bases__ for cls in Product.mro())


def test_abstract_methods_implementation():
    """Тест, что абстрактные методы реализованы в наследниках."""
    product = Product("Тест", "Описание", 100, 5)
    smartphone = Smartphone(
        name="Тест", 
        description="Тест", 
        price=100, 
        quantity=1,
        efficiency="A", 
        model="X", 
        memory=64, 
        color="Black"
    )
    
    # Проверяем, что абстрактные методы работают
    assert str(product) is not None
    assert str(smartphone) is not None
    # Проверяем сложение
    product2 = Product("Тест2", "Описание", 200, 3)
    total = product + product2
    assert total == 100 * 5 + 200 * 3


def test_backward_compatibility():
    """Тест обратной совместимости."""
    # Старый код должен работать
    product = Product("Старый товар", "Описание", 100, 5)
    assert product.name == "Старый товар"
    assert product.price == 100
    assert product.quantity == 5
    
    smartphone = Smartphone(
        name="Старый смартфон",
        description="Описание",
        price=50000,
        quantity=2,
        efficiency="Старая",
        model="Old",
        memory=64,
        color="Black"
    )
    assert smartphone.name == "Старый смартфон"
    assert smartphone.model == "Old"
    assert smartphone.memory == 64
    
    # Сложение должно работать
    product2 = Product("Товар 2", "Описание", 200, 3)
    total = product + product2
    assert total == 100 * 5 + 200 * 3
