import sys
import os

# Добавляем путь к src в PYTHONPATH для импорта
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.models import Product, Category


def test_product_initialization():
    """Тест корректности инициализации объекта Product."""
    product = Product("Тестовый товар", "Описание", 100.50, 5)

    assert product.name == "Тестовый товар"
    assert product.description == "Описание"
    assert product.price == 100.50
    assert product.quantity == 5


def test_category_initialization():
    """Тест корректности инициализации объекта Category."""
    product1 = Product("Товар 1", "Описание 1", 100, 2)
    product2 = Product("Товар 2", "Описание 2", 200, 3)

    category = Category("Тестовая категория", "Описание", [product1, product2])

    assert category.name == "Тестовая категория"
    assert category.description == "Описание"
    assert len(category.products) == 2
    assert isinstance(category.products[0], Product)


def test_category_count():
    """Тест подсчета количества категорий."""
    # Сбрасываем счетчик для чистоты теста
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Товар 1", "Описание", 100, 1)
    product2 = Product("Товар 2", "Описание", 200, 2)

    category1 = Category("Категория 1", "Описание", [product1])
    assert Category.category_count == 1

    category2 = Category("Категория 2", "Описание", [product2])
    assert Category.category_count == 2


def test_product_count():
    """Тест подсчета количества товаров."""
    # Сбрасываем счетчик
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Товар 1", "Описание", 100, 1)
    product2 = Product("Товар 2", "Описание", 200, 2)
    product3 = Product("Товар 3", "Описание", 300, 3)

    category1 = Category("Категория 1", "Описание", [product1, product2])
    assert Category.product_count == 2

    category2 = Category("Категория 2", "Описание", [product3])
    assert Category.product_count == 3


def test_empty_category():
    """Тест создания категории без товаров."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Пустая категория", "Описание", [])

    assert category.name == "Пустая категория"
    assert len(category.products) == 0
    assert Category.category_count == 1
    assert Category.product_count == 0
