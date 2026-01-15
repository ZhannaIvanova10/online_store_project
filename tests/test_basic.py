"""Базовые тесты для проверки импортов"""

def test_imports():
    """Проверка что основные импорты работают"""
    from src.models import Product, Category
    assert Product is not None
    assert Category is not None
    
    # Проверяем создание объектов
    product = Product("Тест", "Описание", 100, 5)
    assert product.name == "Тест"
    assert product.price == 100
    
    category = Category("Тест", "Описание")
    assert category.name == "Тест"
    assert category.calculate_average_price() == 0


def test_product_exception():
    """Проверка исключения при quantity=0"""
    from src.models import Product
    import pytest
    with pytest.raises(ValueError) as exc_info:
        Product("Тест", "Описание", 100, 0)
    
    assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"


def test_category_average_price():
    """Проверка метода calculate_average_price"""
    from src.models import Category, Product
    
    # Пустая категория
    category = Category("Пустая", "Описание")
    assert category.calculate_average_price() == 0
    
    # Категория с товарами
    products = [
        Product("Т1", "D1", 100, 5),
        Product("Т2", "D2", 200, 3)
    ]
    category2 = Category("С товарами", "Описание", products)
    assert category2.calculate_average_price() == 150.0
