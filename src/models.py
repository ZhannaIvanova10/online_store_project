"""
Модели данных для интернет-магазина.
"""

import json
from pathlib import Path


class BaseProduct:
    """Базовый класс для всех товаров."""
    
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация базового продукта.
        Args:
            name: Название товара
            description: Описание товара
            price: Цена товара
            quantity: Количество товара
            
        Raises:
            ValueError: Если количество <= 0
        """
        if quantity <= 0:
            raise ValueError(f"Количество товара должно быть больше 0. Получено: {quantity}")
        
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        return f"{self.name} - {self.price} руб. (Осталось: {self.quantity})"

class Product(BaseProduct):
    """Класс для обычных товаров."""
    
    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(name, description, price, quantity)


class Smartphone(Product):
    """Класс для смартфонов."""
    
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 performance: str, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color
    def __str__(self):
        return f"{self.name} {self.model} - {self.price} руб., {self.memory}ГБ, {self.color}"


class LawnGrass(Product):
    """Класс для газонной травы."""
    
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class LoggingMixin:
    """Миксин для логирования."""
    def log(self, message: str):
        print(f"[LOG] {message}")


class Category(LoggingMixin):
    """Класс для категорий товаров."""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.products = []
    
    def add_product(self, product):
        """Добавляет продукт в категорию."""
        if not isinstance(product, (Product, Smartphone, LawnGrass)):
            raise TypeError(f"Ожидается объект Product, получен {type(product)}")
        
        self.products.append(product)
        self.log(f"Добавлен продукт '{product.name}' в категорию '{self.name}'")
    def calculate_average_price(self) -> float:
        """Вычисляет среднюю цену товаров в категории."""
        if not self.products:
            return 0.0
        
        total_price = sum(product.price for product in self.products)
        return total_price / len(self.products)
    
    def __len__(self):
        """Возвращает общее количество товаров в категории."""
        return len(self.products)
    
    def __str__(self):
        return f"Категория: {self.name} ({len(self.products)} товаров)"


def load_categories_from_json(file_path: str):
    """
    Загружает категории из JSON файла.
    Args:
        file_path: Путь к JSON файлу с данными категорий

    Returns:
        Список объектов Category
    """
    categories = []

    try:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Файл {file_path} не найден")
        
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for category_data in data.get('categories', []):
            category = Category(
                name=category_data['name'],
                description=category_data.get('description', '')
            )
            # Добавляем продукты в категорию
            for product_data in category_data.get('products', []):
                product = Product(
                    name=product_data['name'],
                    description=product_data['description'],
                    price=product_data['price'],
                    quantity=product_data['quantity']
                )
                category.add_product(product)

            categories.append(category)
    
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON: {e}")
        return []
    except KeyError as e:
        print(f"Отсутствует обязательное поле в данных: {e}")
        return []
    except Exception as e:
        print(f"Произошла ошибка при загрузке файла: {e}")
        return []
    return categories
