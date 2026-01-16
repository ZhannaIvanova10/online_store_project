"""
Минимальные тесты для проверки основных критериев.
"""
import pytest
from models import BaseProduct, Category, Product


def test_product_zero_quantity():
    """Тест создания продукта с нулевым количеством."""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        BaseProduct("Тест", "Описание", 100, 0)


def test_product_negative_quantity():
    """Тест создания продукта с отрицательным количеством."""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        BaseProduct("Тест", "Описание", 100, -1)

def test_product_valid():
    """Тест создания валидного продукта."""
    p = BaseProduct("Тест", "Описание", 100, 10)
    assert p.name == "Тест"
    assert p.price == 100
    assert p.quantity == 10


def test_category_average_price_empty():
    """Тест средней цены пустой категории."""
    cat = Category("Тест", "Описание")
    assert cat.average_price() == 0


def test_category_average_price_with_products():
    """Тест средней цены категории с товарами."""
    cat = Category("Тест", "Описание")
    p1 = Product("Товар1", "Описание", 100, 5)
    p2 = Product("Товар2", "Описание", 300, 3)
    cat.add_product(p1)
    cat.add_product(p2)
    assert cat.average_price() == 200  # (100 + 300) / 2


def test_category_total_products():
    """Тест количества товаров в категории."""
    cat = Category("Тест", "Описание")
    assert cat.total_products == 0
    p = Product("Товар", "Описание", 100, 5)
    cat.add_product(p)
    assert cat.total_products == 1
