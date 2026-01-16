"""Тест загрузки JSON."""
import sys
import os

print("="*60)
print("ТЕСТ ЗАГРУЗКИ ДАННЫХ ИЗ JSON")
print("="*60)

# Добавляем src в путь
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from models import load_categories_from_json
    print("✅ Модуль загружен успешно")
except ImportError as e:
    print(f"❌ Ошибка импорта: {e}")
    sys.exit(1)
# Проверяем существование файла
if os.path.exists("test_data.json"):
    print("✅ Файл test_data.json найден")
    
    # Загружаем данные
    categories = load_categories_from_json("test_data.json")
    
    print(f"\nЗагружено категорий: {len(categories)}")
    
    if categories:
        for i, category in enumerate(categories, 1):
            print(f"\n{i}. Категория: {category.name}")
            print(f"   Описание: {category.description}")
            print(f"   Количество товаров: {len(category.products)}")
            
            for j, product in enumerate(category.products, 1):
                print(f"   {j}. {product.name}")
                print(f"      Цена: {product.price} руб.")
                print(f"      Количество: {product.quantity} шт.")
    else:
        print("⚠️  Категории не загружены (возможно ошибка в файле)")
else:
    print("❌ Файл test_data.json не найден")
    print("Создаем примерный файл...")
    
    # Создаем примерный JSON
    sample_data = {
        "categories": [
            {
                "name": "Электроника",
                "description": "Электронные устройства",
                "products": [
                    {
                        "name": "Смартфон",
                        "description": "Мощный смартфон",
                        "price": 29999.99,
                        "quantity": 10
                    }
                ]
            }
        ]
    }
    import json
    with open("test_data.json", "w", encoding="utf-8") as f:
        json.dump(sample_data, f, ensure_ascii=False, indent=2)
    
    print("✅ Файл test_data.json создан")
    print("Запустите тест снова")

print("\n" + "="*60)
print("ТЕСТ ЗАВЕРШЕН")
print("="*60)
