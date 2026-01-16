#!/usr/bin/env python3
"""
Тест загрузки данных из JSON.
"""

import sys
import io
import json

# Устанавливаем UTF-8 кодировку для Windows
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Проверяем импорт
print("="*60)
print("ТЕСТ ЗАГРУЗКИ ДАННЫХ ИЗ JSON")
print("="*60)

try:
    from src.models import load_categories_from_json
    print("[OK] Модуль загружен успешно")
except ImportError as e:
    print(f"[FAIL] Ошибка импорта: {e}")
    sys.exit(1)
# Проверяем существование файла
import os
if os.path.exists("test_data.json"):
    print("[OK] Файл test_data.json найден")
else:
    print("[FAIL] Файл test_data.json не найден")
    sys.exit(1)

# Загружаем данные
try:
    categories = load_categories_from_json("test_data.json")
    print(f"\nЗагружено категорий: {len(categories)}")
    
    for category in categories:
        print(f"\n{category.name}:")
        print(f"  Описание: {category.description}")
        print(f"  Товаров: {category.get_products_count()}")
        print(f"  Средняя цена: {category.average_price():.2f} руб.")
        
        for product in category.products:
            print(f"  - {product.name}: {product.price} руб. ({product.quantity} шт.)")
    
    print("\n" + "="*60)
    print("ТЕСТ ЗАВЕРШЕН УСПЕШНО")
    print("="*60)
except Exception as e:
    print(f"\n[FAIL] Ошибка при загрузке: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
