"""
Основной модуль интернет-магазина с демонстрацией абстрактных классов и миксинов.
"""

import sys
import os

# Добавляем путь для импорта модулей
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from .models import (BaseProduct, Product, Smartphone, LawnGrass, 
                     Category, LoggingMixin, load_categories_from_json, OrderItem)


def demonstrate_abstract_classes_and_mixins():
    """Демонстрация работы абстрактных классов и миксинов."""
    print("\n" + "=" * 70)
    print("ДЕМОНСТРАЦИЯ АБСТРАКТНЫХ КЛАССОВ И МИКСИНОВ")
    print("=" * 70)
    print("\n1. Создание объектов с логированием (миксин LoggingMixin):")
    print("-" * 50)
    
    print("\nСоздание базового товара:")
    product = Product("Книга", "Художественная литература", 500, 10)
    
    print("\nСоздание смартфона:")
    smartphone = Smartphone(
        name="iPhone 15 Pro",
        description="Флагманский смартфон Apple",
        price=129999,
        quantity=5,
        efficiency="A17 Pro",
        model="iPhone 15 Pro",
        memory=256,
        color="Титановый синий"
    )
    print("\nСоздание газонной травы:")
    lawn_grass = LawnGrass(
        name="Газонная трава Premium",
        description="Высококачественная газонная трава",
        price=2500,
        quantity=15,
        country="Германия",
        germination_period=14,
        color="Изумрудно-зеленый"
    )
    
    print("\n2. Проверка наследования от абстрактного класса BaseProduct:")
    print("-" * 50)
    
    print(f"product является Product: {isinstance(product, Product)}")
    print(f"product является BaseProduct: {isinstance(product, BaseProduct)}")
    print(f"smartphone является Smartphone: {isinstance(smartphone, Smartphone)}")
    print(f"smartphone является Product: {isinstance(smartphone, Product)}")
    print(f"smartphone является BaseProduct: {isinstance(smartphone, BaseProduct)}")
    print(f"lawn_grass является LawnGrass: {isinstance(lawn_grass, LawnGrass)}")
    print(f"lawn_grass является BaseProduct: {isinstance(lawn_grass, BaseProduct)}")
    print("\n3. Демонстрация методов абстрактного класса:")
    print("-" * 50)
    
    print(f"\nМетод get_total_cost() для товаров:")
    print(f"  {product.name}: {product.get_total_cost()} руб.")
    print(f"  {smartphone.name}: {smartphone.get_total_cost()} руб.")
    print(f"  {lawn_grass.name}: {lawn_grass.get_total_cost()} руб.")
    
    print(f"\nИзменение количества товаров:")
    print(f"  Увеличение количества {product.name} на 5: {product.increase_quantity(5)}")
    print(f"  Новое количество: {product.quantity}")
    print(f"  Уменьшение количества {product.name} на 3: {product.decrease_quantity(3)}")
    print(f"  Новое количество: {product.quantity}")
    
    print("\n4. Проверка __repr__ методов:")
    print("-" * 50)
    print(f"repr(product): {repr(product)}")
    print(f"repr(smartphone): {repr(smartphone)}")
    print(f"repr(lawn_grass): {repr(lawn_grass)}")
    
    print("\n5. Дополнительное задание: класс OrderItem:")
    print("-" * 50)
    
    order_item1 = OrderItem(smartphone, 2)
    order_item2 = OrderItem(lawn_grass, 5)
    
    print(f"Элемент заказа 1: {order_item1}")
    print(f"Элемент заказа 2: {order_item2}")
    
    print(f"\nОбщая стоимость заказа: {order_item1.total_cost + order_item2.total_cost} руб.")


