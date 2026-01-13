"""
Пакет интернет-магазина.
"""

# Экспортируем основные классы и функции
from .models import Product, Category, load_categories_from_json

__all__ = ['Product', 'Category', 'load_categories_from_json']

print(f"Импортирован пакет интернет-магазина")
