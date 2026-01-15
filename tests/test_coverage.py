"""Тесты для улучшения покрытия"""

from src.models import Smartphone, LawnGrass, BaseProduct, LoggingMixin


def test_smartphone():
    """Тест создания Smartphone"""
    smartphone = Smartphone(
        "iPhone", "Флагман", 99999, 5,
        "Высокая", "15 Pro", 256, "Черный"
    )
    assert smartphone.name == "iPhone"
    assert smartphone.price == 99999
    assert smartphone.quantity == 5
    assert smartphone.model == "15 Pro"
    assert smartphone.memory == 256
def test_lawn_grass():
    """Тест создания LawnGrass"""
    grass = LawnGrass(
        "Газонная трава", "Премиум", 5000, 20,
        "Германия", "14 дней", "Изумрудный"
    )
    assert grass.name == "Газонная трава"
    assert grass.price == 5000
    assert grass.quantity == 20
    assert grass.country == "Германия"
    assert grass.germination_period == "14 дней"


def test_smartphone_exception():
    """Проверка что Smartphone наследует исключение"""
    import pytest
    
    with pytest.raises(ValueError) as exc_info:
        Smartphone("Тест", "Описание", 1000, 0, "Высокая", "Модель", 128, "Черный")
    assert "Товар с нулевым количеством не может быть добавлен" in str(exc_info.value)


def test_lawn_grass_exception():
    """Проверка что LawnGrass наследует исключение"""
    import pytest
    
    with pytest.raises(ValueError) as exc_info:
        LawnGrass("Тест", "Описание", 1000, 0, "Россия", "14 дней", "Зеленый")
    
    assert "Товар с нулевым количеством не может быть добавлен" in str(exc_info.value)


def test_base_product_abc():
    """Проверка что BaseProduct является абстрактным классом"""
    import pytest
    from abc import ABC
    
    assert issubclass(BaseProduct, ABC)
    
    # Нельзя создать экземпляр абстрактного класса
    with pytest.raises(TypeError):
        BaseProduct("Тест", "Описание", 100, 5)
def test_category_methods():
    """Тест методов Category"""
    from src.models import Category, Product
    
    category = Category("Тест", "Описание")
    
    # Проверяем свойства
    assert category.name == "Тест"
    assert category.description == "Описание"
    assert category.products == []  # Пустой список для пустой категории
    
    # Добавляем товар
    product = Product("Товар", "Описание", 100, 5)
    category.add_product(product)
    
    # Проверяем что products property возвращает строку
    products_str = category.products
    # Проверяем что products property возвращает список
    products_list = category.products
    assert len(products_list) == 1
    assert products_list[0].name == "Товар"
    # Проверяем get_products
    products_list = category.products
    assert len(products_list) == 1
    assert products_list[0].name == "Товар"