def create_sample_data():
    """
    Создает пример данных для демонстрации.
    
    Returns:
        Список объектов Category
    """
    # Сбрасываем счетчики для чистоты примера
    Category.category_count = 0
    Category.product_count = 0
    
    # Создаем товары разных типов
    book = Product(
        name="Python для начинающих", 
        description="Учебник по Python", 
        price=1500, 
        quantity=20
    )
    
    smartphone = Smartphone(
        name="Samsung Galaxy S24",
        description="Флагманский смартфон Samsung",
        price=89999,
        quantity=8,
        efficiency="Snapdragon 8 Gen 3",
        model="Galaxy S24 Ultra",
        memory=256,
        color="Титановый серый"
    )
    lawn_grass = LawnGrass(
        name="Газонная трава Premium",
        description="Высококачественная газонная трава для дачи",
        price=2500,
        quantity=15,
        country="Германия",
        germination_period=10,
        color="Изумрудно-зеленый"
    )
    
    # Создаем категории
    books_category = Category(
        name="Книги", 
        description="Учебная литература", 
        products=[book]
    )
    electronics_category = Category(
        name="Электроника", 
        description="Техника и гаджеты", 
        products=[smartphone]
    )
    
    garden_category = Category(
        name="Сад и огород", 
        description="Товары для сада", 
        products=[lawn_grass]
    )
    
    return [books_category, electronics_category, garden_category]


def print_store_info(categories):
    """
    Выводит информацию о магазине.
    
    Args:
        categories: Список объектов Category
    """
    print("\n" + "=" * 50)
    print("ИНФОРМАЦИЯ О МАГАЗИНЕ")
    print("=" * 50)
    print(f"\nВсего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")
    
    for category in categories:
        print(f"\n{'-' * 40}")
        print(f"Категория: {category.name}")
        print(f"Описание: {category.description}")
        print(f"Общее количество товаров: {category.total_quantity}")
        
        if category.products:
            print("\nТовары в категории:")
            print(category.products)
        else:
            print("\nВ категории нет товаров")


def main():
    """Основная функция программы."""
    print("ДЕМОНСТРАЦИЯ РАБОТЫ ИНТЕРНЕТ-МАГАЗИНА С АБСТРАКТНЫМИ КЛАССАМИ И МИКСИНАМИ")
    print("=" * 70)
    # Демонстрация 1: Абстрактные классы и миксины
    demonstrate_abstract_classes_and_mixins()
    
    # Демонстрация 2: Создание и вывод примерных данных
    print("\n" + "=" * 70)
    print("2. ПРИМЕРНЫЕ ДАННЫЕ С РАЗНЫМИ ТИПАМИ ТОВАРОВ:")
    print("=" * 70)
    
    sample_categories = create_sample_data()
    print_store_info(sample_categories)
    
    # Демонстрация 3: Загрузка из JSON
    print("\n" + "=" * 70)
    print("3. ЗАГРУЗКА ИЗ JSON ФАЙЛА:")
    print("=" * 70)
    
    # Создаем тестовый JSON файл
    import json
    test_json_data = [
        {
            "name": "Электроника",
            "description": "Техника и устройства",
            "products": [
                {
                    "name": "Смартфон",
                    "description": "Телефон",
                    "price": 50000,
                    "quantity": 5,
                    "model": "Model X",
                    "memory": 128,
                    "efficiency": "Высокая",
                    "color": "Черный"
                }
            ]
        }
    ]
    
    with open("test_demo.json", "w", encoding="utf-8") as f:
        json.dump(test_json_data, f, ensure_ascii=False, indent=2)
    
    print("   Создан тестовый файл test_demo.json")
    
    try:
        categories = load_categories_from_json("test_demo.json")
        print("   Файл успешно загружен")
        
        print("\n   Результаты загрузки:")
        for category in categories:
            print(f"\n   Категория: {category.name}")
            for product in category:
                print(f"     - {product.name} ({type(product).__name__})")
                
    except Exception as e:
        print(f"   Ошибка при загрузке: {e}")
    
    # Удаляем тестовый файл
    if os.path.exists("test_demo.json"):
        os.unlink("test_demo.json")
        print("\n   Тестовый файл удален")
    
    print("\n" + "=" * 70)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 70)


if __name__ == "__main__":
    main()
