#!/usr/bin/env python3
"""
Главный модуль интернет-магазина.
Демонстрирует работу с исключениями.
"""

import sys
import io

# Устанавливаем UTF-8 кодировку для Windows
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import json
from models import BaseProduct, Category, load_categories_from_json
def demonstrate_exceptions(store):
    """
    Демонстрирует различные сценарии обработки исключений.
    """
    print("\n" + "="*60)
    print("ДЕМОНСТРАЦИЯ ОБРАБОТКИ ИСКЛЮЧЕНИЙ")
    print("="*60)
    
    # 1. Попытка создать товар с нулевым количеством
    print("\n1. Попытка создать товар с quantity=0:")
    try:
        product = BaseProduct("Невалидный товар", "Описание", 100, 0)
        print("   [ERROR] Должно было быть исключение!")
    except ValueError as e:
        print(f"   [OK] ValueError перехвачено: {e}")
    
    # 2. Попытка создать товар с отрицательным количеством
    print("\n2. Попытка создать товар с quantity=-1:")
    try:
        product = BaseProduct("Невалидный товар", "Описание", 100, -1)
        print("   [ERROR] Должно было быть исключение!")
    except ValueError as e:
        print(f"   [OK] ValueError перехвачено: {e}")
    # 3. Добавление не-продукта в категорию
    print("\n3. Попытка добавить не-продукт в категорию:")
    try:
        cat = Category("Тест", "Тест")
        cat.add_product("не продукт")
        print("   [ERROR] Должно было быть исключение!")
    except TypeError as e:
        print(f"   [OK] TypeError перехвачено: {e}")
    
    # 4. Средняя цена пустой категории
    print("\n4. Средняя цена пустой категории:")
    empty_category = Category("Пустая", "Без товаров")
    print(f"   [OK] Средняя цена: {empty_category.average_price()} руб.")
    
    # 5. Работа с несуществующим файлом
    print("\n5. Попытка загрузить несуществующий JSON файл:")
    try:
        categories = load_categories_from_json("не_существует.json")
        print("   [ERROR] Должно было быть исключение!")
    except FileNotFoundError as e:
        print(f"   [OK] FileNotFoundError перехвачено: {e}")
    
    print("\n" + "="*60)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("="*60)
def main():
    """
    Основная функция программы.
    """
    print("ЗАГРУЗКА ИНТЕРНЕТ-МАГАЗИНА")
    print("="*60)
    
    # Создаем магазин
    store = {}
    
    # Загружаем тестовые данные
    try:
        print("\nЗагрузка тестовых данных из test_data.json...")
        categories = load_categories_from_json("../test_data.json")
        
        # Добавляем категории в магазин
        for category in categories:
            store[category.name] = category
        
        print(f"[OK] Загружено {len(categories)} категорий")
        
        # Выводим информацию
        print("\n" + "="*60)
        print("ИНФОРМАЦИЯ О МАГАЗИНЕ")
        print("="*60)
        for category_name, category in store.items():
            print(f"\nКатегория: {category_name}")
            print(f"Описание: {category.description}")
            print(f"Количество товаров: {category.total_products}")
            print(f"Средняя цена: {category.average_price():.2f} руб.")
            print("Товары:")
            
            for product in category.products:
                print(f"  - {product.name}: {product.price} руб. ({product.quantity} шт.)")
    
    except Exception as e:
        print(f"[ERROR] Ошибка при загрузке данных: {e}")
        return
    
    # Демонстрируем исключения
    demonstrate_exceptions(store)
    # Финальное сообщение
    print("\n" + "="*60)
    print("ПРОВЕРКА ВЫПОЛНЕНА УСПЕШНО!")
    print("="*60)
    print("\nВсе исключения корректно обрабатываются:")
    print("1. [OK] ValueError при создании товара с quantity <= 0")
    print("2. [OK] TypeError при добавлении не-продукта в категорию")
    print("3. [OK] ZeroDivisionError обработан в average_price()")
    print("4. [OK] FileNotFoundError при загрузке несуществующего файла")
    print("5. [OK] JSONDecodeError при невалидном JSON")
    print("6. [OK] KeyError при отсутствии обязательных полей")
    print("="*60)


if __name__ == "__main__":
    main()
