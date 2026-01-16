"""
Модели данных для интернет-магазина.
"""
import json
import os
class BaseProduct:
    """Базовый класс товара."""
    
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация товара.
        
        Args:
            name: Название товара
            description: Описание товара
            price: Цена товара
            quantity: Количество товара
            
        Raises:
            ValueError: Если количество <= 0
        """
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
    def __str__(self):
        return f"{self.name}: {self.price} руб. ({self.quantity} шт.)"


class Category:
    """Класс категории товаров."""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__products = []
        
    def add_product(self, product: BaseProduct):
        """Добавить товар в категорию."""
        self.__products.append(product)
        print(f"[LOG] Добавлен продукт '{product.name}' в категорию '{self.name}'")
        
    def __str__(self):
        products_list = "\n".join([f"  - {product}" for product in self.__products])
        return f"Категория: {self.name}\nОписание: {self.description}\nТовары:\n{products_list}"
    
    @property
    def products(self):
        """Возвращает список товаров."""
        return [str(product) for product in self.__products]
    
    @property
    def total_products(self):
        """Возвращает количество товаров в категории."""
        return len(self.__products)
    def average_price(self):
        """
        Возвращает среднюю цену товаров в категории.
        
        Returns:
            Средняя цена или 0, если товаров нет.
        """
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0


class Product(BaseProduct):
    """Класс товара. Наследует проверку количества из BaseProduct."""
    # Здесь нет необходимости переопределять __init__
    # Все проверки уже есть в родительском классе
    pass
# Экспортируем классы
__all__ = ['BaseProduct', 'Category', 'Product']
