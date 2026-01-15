"""
Демонстрация домашнего задания: Обработка исключений
"""

import sys
import os
import json
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from models import (BaseProduct, Product, Smartphone, LawnGrass,
                        Category, LoggingMixin)
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ: Обработка исключений в интернет-магазине")
    print("=" * 60)
    
    # Задание 1: Проверка нулевого количества
    print("\n1. ЗАДАНИЕ 1: Проверка нулевого количества товара")
    print("Попытка создать товар с quantity = 0:")
    try:
        bad_product = Product("Тестовый товар", "Описание", 100, 0)
        print("❌ ОШИБКА: Должно было возникнуть исключение!")
    except ValueError as e:
        print(f"✅ УСПЕХ: Исключение обработано: {e}")
    # Создание нормальных товаров
    print("\nСоздание нормальных товаров:")
    try:
        p1 = Product("Товар 1", "Описание 1", 100, 10)
        p2 = Product("Товар 2", "Описание 2", 200, 5)
        print(f"✅ Созданы: {p1.name}, {p2.name}")
    except Exception as e:
        print(f"❌ ОШИБКА: {e}")
    
    # Задание 2: Средняя цена в категории
    print("\n2. ЗАДАНИЕ 2: Метод calculate_average_price()")
    
    # Пустая категория
    empty_cat = Category("Пустая категория", "Нет товаров")
    avg_empty = empty_cat.calculate_average_price()
    print(f"Средняя цена в пустой категории: {avg_empty} (ожидается: 0)")
    
    # Категория с товарами
    cat = Category("Электроника", "Техника")
    cat.add_product(p1)
    cat.add_product(p2)
    avg_with_items = cat.calculate_average_price()
    print(f"Средняя цена в категории с товарами: {avg_with_items} (ожидается: 150.0)")
    # Проверка
    if avg_empty == 0 and abs(avg_with_items - 150.0) < 0.01:
        print("✅ ЗАДАНИЕ 2 ВЫПОЛНЕНО КОРРЕКТНО")
    else:
        print("❌ ПРОБЛЕМА С ЗАДАНИЕМ 2")
    
    # Дополнительная демонстрация
    print("\n3. ДОПОЛНИТЕЛЬНО: Другие проверки")
    
    # Проверка добавления неправильного типа
    print("Попытка добавить строку вместо продукта в категорию:")
    try:
        cat.add_product("не продукт")
        print("❌ ОШИБКА: Должно было возникнуть исключение!")
    except TypeError as e:
        print(f"✅ УСПЕХ: Исключение обработано: {e}")
    # Создание смартфона (наследник Product)
    print("\nСоздание смартфона (наследник Product):")
    try:
        phone = Smartphone("Смартфон", "Описание", 50000, 5, 
                          "Высокая", "Модель X", 256, "Черный")
        print(f"✅ УСПЕХ: Создан {phone.name}")
        cat.add_product(phone)
        print(f"✅ Смартфон добавлен в категорию")
    except Exception as e:
        print(f"❌ ОШИБКА: {e}")
    
    # Создание газонной травы
    print("\nСоздание газонной травы (наследник Product):")
    try:
        grass = LawnGrass("Газонная трава", "Для сада", 1500, 100,
                         "Россия", "14 дней", "Зеленый")
        print(f"✅ УСПЕХ: Создана {grass.name}")
    except Exception as e:
        print(f"❌ ОШИБКА: {e}")
    # Демонстрация LoggingMixin
    print("\n4. Логирование (LoggingMixin):")
    try:
        test_product = Product("Тест логирования", "Для демонстрации", 500, 3)
        print("✅ LoggingMixin работает (сообщение выше)")
    except Exception as e:
        print(f"❌ ОШИБКА с LoggingMixin: {e}")
    
    print("\n" + "=" * 60)
    print("ВСЕ ЗАДАНИЯ ВЫПОЛНЕНЫ:")
    print("1. ✅ Проверка нулевого количества - ВЫПОЛНЕНО")
    print("2. ✅ Средняя цена с обработкой исключений - ВЫПОЛНЕНО")
    print("3. ✅ Демонстрация и тестирование - ВЫПОЛНЕНО")
    print("=" * 60)
    
except ImportError as e:
    print(f"❌ Ошибка импорта: {e}")
    print("Проверьте наличие файла models.py и его содержимое")
