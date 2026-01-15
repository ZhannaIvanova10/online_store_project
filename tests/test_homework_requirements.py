"""Тесты, соответствующие требованиям домашнего задания"""

import pytest
from src.models import Product, Category


class TestRequirement1:
    """Тесты для требования 1: Инициализация экземпляра класса Product"""
    
    def test_product_zero_quantity_raises_valueerror(self):
        """При инициализации с quantity=0 выбрасывается ValueError"""
        with pytest.raises(ValueError) as exc_info:
            Product("Тестовый товар", "Описание", 100.0, 0)
        # Проверяем точное сообщение из задания
        assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"
    
    def test_product_positive_quantity_works(self):
        """Товар с положительным количеством создается нормально"""
        product = Product("Тестовый товар", "Описание", 100.0, 5)
        assert product.quantity == 5


class TestRequirement2:
    """Тесты для требования 2: Метод подсчета среднего ценника"""
    
    def test_calculate_average_price_exists(self):
        """Метод calculate_average_price существует в Category"""
        category = Category("Тест", "Описание")
        assert hasattr(category, 'calculate_average_price')
    def test_calculate_average_price_empty_category(self):
        """Метод возвращает 0 для пустой категории"""
        category = Category("Пустая категория", "Нет товаров")
        assert category.calculate_average_price() == 0
    
    def test_calculate_average_price_with_products(self):
        """Метод правильно считает среднюю цену"""
        products = [
            Product("Товар 1", "Описание 1", 100.0, 5),
            Product("Товар 2", "Описание 2", 200.0, 3),
            Product("Товар 3", "Описание 3", 300.0, 2)
        ]
        category = Category("Категория", "Несколько товаров", products)
        
        # Складываем только цены и делим на количество товаров
        expected = (100.0 + 200.0 + 300.0) / 3
        assert category.calculate_average_price() == expected
    def test_calculate_average_price_single_product(self):
        """Метод работает с одним товаром"""
        product = Product("Товар", "Описание", 150.0, 10)
        category = Category("Категория", "Один товар", [product])
        assert category.calculate_average_price() == 150.0


class TestAdditionalCoverage:
    """Дополнительные тесты для покрытия"""
    
    def test_category_str_representation(self):
        """Тест строкового представления категории"""
        category = Category("Электроника", "Техника")
        assert "Электроника" in str(category)
    
    def test_product_str_representation(self):
        """Тест строкового представления продукта"""
        product = Product("Телефон", "Смартфон", 50000.0, 5)
        assert "Телефон" in str(product)
        assert "50000.0" in str(product)
    
    def test_category_add_product_with_zero_quantity(self):
        """Проверка add_product с товаром quantity=0"""
        category = Category("Категория", "Описание")
        product = Product("Товар", "Описание", 100.0, 0)
        with pytest.raises(ValueError) as exc_info:
            category.add_product(product)
        
        assert "Товар с нулевым количеством не может быть добавлен" in str(exc_info.value)
    
    def test_category_len(self):
        """Тест метода __len__ категории"""
        category = Category("Категория", "Описание")
        assert len(category) == 0
        
        product = Product("Товар", "Описание", 100.0, 5)
        category.add_product(product)
        assert len(category) == 5
