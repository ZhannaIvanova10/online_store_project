#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Демонстрационный файл для ДЗ 3: Обработка исключений.
Этот файл должен запускаться без ошибок.
"""

import sys
import io

# Устанавливаем правильную кодировку для Windows
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from src.models import Product, Category, ZeroQuantityError


def main():
    """Основная функция для демонстрации работы с исключениями."""
    
    # Часть 1: Демонстрация первого критерия
    print("1. Демонстрация критерия 1:")
    print("   Создание товара с положительным количеством:")
    try:
        laptop = Product("Ноутбук", 150000, 3)
        print(f"   Успешно создан: {laptop}")
    except ZeroQuantityError as e:
        print(f"   Ошибка: {e}")
    
    print("\n   Попытка создать товар с нулевым количеством:")
    try:
        invalid_product = Product("Битая мышка", 500, 0)
        print(f"   Успешно создан: {invalid_product}")
    except ValueError as e:
        print(f"   Ожидаемая ошибка ValueError: {e}")
    # Часть 2: Демонстрация второго критерия
    print("\n2. Демонстрация критерия 2:")
    
    # Создаем категорию с товарами
    electronics = Category("Электроника")
    
    # Добавляем товары
    electronics.products = [
        Product("Ноутбук", 100000, 5),
        Product("Смартфон", 80000, 3),
        Product("Планшет", 60000, 2)
    ]
    
    print(f"   Категория: {electronics.name}")
    print(f"   Количество товаров: {len(electronics.products)}")
    print(f"   Средняя цена: {electronics.calculate_average_price():.2f} руб.")
    
    # Создаем пустую категорию
    empty_category = Category("Пустая категория")
    
    print(f"\n   Категория: {empty_category.name}")
    print(f"   Количество товаров: {len(empty_category.products)}")
    print(f"   Средняя цена: {empty_category.calculate_average_price():.2f} руб.")
    # Часть 3: Демонстрация дополнительного задания
    print("\n3. Дополнительное задание:")
    
    test_category = Category("Тестовая категория")
    
    print("   Успешное добавление товара:")
    try:
        good_product = Product("Тестовый товар", 1000, 5)
        test_category.add_product(good_product)
    except ZeroQuantityError as e:
        print(f"   Поймано исключение: {e}")
    else:
        print("   Товар успешно добавлен!")
    finally:
        print("   Обработка завершена")
    
    print("\n   Попытка добавления товара с нулевым количеством:")
    try:
        bad_product = Product("Битый товар", 500, 0)
        test_category.add_product(bad_product)
    except ZeroQuantityError as e:
        print(f"   Поймано исключение: {e}")
    else:
        print("   Товар успешно добавлен!")
    finally:
        print("   Обработка завершена")
    
    print("\nДемонстрация завершена успешно!")


if __name__ == "__main__":
    main()
