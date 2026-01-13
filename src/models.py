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
        """
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")
        return self.price * self.quantity + other.price * other.quantity


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
        self._products = products  # приватный атрибут
        # Обновляем счетчики
        Category.category_count += 1
        Category.product_count += len(products)
    
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
