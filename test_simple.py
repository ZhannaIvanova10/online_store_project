#!/usr/bin/env python3
"""
Простейшие тесты проекта интернет-магазина.
"""

import sys
import io

# Устанавливаем UTF-8 кодировку для Windows
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from src.models import BaseProduct, Category


def test_product_creation():
    """Тест создания продукта."""
    print("\n" + "="*60)
    print("ТЕСТ СОЗДАНИЯ ПРОДУКТА")
    print("="*60)
    # Нормальное создание
    try:
        p = BaseProduct("Тест", "Описание", 100, 10)
        print("[OK] Нормальное создание продукта")
    except Exception as e:
        print(f"[FAIL] Ошибка при нормальном создании: {e}")
        return False
    
    # Создание с quantity=0
    try:
        p = BaseProduct("Тест", "Описание", 100, 0)
        print("[FAIL] Должно было быть исключение для quantity=0")
        return False
    except ValueError as e:
        if "Товар с нулевым количеством не может быть добавлен" in str(e):
            print("[OK] Исключение при quantity=0")
        else:
            print(f"[FAIL] Неправильное сообщение: {e}")
            return False
    
    # Создание с quantity=-1
    try:
        p = BaseProduct("Тест", "Описание", 100, -1)
        print("[FAIL] Должно было быть исключение для quantity=-1")
        return False
    except ValueError as e:
        print("[OK] Исключение при quantity=-1")
    return True


def test_category_operations():
    """Тест операций с категорией."""
    print("\n" + "="*60)
    print("ТЕСТ ОПЕРАЦИЙ С КАТЕГОРИЕЙ")
    print("="*60)
    
    # Создание категории
    try:
        cat = Category("Категория", "Описание")
        print("[OK] Создание категории")
    except Exception as e:
        print(f"[FAIL] Ошибка при создании категории: {e}")
        return False
    
    # Добавление продукта
    try:
        p = BaseProduct("Тест", "Описание", 100, 10)
        cat.add_product(p)
        print("[OK] Добавление продукта в категорию")
    except Exception as e:
        print(f"[FAIL] Ошибка при добавлении продукта: {e}")
        return False
    # Средняя цена
    try:
        avg = cat.average_price()
        if avg == 100:
            print("[OK] Расчет средней цены")
        else:
            print(f"[FAIL] Неправильная средняя цена: {avg}")
            return False
    except Exception as e:
        print(f"[FAIL] Ошибка при расчете средней цены: {e}")
        return False
    
    # Средняя цена пустой категории
    try:
        empty_cat = Category("Пустая", "Без товаров")
        avg = empty_cat.average_price()
        if avg == 0:
            print("[OK] Средняя цена пустой категории")
        else:
            print(f"[FAIL] Неправильная средняя цена пустой категории: {avg}")
            return False
    except Exception as e:
        print(f"[FAIL] Ошибка при расчете средней цены пустой категории: {e}")
        return False
    # Добавление не-продукта
    try:
        cat.add_product("не продукт")
        print("[FAIL] Должно было быть исключение при добавлении не-продукта")
        return False
    except TypeError:
        print("[OK] Исключение при добавлении не-продукта")
    
    return True


def main():
    """Основная функция тестирования."""
    print("="*60)
    print("ПРОСТЕЙШИЕ ТЕСТЫ ПРОЕКТА")
    print("="*60)
    
    tests = [
        ("Тест создания продукта", test_product_creation),
        ("Тест операций с категорией", test_category_operations)
    ]
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        try:
            if test_func():
                passed += 1
                print(f"[OK] {test_name} пройден")
            else:
                print(f"[FAIL] {test_name} не пройден")
        except Exception as e:
            print(f"[ERROR] Ошибка в тесте {test_name}: {e}")
    
    print("\n" + "="*60)
    print(f"Всего тестов: {total}")
    print(f"Пройдено: {passed}")
    
    if passed == total:
        print("[OK] ВСЕ ТЕСТЫ ПРОЙДЕНЫ!")
    else:
        print(f"[FAIL] Не пройдено тестов: {total - passed}")
    
    print("="*60)
    return passed == total
if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
