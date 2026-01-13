"""Основной модуль для демонстрации работы классов Product и Category."""
from src.models import Product, Category, load_categories_from_json
import os


def create_sample_data():
    """Создание тестовых данных для демонстрации."""
    product1 = Product("iPhone 15", "Смартфон от Apple", 999.99, 10)
    product2 = Product("Samsung Galaxy S23", "Смартфон от Samsung", 899.99, 15)
    product3 = Product("Наушники Sony", "Беспроводные наушники", 199.99, 30)

    smartphones = Category("Смартфоны", "Мобильные телефоны", [product1, product2])
    accessories = Category("Аксессуары", "Аксессуары для техники", [product3])

    return smartphones, accessories


def print_store_info(category1, category2):
    """Вывод информации о магазине."""
    print("=" * 50)
    print("ИНФОРМАЦИЯ О МАГАЗИНЕ")
    print("=" * 50)

    print(f"\nКатегория: {category1.name}")
    print(f"Описание: {category1.description}")
    print(f"Товаров в категории: {len(category1.products)}")

    print(f"\nКатегория: {category2.name}")
    print(f"Описание: {category2.description}")
    print(f"Товаров в категории: {len(category2.products)}")

    print(f"\n{'=' * 50}")
    print(f"Всего категорий в магазине: {Category.category_count}")
    print(f"Всего уникальных товаров в магазине: {Category.product_count}")
    print(f"{'=' * 50}")


def load_and_print_json_data():
    """Загрузка и вывод данных из JSON файла."""
    json_path = "products.json"

    if os.path.exists(json_path):
        print("\n" + "=" * 50)
        print("ДАННЫЕ ИЗ JSON-ФАЙЛА")
        print("=" * 50)

        # Сбрасываем счетчики для демонстрации
        original_category_count = Category.category_count
        original_product_count = Category.product_count

        Category.category_count = 0
        Category.product_count = 0

        categories = load_categories_from_json(json_path)

        for category in categories:
            print(f"\nКатегория: {category.name}")
            print(f"Описание: {category.description}")
            print(f"Товаров в категории: {len(category.products)}")
            for product in category.products:
                print(f"  - {product.name}: ${product.price}")

        print(f"\n{'=' * 50}")
        print(f"Всего категорий загружено: {Category.category_count}")
        print(f"Всего товаров загружено: {Category.product_count}")
        print(f"{'=' * 50}")

        # Восстанавливаем счетчики
        Category.category_count = original_category_count
        Category.product_count = original_product_count
    else:
        print(f"\nФайл {json_path} не найден")


def main():
    """Основная функция для демонстрации работы."""
    cat1, cat2 = create_sample_data()
    print_store_info(cat1, cat2)
    load_and_print_json_data()


if __name__ == "__main__":
    main()
