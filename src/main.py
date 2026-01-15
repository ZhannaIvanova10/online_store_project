"""
Основной модуль интернет-магазина с демонстрацией обработки исключений.
"""

import sys
import os
import json
from pathlib import Path
# Добавляем родительскую директорию в путь
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models import (BaseProduct, Product, Smartphone, LawnGrass,
                    Category, LoggingMixin, OrderItem)


def load_categories_from_json(filename):
    """
    Загружает категории из JSON файла.
    
    Args:
        filename (str): Путь к JSON файлу
        
    Returns:
        list: Список объектов Category
    """
    try:
        filepath = Path(filename)
        if not filepath.exists():
            raise FileNotFoundError(f"Файл {filename} не найден")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        categories = []
        for category_data in data:
            category = Category(
                name=category_data['name'],
                description=category_data.get('description', ''),
                products=[]
            )
            
            for product_data in category_data['products']:
                product_type = product_data.get('type', 'product')
                
                if product_type == 'smartphone':
                    product = Smartphone(
                        name=product_data['name'],
                        description=product_data.get('description', ''),
                        price=product_data['price'],
                        quantity=product_data.get('quantity', 0),
                        performance=product_data.get('performance', ''),
                        model=product_data.get('model', ''),
                        memory=product_data.get('memory', 0),
                        color=product_data.get('color', '')
                    )
                elif product_type == 'lawn_grass':
                    product = LawnGrass(
                        name=product_data['name'],
                        description=product_data.get('description', ''),
                        price=product_data['price'],
                        quantity=product_data.get('quantity', 0),
                        country=product_data.get('country', ''),
                        germination_period=product_data.get('germination_period', ''),
                        color=product_data.get('color', '')
                    )
                else:
                    product = Product(
                        name=product_data['name'],
                        description=product_data.get('description', ''),
                        price=product_data['price'],
                        quantity=product_data.get('quantity', 0)
                    )
                
                category.add_product(product)
            categories.append(category)
        
        return categories
    
    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка декодирования JSON: {e}")
    except KeyError as e:
        raise ValueError(f"Отсутствует обязательное поле в JSON: {e}")


def main():
    """Основная функция демонстрации работы интернет-магазина."""
    print("=" * 60)
    print("Демонстрация работы интернет-магазина")
    print("=" * 60)
    
    # Попытка загрузить категории из JSON
    try:
        categories = load_categories_from_json("data/products.json")
        print(f"✅ Загружено категорий из JSON: {len(categories)}")
    except FileNotFoundError as e:
        print(f"❌ Файл не найден: {e}")
        print("Создаем тестовые данные...")
        # Создаем тестовые категории вручную
        category1 = Category("Электроника", "Электронные устройства")
        category2 = Category("Сад и огород", "Товары для сада")
        
        # Создаем тестовые продукты
        phone = Smartphone(
            name="iPhone 15",
            description="Смартфон Apple",
            price=99999,
            quantity=10,
            performance="A16 Bionic",
            model="iPhone 15 Pro",
            memory=256,
            color="Black"
        )
        
        grass = LawnGrass(
            name="Газонная трава Премиум",
            description="Качественная газонная трава",
            price=1500,
            quantity=100,
            country="Россия",
            germination_period="14 дней",
            color="Зеленый"
        )
        product1 = Product("Наушники", "Беспроводные наушники", 5000, 25)
        product2 = Product("Лейка", "Пластиковая лейка для полива", 800, 40)
        
        category1.add_product(phone)
        category1.add_product(product1)
        category2.add_product(grass)
        category2.add_product(product2)
        
        categories = [category1, category2]
        print(f"✅ Создано тестовых категорий: {len(categories)}")
    
    # Демонстрация работы с категориями
    print("\n1. Демонстрация категорий и продуктов:")
    for category in categories:
        print(f"\nКатегория: {category.name}")
        print(f"Описание: {category.description}")
        print(f"Количество продуктов: {len(category.products)}")
        
        for product in category.products[:2]:  # Показываем первые 2 продукта
            print(f"  - {product.name}: {product.price} руб.")
    
    # Демонстрация создания заказа
    print("\n" + "=" * 60)
    print("2. Демонстрация создания заказа:")
    try:
        # Выбираем несколько продуктов
        all_products = []
        for category in categories:
            all_products.extend(category.products)
        
        if len(all_products) >= 2:
            item1 = OrderItem(all_products[0], 2)
            item2 = OrderItem(all_products[1], 1)
            
            print(f"✅ Созданы позиции заказа:")
            print(f"   - {item1.product.name}: {item1.quantity} шт.")
            print(f"   - {item2.product.name}: {item2.quantity} шт.")
    
    except Exception as e:
        print(f"❌ Ошибка при создании заказа: {e}")
    
    # Демонстрация обработки исключений
    print("\n" + "=" * 60)
    print("3. Демонстрация обработки исключений:")
    try:
        # Пытаемся создать продукт с некорректными данными
        print("\nПопытка создать продукт с отрицательной ценой:")
        invalid_product = Product("Некорректный продукт", -100, "Описание", 10)
    except ValueError as e:
        print(f"✅ Поймано исключение: {e}")
    
    try:
        print("\nПопытка создать продукт с нулевым количеством:")
        invalid_product2 = Product("Продукт 2", 100, "Описание", 0)
    except ValueError as e:
        print(f"✅ Поймано исключение: {e}")
    
    # Демонстрация работы миксина логирования
    print("\n" + "=" * 60)
    print("4. Демонстрация логирования:")
    
    logger = LoggingMixin()
    logger.log_info("Тестовое информационное сообщение")
    logger.log_warning("Тестовое предупреждение")
    logger.log_error("Тестовая ошибка")
    
    print("\n" + "=" * 60)
    print("Демонстрация завершена успешно!")
    print("=" * 60)
if __name__ == "__main__":
    main()
