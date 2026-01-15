"""
Основной модуль интернет-магазина с демонстрацией обработки исключений.
"""

import sys
import os

# Добавляем путь для импорта модулей
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from .models import (BaseProduct, Product, Smartphone, LawnGrass, 
                     Category, LoggingMixin, 
                     load_categories_from_json, OrderItem)


def demonstrate_exceptions():
    """Демонстрация работы с исключениями."""
    print("\n" + "=" * 70)
    print("ДЕМОНСТРАЦИЯ ОБРАБОТКИ ИСКЛЮЧЕНИЙ")
    print("=" * 70)
    
    print("\n1. Создание товара с нулевым количеством (ValueError):")
    print("-" * 50)
    
    try:
        print("Пытаемся создать товар с quantity=0...")
        bad_product = Product("Несуществующий товар", "Описание", 100, 0)
        print("ОШИБКА: Этот код не должен был выполниться")
    except ValueError as e:
        print(f"[OK] Поймано исключение ValueError: {e}")
    
    print("\n2. Создание товара с корректным количеством:")
    print("-" * 50)
    
    try:
        good_product = Product("Книга", "Художественная литература", 500, 10)
        print(f"[OK] Товар создан успешно: {good_product}")
    except ValueError as e:
        print(f"ОШИБКА: {e}")
    
    print("\n3. Метод get_average_price() в Category:")
    print("-" * 50)
    # Создаем категорию с товарами
    products = [
        Product("Товар 1", "Описание", 100, 5),
        Product("Товар 2", "Описание", 200, 3),
        Product("Товар 3", "Описание", 300, 2),
    ]
    
    category_with_products = Category("Категория с товарами", "Описание", products)
    average_price = category_with_products.get_average_price()
    print(f"Средняя цена в категории с товарами: {average_price:.2f} руб.")
    
    # Создаем пустую категорию
    empty_category = Category("Пустая категория", "Нет товаров")
    empty_average = empty_category.get_average_price()
    print(f"Средняя цена в пустой категории: {empty_average} руб.")
    
    print("\n4. Добавление товара в категорию с проверкой:")
    print("-" * 50)
    
    category = Category("Тестовая категория", "Для демонстрации")
    
    print("Пытаемся добавить товар с нулевым количеством...")
    try:
        zero_product = Product("Товар с 0", "Описание", 100, 0)
        print("ОШИБКА: Товар не должен был быть создан")
    except ValueError as e:
        print(f"[OK] Товар не создан: {e}")
    print("\nПытаемся добавить корректный товар...")
    try:
        category.add_product(good_product)
    except Exception as e:
        print(f"ОШИБКА: {e}")
    
    print("\n5. Дополнительное задание: пользовательское исключение :")
    print("-" * 50)
    
    try:
        print("Создаем OrderItem с quantity=0...")
        order_item = OrderItem(good_product, 0)
        print("ОШИБКА: Заказ не должен был быть создан")
    except  as e:
        print(f"[OK] Поймано пользовательское исключение : {e}")
    
    print("\nСоздаем OrderItem с корректным количеством...")
    try:
        order_item = OrderItem(good_product, 3)
        print(f"[OK] Заказ создан: {order_item}")
    except  as e:
        print(f"ОШИБКА: {e}")
    print("\n6. Добавление товара с нулевым количеством через add_product:")
    print("-" * 50)
    
    # Сначала создадим товар с количеством 1
    temp_product = Product("Временный товар", "Описание", 50, 1)
    
    # Затем попробуем изменить количество на 0 и добавить
    try:
        print("Устанавливаем quantity=0 у существующего товара...")
        temp_product.quantity = 0
        category.add_product(temp_product)
        print("ОШИБКА: Товар не должен был быть добавлен")
    except  as e:
        print(f"[OK] Поймано : {e}")


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
        print(f"Средняя цена товаров: {category.get_average_price():.2f} руб.")
        
        if category.products:
            print("\nТовары в категории:")
            print(category.products)
        else:
            print("\nВ категории нет товаров")
def main():
    """Основная функция программы."""
    print("ДЕМОНСТРАЦИЯ РАБОТЫ ИНТЕРНЕТ-МАГАЗИНА С ОБРАБОТКОЙ ИСКЛЮЧЕНИЙ")
    print("=" * 70)
    
    # Демонстрация 1: Обработка исключений
    demonstrate_exceptions()
    
    # Демонстрация 2: Создание и вывод примерных данных
    print("\n" + "=" * 70)
    print("2. ПРИМЕРНЫЕ ДАННЫЕ С РАЗНЫМИ ТИПАМИ ТОВАРОВ:")
    print("=" * 70)
    
    sample_categories = create_sample_data()
    print_store_info(sample_categories)
    
    # Демонстрация 3: Работа с get_average_price
    print("\n" + "=" * 70)
    print("3. РАБОТА С МЕТОДОМ get_average_price():")
    print("=" * 70)
    
    print("\nПроверка средней цены для разных категорий:")
    for category in sample_categories:
        avg_price = category.get_average_price()
        print(f"  {category.name}: {avg_price:.2f} руб.")
    
    # Проверка пустой категории
    empty_category = Category("Тестовая пустая", "Без товаров")
    print(f"\n  Пустая категория '{empty_category.name}': {empty_category.get_average_price()} руб.")
    print("\n" + "=" * 70)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 70)


if __name__ == "__main__":
    main()
