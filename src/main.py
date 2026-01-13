"""
Основной модуль интернет-магазина.
"""

import sys
import os

# Добавляем путь для импорта модулей
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from .models import Product, Category, load_categories_from_json


def create_sample_data():
    """
    Создает пример данных для демонстрации.
    
    Returns:
        Список объектов Category
    """
    # Сбрасываем счетчики для чистоты примера
    Category.category_count = 0
    Category.product_count = 0
    # Создаем товары
    laptop = Product(
        name="Ноутбук", 
        description="Мощный игровой ноутбук", 
        price=150000, 
        quantity=5
    )
    
    phone = Product(
        name="Смартфон", 
        description="Флагманский смартфон", 
        price=80000, 
        quantity=10
    )
    
    tablet = Product(
        name="Планшет", 
        description="Графический планшет", 
        price=50000, 
        quantity=7
    )
    # Создаем категории
    electronics = Category(
        name="Электроника", 
        description="Техника и гаджеты", 
        products=[laptop, phone, tablet]
    )
    
    # Создаем товары для другой категории
    book1 = Product(
        name="Python для начинающих", 
        description="Учебник по Python", 
        price=1500, 
        quantity=20
    )
    
    book2 = Product(
        name="Алгоритмы и структуры данных", 
        description="Продвинутая книга", 
        price=2500, 
        quantity=15
    )
    books = Category(
        name="Книги", 
        description="Учебная литература", 
        products=[book1, book2]
    )
    
    return [electronics, books]


def print_store_info(categories):
    """
    Выводит информацию о магазине.
    
    Args:
        categories: Список объектов Category
    """
    print("=" * 50)
    print("ИНФОРМАЦИЯ О МАГАЗИНЕ")
    print("=" * 50)
    
    print(f"\nВсего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")
    
    for category in categories:
        print(f"\n{'-' * 30}")
        print(f"Категория: {category.name}")
        print(f"Описание: {category.description}")
        print(f"Общее количество товаров: {category.total_quantity}")
        if category.products:
            print("\nТовары в категории:")
            print(category.products)
        else:
            print("\nВ категории нет товаров")


def load_and_print_json_data(file_path="products.json"):
    """
    Загружает данные из JSON файла и выводит информацию.
    
    Args:
        file_path: Путь к JSON файлу
    """
    try:
        print(f"\nЗагрузка данных из файла: {file_path}")
        categories = load_categories_from_json(file_path)
        
        print_store_info(categories)
        
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
        print("Проверьте наличие файла products.json")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
def main():
    """Основная функция программы."""
    print("ДЕМОНСТРАЦИЯ РАБОТЫ ИНТЕРНЕТ-МАГАЗИНА")
    print("=" * 50)
    
    # Демонстрация 1: Создание и вывод примерных данных
    print("\n1. Примерные данные:")
    sample_categories = create_sample_data()
    print_store_info(sample_categories)
    
    # Демонстрация 2: Работа магических методов
    print("\n" + "=" * 50)
    print("2. ДЕМОНСТРАЦИЯ МАГИЧЕСКИХ МЕТОДОВ:")
    print("=" * 50)
    
    # Создаем товары для демонстрации
    product1 = Product("Товар A", "Описание A", 100, 2)  # 200
    product2 = Product("Товар B", "Описание B", 200, 3)  # 600
    
    print(f"\nДемонстрация __str__ для товара:")
    print(f"product1: {product1}")
    print(f"product2: {product2}")
    
    print(f"\nДемонстрация __add__ для товаров:")
    total = product1 + product2
    print(f"product1 + product2 = {total} (200 + 600)")
    
    print(f"\nДемонстрация __str__ для категории:")
    test_category = Category("Тестовая категория", "Для демонстрации", [product1, product2])
    print(test_category)
    print(f"\nДемонстрация итератора категории:")
    print("Товары в категории (через итератор):")
    for i, product in enumerate(test_category, 1):
        print(f"  {i}. {product.name} - {product.price} руб.")
    
    print(f"\nДемонстрация total_quantity:")
    print(f"Общее количество в категории: {test_category.total_quantity}")
    
    # Демонстрация 3: Загрузка из JSON файла
    print("\n" + "=" * 50)
    print("3. ЗАГРУЗКА ИЗ JSON ФАЙЛА:")
    print("=" * 50)
    
    if os.path.exists("products.json"):
        load_and_print_json_data()
    else:
        print("Файл products.json не найден, создаем примерный...")
        
        # Создаем примерный JSON файл
        import json
        
        sample_data = [
            {
                "name": "Электроника",
                "description": "Техника и устройства",
                "products": [
                    {
                        "name": "Смартфон",
                        "description": "Флагманский телефон",
                        "price": 79999.99,
                        "quantity": 8
                    },
                    {
                        "name": "Ноутбук", 
                        "description": "Игровой ноутбук",
                        "price": 129999.99,
                        "quantity": 3
                    }
                ]
            },
            {
                "name": "Книги",
                "description": "Литература",
                "products": [
                    {
                        "name": "Python для начинающих",
                        "description": "Учебник программирования",
                        "price": 1499.99,
                        "quantity": 25
                    }
                ]
            }
        ]
        with open("products.json", "w", encoding="utf-8") as f:
            json.dump(sample_data, f, ensure_ascii=False, indent=2)
        
        print("Файл products.json создан, загружаем данные...")
        load_and_print_json_data()
    
    print("\n" + "=" * 50)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 50)


if __name__ == "__main__":
    main()
