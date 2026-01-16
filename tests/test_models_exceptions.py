"""
Тесты для проверки обработки исключений.
"""
import pytest
from src.models import BaseProduct, Category


def test_product_zero_quantity():
    """Тест создания продукта с нулевым количеством."""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        BaseProduct("Тест", "Описание", 100, 0)
def test_product_negative_quantity():
    """Тест создания продукта с отрицательным количеством."""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        BaseProduct("Тест", "Описание", 100, -1)


def test_product_valid_quantity():
    """Тест создания продукта с валидным количеством."""
    product = BaseProduct("Тест", "Описание", 100, 10)
    assert product.name == "Тест"
    assert product.price == 100
    assert product.quantity == 10


def test_category_add_non_product():
    """Тест добавления не-продукта в категорию."""
    category = Category("Тест", "Описание")
    with pytest.raises(TypeError):
        category.add_product("не продукт")
def test_category_average_price_empty():
    """Тест средней цены пустой категории."""
    category = Category("Тест", "Описание")
    assert category.average_price() == 0


def test_category_average_price_with_products():
    """Тест средней цены категории с товарами."""
    category = Category("Тест", "Описание")
    product1 = BaseProduct("Товар1", "Описание", 100, 5)
    product2 = BaseProduct("Товар2", "Описание", 300, 3)
    category.add_product(product1)
    category.add_product(product2)
    
    # (100 + 300) / 2 = 200
    assert category.average_price() == 200


def test_category_products_count():
    """Тест подсчета товаров в категории."""
    category = Category("Тест", "Описание")
    assert category.get_products_count() == 0
    product = BaseProduct("Товар", "Описание", 100, 5)
    category.add_product(product)
    assert category.get_products_count() == 1


def test_category_contains():
    """Тест проверки наличия товара в категории."""
    category = Category("Тест", "Описание")
    product = BaseProduct("Товар", "Описание", 100, 5)
    category.add_product(product)
    
    assert product in category
    assert BaseProduct("Другой", "Описание", 200, 3) not in category
