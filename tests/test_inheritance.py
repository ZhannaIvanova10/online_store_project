"""
Тесты для классов-наследников и ограничений.
"""

import sys
import os

# Добавляем путь к src в PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.models import Product, Smartphone, LawnGrass, Category
import pytest


def test_smartphone_creation():
    """Тест создания объекта Smartphone."""
    phone = Smartphone(
        name="iPhone 15 Pro",
        description="Флагманский смартфон Apple",
        price=129999,
        quantity=10,
        efficiency="A17 Pro",
        model="iPhone 15 Pro",
        memory=256,
        color="Титановый синий"
    )
    
    assert phone.name == "iPhone 15 Pro"
    assert phone.price == 129999
    assert phone.quantity == 10
    assert phone.efficiency == "A17 Pro"
    assert phone.model == "iPhone 15 Pro"
    assert phone.memory == 256
    assert phone.color == "Титановый синий"
    assert isinstance(phone, Product)
def test_lawn_grass_creation():
    """Тест создания объекта LawnGrass."""
    grass = LawnGrass(
        name="Газонная трава Премиум",
        description="Высококачественная газонная трава",
        price=1500,
        quantity=50,
        country="Германия",
        germination_period=14,
        color="Ярко-зеленый"
    )
    
    assert grass.name == "Газонная трава Премиум"
    assert grass.price == 1500
    assert grass.quantity == 50
    assert grass.country == "Германия"
    assert grass.germination_period == 14
    assert grass.color == "Ярко-зеленый"
    assert isinstance(grass, Product)
def test_product_str_method_inheritance():
    """Тест, что __str__ работает для наследников."""
    phone = Smartphone(
        name="Тестовый телефон",
        description="Тест",
        price=1000,
        quantity=5,
        efficiency="Тест",
        model="Модель X",
        memory=128,
        color="Черный"
    )
    
    grass = LawnGrass(
        name="Тестовая трава",
        description="Тест",
        price=500,
        quantity=10,
        country="Россия",
        germination_period=7,
        color="Зеленый"
    )
    phone_str = str(phone)
    grass_str = str(grass)
    
    assert "Тестовый телефон" in phone_str
    assert "Модель: Модель X" in phone_str
    assert "Память: 128 ГБ" in phone_str
    
    assert "Тестовая трава" in grass_str
    assert "Страна: Россия" in grass_str
    assert "Прорастание: 7 дней" in grass_str


def test_add_same_class_products():
    """Тест сложения товаров одного класса."""
    phone1 = Smartphone(
        name="Phone 1",
        description="Тест",
        price=1000,
        quantity=2,
        efficiency="A",
        model="X",
        memory=64,
        color="Black"
    )
    phone2 = Smartphone(
        name="Phone 2",
        description="Тест",
        price=2000,
        quantity=3,
        efficiency="B",
        model="Y",
        memory=128,
        color="White"
    )
    
    total = phone1 + phone2
    assert total == 1000 * 2 + 2000 * 3  # 2000 + 6000 = 8000
    
    grass1 = LawnGrass(
        name="Grass 1",
        description="Тест",
        price=500,
        quantity=5,
        country="RU",
        germination_period=10,
        color="Green"
    )
    grass2 = LawnGrass(
        name="Grass 2",
        description="Тест",
        price=300,
        quantity=4,
        country="DE",
        germination_period=14,
        color="Dark Green"
    )
    
    total_grass = grass1 + grass2
    assert total_grass == 500 * 5 + 300 * 4  # 2500 + 1200 = 3700


def test_add_different_class_products():
    """Тест ошибки при сложении товаров разных классов."""
    phone = Smartphone(
        name="Phone",
        description="Тест",
        price=1000,
        quantity=1,
        efficiency="A",
        model="X",
        memory=64,
        color="Black"
    )
    grass = LawnGrass(
        name="Grass",
        description="Тест",
        price=500,
        quantity=2,
        country="RU",
        germination_period=10,
        color="Green"
    )
    
    with pytest.raises(TypeError) as exc_info:
        result = phone + grass
    
    assert "Нельзя складывать товары разных типов" in str(exc_info.value)
    assert "Smartphone" in str(exc_info.value)
    assert "LawnGrass" in str(exc_info.value)


def test_add_product_with_base_product():
    """Тест сложения базового Product с наследником."""
    base_product = Product(
        name="Базовый товар",
        description="Тест",
        price=1000,
        quantity=3
    )
    phone = Smartphone(
        name="Phone",
        description="Тест",
        price=2000,
        quantity=2,
        efficiency="A",
        model="X",
        memory=64,
        color="Black"
    )
    
    with pytest.raises(TypeError) as exc_info:
        result = base_product + phone
    
    assert "Нельзя складывать товары разных типов" in str(exc_info.value)


