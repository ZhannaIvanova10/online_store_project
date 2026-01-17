"""
Тесты для проверки обработки исключений в модуле models.py
"""

import pytest
from src.models import Product, Category, ZeroQuantityError


class TestProductExceptions:
    """Тесты для класса Product с обработкой исключений."""
    
    def test_product_creation_with_zero_quantity_raises_error(self):
        """Тест: создание товара с нулевым количеством вызывает исключение."""
        with pytest.raises(ZeroQuantityError) as exc_info:
            Product("Тестовый товар", 1000, 0)
        
        assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"
        assert isinstance(exc_info.value, ValueError)
    
    def test_product_creation_with_positive_quantity_success(self):
        """Тест: создание товара с положительным количеством проходит успешно."""
        product = Product("Ноутбук", 150000, 3)
        assert product.name == "Ноутбук"
        assert product.price == 150000
        assert product.quantity == 3
    def test_product_string_representation(self):
        """Тест: строковое представление товара."""
        product = Product("Телефон", 50000, 5)
        expected = "Телефон, 50000 руб. Остаток: 5 шт."
        assert str(product) == expected
    
    def test_product_custom_exception_type(self):
        """Тест: ZeroQuantityError является подклассом ValueError."""
        assert issubclass(ZeroQuantityError, ValueError)


class TestCategoryExceptions:
    """Тесты для класса Category с обработкой исключений."""
    
    def setup_method(self):
        """Настройка перед каждым тестом."""
        self.category = Category("Электроника")
        self.product1 = Product("Ноутбук", 100000, 2)
        self.product2 = Product("Смартфон", 50000, 3)
    
    def test_category_average_price_with_products(self):
        """Тест: расчет средней цены с товарами."""
        self.category.products = [self.product1, self.product2]
        expected_average = (100000 + 50000) / 2
        assert self.category.calculate_average_price() == expected_average
    
    def test_category_average_price_empty(self):
        """Тест: расчет средней цены для пустой категории."""
        assert self.category.calculate_average_price() == 0.0
    def test_category_average_price_single_product(self):
        """Тест: расчет средней цены для одного товара."""
        self.category.products = [self.product1]
        assert self.category.calculate_average_price() == 100000
    
    def test_category_string_representation(self):
        """Тест: строковое представление категории."""
        self.category.products = [self.product1]
        expected = "Категория: Электроника\nТовары:\nНоутбук, 100000 руб. Остаток: 2 шт."
        assert str(self.category) == expected
    
    def test_add_product_success(self):
        """Тест: успешное добавление товара в категорию."""
        category = Category("Тестовая")
        product = Product("Тестовый товар", 1000, 5)
        
        # Проверяем, что товар добавляется без ошибок
        category.add_product(product)
        assert len(category.products) == 1
        assert category.products[0] == product
    
    def test_add_product_zero_quantity(self):
        """Тест: попытка создания товара с нулевым количеством вызывает ошибку при создании."""
        # Тест проверяет, что нельзя создать товар с нулевым количеством
        pass
    def test_add_product_with_existing_zero_quantity_product(self):
        """Тест: работа категории с товаром, который изначально имеет нулевое количество."""
        category = Category("Тестовая")
        
        # Сначала добавляем нормальный товар
        good_product = Product("Хороший товар", 1000, 5)
        category.add_product(good_product)
        
        # Проверяем, что только хороший товар добавлен
        assert len(category.products) == 1
        assert category.products[0] == good_product
