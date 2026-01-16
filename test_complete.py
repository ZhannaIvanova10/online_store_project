import pytest
import json
import os
from src.models import BaseProduct, Category, Product, Smartphone, LawnGrass, load_categories_from_json

# Тесты для BaseProduct
def test_base_product_creation():
    """Тест создания базового продукта."""
    p = BaseProduct("Тест", "Описание", 100, 10)
    assert p.name == "Тест"
    assert p.description == "Описание"
    assert p.price == 100
    assert p.quantity == 10

def test_base_product_str():
    """Тест строкового представления."""
    p = BaseProduct("Тест", "Описание", 100, 10)
    assert "Тест" in str(p)
    assert "100" in str(p)
    assert "10" in str(p)
# Тесты для Product
def test_product_creation():
    """Тест создания продукта."""
    p = Product("Тест", "Описание", 100, 10)
    assert isinstance(p, BaseProduct)
    assert p.name == "Тест"

# Тесты для Category
def test_category_creation():
    """Тест создания категории."""
    cat = Category("Тест", "Описание")
    assert cat.name == "Тест"
    assert cat.description == "Описание"
    assert cat.total_products == 0

def test_category_add_product():
    """Тест добавления продукта в категорию."""
    cat = Category("Тест", "Описание")
    p = Product("Товар", "Описание", 100, 5)
    cat.add_product(p)
    assert cat.total_products == 1
    assert p in cat.products
def test_category_add_invalid_product():
    """Тест добавления невалидного продукта."""
    cat = Category("Тест", "Описание")
    with pytest.raises(TypeError):
        cat.add_product("не продукт")

def test_category_len():
    """Тест метода __len__."""
    cat = Category("Тест", "Описание")
    p = Product("Товар", "Описание", 100, 5)
    cat.add_product(p)
    assert len(cat) == 1

def test_category_contains():
    """Тест метода __contains__."""
    cat = Category("Тест", "Описание")
    p = Product("Товар", "Описание", 100, 5)
    cat.add_product(p)
    assert p in cat
    assert Product("Другой", "Описание", 200, 3) not in cat
def test_category_str():
    """Тест строкового представления категории."""
    cat = Category("Тест", "Описание")
    assert "Тест" in str(cat)

# Тесты для average_price
def test_average_price_empty():
    """Тест средней цены пустой категории."""
    cat = Category("Тест", "Описание")
    assert cat.average_price() == 0

def test_average_price_single():
    """Тест средней цены с одним товаром."""
    cat = Category("Тест", "Описание")
    p = Product("Товар", "Описание", 100, 5)
    cat.add_product(p)
    assert cat.average_price() == 100

def test_average_price_multiple():
    """Тест средней цены с несколькими товарами."""
    cat = Category("Тест", "Описание")
    p1 = Product("Товар1", "Описание", 100, 5)
    p2 = Product("Товар2", "Описание", 300, 3)
    cat.add_product(p1)
    cat.add_product(p2)
    assert cat.average_price() == 200
# Тесты для исключений
def test_product_zero_quantity():
    """Тест создания продукта с quantity=0."""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        BaseProduct("Тест", "Описание", 100, 0)

def test_product_negative_quantity():
    """Тест создания продукта с quantity=-1."""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        BaseProduct("Тест", "Описание", 100, -1)

# Тесты для JSON загрузки
def test_load_valid_json(tmp_path):
    """Тест загрузки валидного JSON."""
    test_data = [
        {
            "name": "Электроника",
            "description": "Электронные устройства",
            "products": [
                {
                    "name": "Смартфон",
                    "description": "Мощный смартфон",
                    "price": 29999.99,
                    "quantity": 10
                }
            ]
        }
    ]
    
    test_file = tmp_path / "test.json"
    test_file.write_text(json.dumps(test_data), encoding='utf-8')
    
    categories = load_categories_from_json(str(test_file))
    assert len(categories) == 1
    assert categories[0].name == "Электроника"
    assert categories[0].total_products == 1
def test_load_nonexistent_file():
    """Тест загрузки несуществующего файла."""
    with pytest.raises(FileNotFoundError):
        load_categories_from_json("nonexistent.json")

def test_load_invalid_json(tmp_path):
    """Тест загрузки невалидного JSON."""
    test_file = tmp_path / "test.json"
    test_file.write_text("{ невалидный json }", encoding='utf-8')
    
    with pytest.raises(json.JSONDecodeError):
        load_categories_from_json(str(test_file))
