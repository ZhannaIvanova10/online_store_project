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
        # BaseProduct.__init__ будет вызван через super() в LoggingMixin
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
        base_str = super().__str__()
        return f"{base_str} | Модель: {self.model}, Память: {self.memory} ГБ, Цвет: {self.color}"
    
    def __repr__(self):
        """Представление объекта для отладки."""
        return (f"Smartphone(name='{self.name}', description='{self.description}', "
                f"price={self.price}, quantity={self.quantity}, efficiency='{self.efficiency}', "
                f"model='{self.model}', memory={self.memory}, color='{self.color}')")


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
            germination_period: Срок прорастания (в днях)
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
        base_str = super().__str__()
        return f"{base_str} | Страна: {self.country}, Прорастание: {self.germination_period} дней, Цвет: {self.color}"
    
    def __repr__(self):
        """Представление объекта для отладки."""
        return (f"LawnGrass(name='{self.name}', description='{self.description}', "
                f"price={self.price}, quantity={self.quantity}, country='{self.country}', "
                f"germination_period={self.germination_period}, color='{self.color}')")


class Category:
    """Класс категории товаров."""
    
    # Статические атрибуты для подсчета
    category_count = 0
    product_count = 0
    def __init__(self, name, description, products=None):
        """
        Инициализация категории.
        
        Args:
            name: Название категории
            description: Описание категории
            products: Список товаров в категории (по умолчанию пустой)
        """
        self.name = name
        self.description = description
        self._products = products if products is not None else []
        
        # Обновляем счетчики
        Category.category_count += 1
        Category.product_count += len(self._products)
    
    def add_product(self, product):
        """
        Добавляет продукт в категорию.
        
        Args:
            product: Объект Product или его наследник
        Raises:
            TypeError: Если передан не Product или его наследник
        """
        if not isinstance(product, Product):
            raise TypeError(f"Можно добавлять только продукты (Product или его наследники), получено: {type(product).__name__}")
        
        self._products.append(product)
        Category.product_count += 1
    
    @property
    def products(self):
        """Геттер для получения строкового представления товаров."""
        if not self._products:
            return ""
        
        products_str = "\n".join(str(product) for product in self._products)
        return products_str
    @property
    def total_quantity(self):
        """Общее количество товаров в категории."""
        return sum(product.quantity for product in self._products)
    
    def __str__(self):
        """Строковое представление категории."""
        products_info = self.products
        if products_info:
            return f"{self.name} ({self.description})\n{products_info}"
        else:
            return f"{self.name} ({self.description}) - нет товаров"
    
    def __iter__(self):
        """Итератор по товарам категории."""
        return iter(self._products)
def load_categories_from_json(file_path):
    """
    Загружает категории из JSON файла.
    
    Args:
        file_path: Путь к JSON файлу
        
    Returns:
        Список объектов Category
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_path} не найден")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Ошибка декодирования JSON: {e}", e.doc, e.pos)
    categories = []
    for category_data in data:
        products = []
        for product_data in category_data.get('products', []):
            # Определяем тип продукта на основе наличия полей
            if 'model' in product_data and 'memory' in product_data:
                product = Smartphone(
                    name=product_data['name'],
                    description=product_data['description'],
                    price=product_data['price'],
                    quantity=product_data['quantity'],
                    efficiency=product_data.get('efficiency', 'не указана'),
                    model=product_data['model'],
                    memory=product_data['memory'],
                    color=product_data.get('color', 'не указан')
                )
            elif 'country' in product_data and 'germination_period' in product_data:
                product = LawnGrass(
                    name=product_data['name'],
                    description=product_data['description'],
                    price=product_data['price'],
                    quantity=product_data['quantity'],
                    country=product_data['country'],
                    germination_period=product_data['germination_period'],
                    color=product_data.get('color', 'не указан')
                )
            else:
                product = Product(
                    name=product_data['name'],
                    description=product_data['description'],
                    price=product_data['price'],
                    quantity=product_data['quantity']
                )
            products.append(product)
        
        category = Category(
            name=category_data['name'],
            description=category_data['description'],
            products=products
        )
        categories.append(category)
    
    return categories
# Дополнительное задание: класс Заказ
class OrderItem:
    """Класс элемента заказа."""
    
    def __init__(self, product, quantity):
        """
        Инициализация элемента заказа.
        
        Args:
            product: Товар
            quantity: Количество
        """
        self.product = product
        self.quantity = quantity
        self.total_cost = product.price * quantity
    
    def __str__(self):
        """Строковое представление элемента заказа."""
        return f"{self.product.name} x {self.quantity} = {self.total_cost} руб."
    def __repr__(self):
        """Представление для отладки."""
        return f"OrderItem(product={repr(self.product)}, quantity={self.quantity})"
