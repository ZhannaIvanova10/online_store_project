"""
Модуль с классами Product и Category для интернет-магазина.
"""


class Product:
    """Класс для представления товара."""
    
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализирует товар.
        
        Args:
            name: Название товара
            description: Описание товара
            price: Цена товара
            quantity: Количество товара на складе
        """
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут
        self.quantity = quantity
    @property
    def price(self) -> float:
        """Геттер для цены товара."""
        return self.__price
    
    @price.setter
    def price(self, new_price: float):
        """
        Сеттер для цены товара с проверкой.
        
        Args:
            new_price: Новая цена товара
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price
    
    @classmethod
    def new_product(cls, product_data: dict, products_list: list = None):
        """
        Класс-метод для создания нового товара.
        
        Args:
            product_data: Словарь с данными товара
            products_list: Список существующих товаров для проверки дубликатов
            
        Returns:
            Product: Новый объект товара
        """
        name = product_data.get('name')
        description = product_data.get('description')
        price = product_data.get('price')
        quantity = product_data.get('quantity')

        # Проверка на дубликаты
        if products_list:
            for existing_product in products_list:
                if existing_product.name.lower() == name.lower():
                    # Объединяем количество
                    existing_product.quantity += quantity
                    # Выбираем максимальную цену
                    if price > existing_product.price:
                        existing_product.price = price
                    return existing_product
        
        # Создаем новый товар
        return cls(name, description, price, quantity)
    
    def __str__(self):
        """Строковое представление товара."""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."


class Category:
    """Класс для представления категории товаров."""
    
    category_count = 0  # Счетчик категорий
    product_count = 0   # Счетчик товаров
    
    def __init__(self, name: str, description: str, products: list = None):
        """
        Инициализирует категорию.
        Args:
            name: Название категории
            description: Описание категории
            products: Список товаров в категории
        """
        self.name = name
        self.description = description
        self.__products = products if products else []  # Приватный атрибут
        
        Category.category_count += 1
        if products:
            Category.product_count += len(products)
    
    def add_product(self, product):
        """
        Добавляет товар в категорию.
        
        Args:
            product: Объект товара для добавления
        """
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
    @property
    def products(self) -> str:
        """Геттер для списка товаров в виде строки."""
        if not self.__products:
            return ""
        
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str
    
    @classmethod
    def load_categories_from_json(cls, json_file: str):
        """
        Загружает категории из JSON файла.
        
        Args:
            json_file: Путь к JSON файлу
            
        Returns:
            list: Список объектов Category
        """
        import json
        
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
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
            
            category = cls(
                name=category_data['name'],
                description=category_data['description'],
                products=products
            )
            categories.append(category)
        
        return categories
    def __str__(self):
        """Строковое представление категории."""
        return f"{self.name}, количество продуктов: {len(self.__products)}"


def load_categories_from_json(json_file: str):
    """
    Функция для загрузки категорий из JSON файла.
    
    Args:
        json_file: Путь к JSON файлу
        
    Returns:
        list: Список объектов Category
    """
    return Category.load_categories_from_json(json_file)
