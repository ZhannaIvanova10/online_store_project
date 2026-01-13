"""
Основной модуль интернет-магазина.
"""

from src.models import Product, Category, load_categories_from_json


def create_sample_data():
    """Создает тестовые данные для демонстрации."""
    # Создаем товары
    product1 = Product("iPhone 15", "Смартфон Apple", 999.99, 10)
    product2 = Product("Samsung Galaxy S24", "Смартфон Samsung", 899.99, 15)
    product3 = Product("Наушники Sony", "Беспроводные наушники", 199.99, 30)
    
    # Создаем категории
    category1 = Category("Смартфоны", "Мобильные телефоны")
    category2 = Category("Аксессуары", "Аксессуары для техники")
    
    # Добавляем товары через метод add_product
    category1.add_product(product1)
    category1.add_product(product2)
    category2.add_product(product3)
    
    return category1, category2
def print_store_info(*categories):
    """Выводит информацию о магазине."""
    print("=" * 50)
    print("ИНФОРМАЦИЯ О МАГАЗИНЕ")
    print("=" * 50)
    
    for category in categories:
        print(f"\n{category.name}:")
        print(f"Описание: {category.description}")
        print("Товары:")
        if category.products:  # Используем геттер
            print(category.products)
        else:
            print("Нет товаров")
    
    print(f"\nВсего категорий в магазине: {Category.category_count}")
    print(f"Всего уникальных товаров в магазине: {Category.product_count}")
def test_new_functionality():
    """Тестирует новую функциональность."""
    print("\n" + "=" * 50)
    print("ТЕСТИРОВАНИЕ НОВОЙ ФУНКЦИОНАЛЬНОСТИ")
    print("=" * 50)
    
    # 1. Тест приватного атрибута и геттера
    print("\n1. Тест геттера products:")
    category = Category("Тест", "Тестовая категория")
    product = Product("Тестовый товар", "Описание", 100, 5)
    category.add_product(product)
    print("Вывод геттера products:")
    print(category.products)
    
    # 2. Тест сеттера цены
    print("\n2. Тест сеттера цены:")
    product = Product("Тест", "Описание", 100, 5)
    print(f"Изначальная цена: {product.price}")
    
    # Попытка установить отрицательную цену
    print("Попытка установить цену -50...")
    product.price = -50  # Должно вывести сообщение об ошибке
    # Установка корректной цены
    product.price = 150
    print(f"Новая цена: {product.price}")
    
    # 3. Тест класс-метода
    print("\n3. Тест класс-метода new_product:")
    product_data = {
        "name": "Новый товар",
        "description": "Описание нового товара",
        "price": 200.0,
        "quantity": 10
    }
    new_product = Product.new_product(product_data)
    print(f"Создан товар: {new_product}")
    
    # 4. Тест проверки дубликатов
    print("\n4. Тест проверки дубликатов:")
    products_list = [Product("Товар 1", "Описание", 100, 5)]
    duplicate_data = {"name": "Товар 1", "description": "Другое описание", "price": 150, "quantity": 3}
    result = Product.new_product(duplicate_data, products_list)
    print(f"Обновленное количество: {products_list[0].quantity}")
    print(f"Цена: {products_list[0].price}")
    
    # 5. Тест приватного доступа
    print("\n5. Тест приватного доступа:")
    try:
        print(f"Прямой доступ к __price: {product._Product__price}")
    except AttributeError:
        print("Нельзя получить прямой доступ к __price")


def load_and_print_json_data():
    """Загружает и выводит данные из JSON файла."""
    print("\n" + "=" * 50)
    print("ДАННЫЕ ИЗ JSON-ФАЙЛА")
    print("=" * 50)
    try:
        categories = load_categories_from_json("products.json")
        for category in categories:
            print(f"\n{category.name}:")
            print(f"Описание: {category.description}")
            print("Товары:")
            if category.products:
                print(category.products)
            else:
                print("Нет товаров")
    except FileNotFoundError:
        print("Файл products.json не найден")
    except Exception as e:
        print(f"Ошибка при загрузке JSON: {e}")


def main():
    """Основная функция программы."""
    # Создаем тестовые данные
    cat1, cat2 = create_sample_data()
    # Выводим информацию о магазине
    print_store_info(cat1, cat2)
    
    # Тестируем новую функциональность
    test_new_functionality()
    
    # Загружаем данные из JSON
    load_and_print_json_data()


if __name__ == "__main__":
    main()
