import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from src.models import Product, Category

# Создаем тестовые данные
p1 = Product("Товар 1", "Описание", 100, 2)
p2 = Product("Товар 2", "Описание", 200, 3)

category = Category("Тест", "Описание", [p1, p2])

print("Тип возвращаемого значения products:", type(category.products))
print("Значение products:", repr(category.products))
print("Длина строки:", len(category.products))
print()
print("Вывод геттера:")
print(category.products)