def test_category_add_product_method():
    """Тест метода add_product с проверкой типа."""
    category = Category("Тест", "Тестовая категория")
    
    # Можно добавлять Product
    product = Product("Товар", "Описание", 100, 5)
    category.add_product(product)
    assert len(category._products) == 1
    # Можно добавлять Smartphone
    phone = Smartphone(
        name="Смартфон", 
        description="Тест", 
        price=1000, 
        quantity=2,
        efficiency="A", 
        model="X", 
        memory=64, 
        color="Black"
    )
    category.add_product(phone)
    assert len(category._products) == 2
    
    # Можно добавлять LawnGrass
    grass = LawnGrass(
        name="Трава", 
        description="Тест", 
        price=500, 
        quantity=3,
        country="RU", 
        germination_period=10, 
        color="Green"
    )
    category.add_product(grass)
    assert len(category._products) == 3


def test_category_add_product_type_error():
    """Тест ошибки при добавлении не-продукта в категорию."""
    category = Category("Тест", "Тестовая категория")
    
    # Нельзя добавлять строку
    with pytest.raises(TypeError) as exc_info:
        category.add_product("не продукт")
    
    assert "Можно добавлять только продукты" in str(exc_info.value)
    
    # Нельзя добавлять число
    with pytest.raises(TypeError) as exc_info:
        category.add_product(123)
    
    assert "Можно добавлять только продукты" in str(exc_info.value)
    
    # Нельзя добавлять список
    with pytest.raises(TypeError) as exc_info:
        category.add_product([1, 2, 3])
    
    assert "Можно добавлять только продукты" in str(exc_info.value)
def test_inheritance_hierarchy():
    """Тест иерархии наследования."""
    phone = Smartphone(
        name="Тест", 
        description="Тест", 
        price=100, 
        quantity=1,
        efficiency="A", 
        model="X", 
        memory=64, 
        color="Black"
    )
    
    grass = LawnGrass(
        name="Тест", 
        description="Тест", 
        price=100, 
        quantity=1,
        country="RU", 
        germination_period=10, 
        color="Green"
    )
    
    # Проверяем наследование
    assert isinstance(phone, Smartphone)
    assert isinstance(phone, Product)
    assert isinstance(grass, LawnGrass)
    assert isinstance(grass, Product)
    
    # Проверяем, что это не базовый класс
    assert not isinstance(phone, LawnGrass)
    assert not isinstance(grass, Smartphone)
    
    # Проверяем классы
    assert issubclass(Smartphone, Product)
    assert issubclass(LawnGrass, Product)


def test_json_loading_with_inheritance():
    """Тест загрузки JSON с разными типами продуктов."""
    import json
    import tempfile
    
    test_data = [
        {
            "name": "Электроника",
            "description": "Техника",
            "products": [
                {
                    "name": "Смартфон",
                    "description": "Телефон",
                    "price": 1000,
                    "quantity": 5,
                    "model": "Model X",
                    "memory": 128,
                    "efficiency": "Высокая",
                    "color": "Черный"
                },
                {
                    "name": "Ноутбук",
                    "description": "Компьютер",
                    "price": 2000,
                    "quantity": 3
                }
            ]
        },
        {
            "name": "Сад",
            "description": "Для сада",
            "products": [
                {
                    "name": "Газонная трава",
                    "description": "Трава",
                    "price": 500,
                    "quantity": 10,
                    "country": "Германия",
                    "germination_period": 14,
                    "color": "Зеленый"
                }
            ]
        }
    ]
    
    temp_file = tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, encoding="utf-8"
    )
    json.dump(test_data, temp_file, ensure_ascii=False)
    temp_file.close()
    
    try:
        from src.models import load_categories_from_json
        categories = load_categories_from_json(temp_file.name)
        
        assert len(categories) == 2
        
        # Проверяем типы продуктов
        electronics_products = categories[0]._products
        assert isinstance(electronics_products[0], Smartphone)
        assert isinstance(electronics_products[1], Product)
        
        garden_products = categories[1]._products
        assert isinstance(garden_products[0], LawnGrass)
        
    finally:
        if os.path.exists(temp_file.name):
            os.unlink(temp_file.name)
def test_backward_compatibility():
    """Тест обратной совместимости со старым кодом."""
    # Старый код должен работать
    product = Product("Старый товар", "Описание", 100, 5)
    assert product.name == "Старый товар"
    assert product.price == 100
    assert product.quantity == 5
    
    category = Category("Старая категория", "Описание", [product])
    assert category.name == "Старая категория"
    assert len(category._products) == 1
    
    # Сложение старых продуктов должно работать
    product2 = Product("Товар 2", "Описание", 200, 3)
    total = product + product2
    assert total == 100 * 5 + 200 * 3
