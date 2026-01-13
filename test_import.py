import sys
import os

# Добавляем текущую директорию в PYTHONPATH
sys.path.insert(0, os.path.abspath('.'))

try:
    # Пробуем импортировать
    from src.models import Product, Category
    print("✅ Успешный импорт из src.models")
    
    # Тестируем создание объектов
    p = Product("Test", "Desc", 100, 5)
    print(f"✅ Product создан: {p.name} = {p.price} руб.")
    
    c = Category("Test Cat", "Desc")
    c.add_product(p)
    print(f"✅ Category создана, products: {c.products}")
    
    print("\n🎉 Все базовые тесты пройдены!")
    
except Exception as e:
    print(f"❌ Ошибка: {e}")
    import traceback
    traceback.print_exc()
