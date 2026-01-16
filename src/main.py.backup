"""
Демонстрация домашнего задания: Обработка исключений
"""

import sys
import os

# Добавляем текущую директорию в путь для импортов
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models import (BaseProduct, Product, Smartphone, LawnGrass,
                    Category, LoggingMixin)


def create_sample_data():
    """Создает пример данных для демонстрации."""
    # Создаем товары
    p1 = Product("Ноутбук", "Игровой ноутбук", 89999, 5)
    p2 = Product("Мышь", "Беспроводная мышь", 2499, 20)
    # Создаем смартфон
    phone = Smartphone("Смартфон", "Флагманский смартфон", 79999, 10,
                      "Высокая", "Galaxy S23", 256, "Черный")

    # Создаем категории
    electronics = Category("Электроника", "Техника и гаджеты")
    electronics.add_product(p1)
    electronics.add_product(p2)
    electronics.add_product(phone)

    return electronics


def print_store_info(store):
    """Выводит информацию о магазине."""
    print(f"\nКатегория: {store.name}")
    print(f"Описание: {store.description}")
    print(f"Количество товаров в категории: {len(store.products)}")
    print(f"Общее количество единиц товаров: {len(store)}")

    if store.products:
        print("\nТовары в категории:")
        for i, product in enumerate(store.products, 1):
            print(f"{i}. {product}")
        # Средняя цена
        avg_price = store.calculate_average_price()
        print(f"\nСредняя цена товаров: {avg_price:.2f} руб.")


def demonstrate_exceptions(store):
    """Демонстрирует обработку исключений."""
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ОБРАБОТКИ ИСКЛЮЧЕНИЙ")
    print("=" * 60)
    
    # 1. Попытка создать товар с нулевым количеством
    print("\n1. Попытка создать товар с quantity = 0:")
    try:
        bad_product = Product("Тестовый товар", "Описание", 100, 0)
        print("❌ ОШИБКА: Должно было возникнуть исключение!")
    except ValueError as e:
        print(f"✅ УСПЕХ: Исключение обработано: {e}")

    # 2. Попытка добавить неправильный тип в категорию
    print("\n2. Попытка добавить строку вместо продукта:")
    try:
        store.add_product("не продукт")
        print("❌ ОШИБКА: Должно было возникнуть исключение!")
    except TypeError as e:
        print(f"✅ УСПЕХ: Исключение обработано: {e}")

    # 3. Обработка пустой категории
    print("\n3. Средняя цена пустой категории:")
    empty_cat = Category("Пустая", "Нет товаров")
    print(f"Результат: {empty_cat.calculate_average_price()} (должно быть 0)")

    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 60)
def main():
    """
    Основная функция приложения.
    """
    print("=" * 60)
    print("ОНОЛАЙН-МАГАЗИН: Демонстрация обработки исключений")
    print("=" * 60)

    # Создаем пример данных
    store = create_sample_data()

    # Выводим информацию о магазине
    print_store_info(store)

    # Демонстрация исключений
    demonstrate_exceptions(store)
    
    # Пример работы с продуктами
    if store.products:
        print(f"\nПервый продукт в категории: {store.products[0].name}")

    print("\n" + "=" * 60)
    print("РАБОТА ПРИЛОЖЕНИЯ ЗАВЕРШЕНА")
    print("=" * 60)


if __name__ == "__main__":
    main()
