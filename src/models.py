"""
Модели данных для интернет-магазина с абстрактным классом и миксином.
"""

import json
from abc import ABC, abstractmethod

class LoggingMixin:
    """Миксин для логирования создания объектов."""

    def __init__(self, *args, **kwargs):
        """Инициализация с логированием."""
        # Сохраняем аргументы для логирования
        self._logging_args = args
        self._logging_kwargs = kwargs

        # Вызываем родительский __init__
        super().__init__(*args, **kwargs)

        # Теперь логируем после установки всех атрибутов
        self._log_creation()

    def _log_creation(self):
        """Логирует создание объекта."""
        class_name = self.__class__.__name__
        params = []

        # Базовые атрибуты Product
        if hasattr(self, 'name'):
            params.append(f"name='{self.name}'")
        if hasattr(self, 'description'):
            params.append(f"description='{self.description}'")
        if hasattr(self, 'price'):
            params.append(f"price={self.price}")
        if hasattr(self, 'quantity'):
            params.append(f"quantity={self.quantity}")
        # Специфичные атрибуты для наследников
        if class_name == 'Smartphone':
            if hasattr(self, 'efficiency'):
                params.append(f"efficiency='{self.efficiency}'")
            if hasattr(self, 'model'):
                params.append(f"model='{self.model}'")
            if hasattr(self, 'memory'):
                params.append(f"memory={self.memory}")
            if hasattr(self, 'color'):
                params.append(f"color='{self.color}'")

        elif class_name == 'LawnGrass':
            if hasattr(self, 'country'):
                params.append(f"country='{self.country}'")
            if hasattr(self, 'germination_period'):
                params.append(f"germination_period={self.germination_period}")
            if hasattr(self, 'color'):
                params.append(f"color='{self.color}'")
        params_str = ', '.join(params)
        print(f"Создан объект: {class_name}({params_str})")

class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @abstractmethod
    def __init__(self, name, description, price, quantity):
        """Абстрактный метод инициализации продукта."""
        # ЗАДАНИЕ 1: Проверка на нулевое количество
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        """Абстрактный метод строкового представления."""
        pass

    @abstractmethod
    def __add__(self, other):
        """Абстрактный метод сложения продуктов."""
        pass
    def get_total_cost(self):
        """Метод для получения общей стоимости продукта."""
        return self.price * self.quantity

    def increase_quantity(self, amount):
        """Увеличивает количество товара."""
        if amount > 0:
            self.quantity += amount
            return True
        return False

    def decrease_quantity(self, amount):
        """Уменьшает количество товара."""
        if 0 < amount <= self.quantity:
            self.quantity -= amount
            return True
        return False


class Product(LoggingMixin, BaseProduct):
    """Базовый класс товара."""
    def __init__(self, name, description, price, quantity):
        """Инициализация товара."""
        # Вызываем родительский конструктор
        super().__init__(name, description, price, quantity)

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

    def __repr__(self):
        """Представление объекта для отладки."""
        return f"Product(name='{self.name}', description='{self.description}', price={self.price}, quantity={self.quantity})"
class Smartphone(Product):
    """Класс смартфона."""

    def __init__(self, name, description, price, quantity,
                 efficiency, model, memory, color):
        """
        Инициализация смартфона.

        Args:
            name: Название
            description: Описание
            price: Цена
            quantity: Количество
            efficiency: Производительность
            model: Модель
            memory: Объем встроенной памяти
            color: Цвет
        """
        # Сначала сохраняем специфичные атрибуты
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        # Затем вызываем родительский __init__
        super().__init__(name, description, price, quantity)
    def __str__(self):
        """Строковое представление смартфона."""
        return f"{self.name} ({self.model}) - {self.price} руб. [Остаток: {self.quantity} шт.]"


class LawnGrass(Product):
    """Класс газонной травы."""

    def __init__(self, name, description, price, quantity,
                 country, germination_period, color):
        """
        Инициализация газонной травы.

        Args:
            name: Название
            description: Описание
            price: Цена
            quantity: Количество
            country: Страна-производитель
            germination_period: Срок прорастания
            color: Цвет
        """
        # Сначала сохраняем специфичные атрибуты
        self.country = country
        self.germination_period = germination_period
        self.color = color
        # Затем вызываем родительский __init__
        super().__init__(name, description, price, quantity)

    def __str__(self):
        """Строковое представление газонной травы."""
        return f"{self.name} - {self.price} руб. [Остаток: {self.quantity} шт.]"


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
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        
        self.products.append(product)
        Category.product_count += 1
    
    def get_average_price(self):
        """
        ЗАДАНИЕ 2: Возвращает среднюю цену товаров в категории.
        
        Returns:
            float: Средняя цена товаров или 0, если в категории нет товаров.
        """
        try:
            if not self.products:
                return 0
            total_price = sum(product.price for product in self.products)
            return total_price / len(self.products)
        except ZeroDivisionError:
            return 0
        except Exception:
            return 0
    def __str__(self):
        """Строковое представление категории."""
        return f"{self.name}, количество продуктов: {len(self.products)} шт."
