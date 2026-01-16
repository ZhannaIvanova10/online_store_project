#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from src.models import BaseProduct, Category
    print("✅ Импорт models успешен")
except ImportError as e:
    print(f"❌ Ошибка импорта models: {e}")

try:
    import src.main
    print("✅ Импорт main успешен")
except ImportError as e:
    print(f"❌ Ошибка импорта main: {e}")

# Тест создания объектов
try:
    p = BaseProduct("Тест", "Описание", 100, 10)
    print("✅ Создание BaseProduct успешно")
except Exception as e:
    print(f"❌ Ошибка создания BaseProduct: {e}")

try:
    cat = Category("Тест", "Описание")
    print("✅ Создание Category успешно")
except Exception as e:
    print(f"❌ Ошибка создания Category: {e}")
