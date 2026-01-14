"""
Модели данных для интернет-магазина.
"""

import json


class Product:
    """Класс товара."""

    def __init__(self, name, description, price, quantity):
        """
        Инициализация товара.

        Args:
            name: Название товара
            description: Описание товара
            price: Цена товара
            quantity: Количество товара
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        """Строковое представление товара."""
        return f"{self.name} - {self.price} руб. [Остаток: {self.quantity} шт.]"
    
    def __add__(self, other):
        """
        Сложение товаров.

        Возвращает общую стоимость товаров.
        Только товары одного типа можно складывать.
        """
        if type(self) != type(other):
            raise TypeError(f"Нельзя складывать товары разных типов: {type(self).__name__} и {type(other).__name__}")
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    """Класс Смартфон, наследник Product."""
    
    def __init__(self, name, description, price, quantity, 
                 efficiency, model, memory, color):
        """
        Инициализация смартфона.

        Args:
            name: Название товара
            description: Описание товара
            price: Цена товара
            quantity: Количество товара
            efficiency: Производительность
            model: Модель
            memory: Объем встроенной памяти (ГБ)
            color: Цвет
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
    
    def __str__(self):
        """Строковое представление смартфона."""
        return (f"{self.name} ({self.model}) - {self.price} руб. "
                f"[Остаток: {self.quantity} шт., Память: {self.memory}ГБ]")


class LawnGrass(Product):
    """Класс Трава газонная, наследник Product."""
    
    def __init__(self, name, description, price, quantity,
                 country, germination_period, color):
        """
        Инициализация травы газонной.

        Args:
            name: Название товара
            description: Описание товара
            price: Цена товара
            quantity: Количество товара
            country: Страна-производитель
            germination_period: Срок прорастания (дней)
            color: Цвет
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
    
    def __str__(self):
        """Строковое представление травы газонной."""
        return (f"{self.name} - {self.price} руб. "
                f"[Остаток: {self.quantity} шт., Страна: {self.country}]")


class Category:
    """Класс категории товаров."""

    # Статические атрибуты для подсчета
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """
        Инициализация категории.

        Args:
            name: Название категории
            description: Описание категории
            products: Список товаров в категории
        """
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.products)
    
    def add_product(self, product):
        """
        Добавляет товар в категорию.

        Args:
            product: Объект товара для добавления
        
        Raises:
            TypeError: Если передан не объект Product или его наследник
        """
        # Используем isinstance для проверки, что объект является Product или его наследником
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        
        self.products.append(product)
        Category.product_count += 1
    
    def __str__(self):
        """Строковое представление категории."""
        return f"{self.name}: {len(self.products)} товаров"
