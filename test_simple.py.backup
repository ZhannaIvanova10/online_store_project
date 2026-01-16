"""Простейшие тесты."""
import sys
sys.path.insert(0, 'src')

def test_basics():
    """Базовые тесты."""
    from models import Product, Category
    
    # 1. Нормальное создание продукта
    p = Product("Тест", "Описание", 100, 5)
    assert p.name == "Тест"
    assert p.price == 100
    assert p.quantity == 5
    print("✅ Нормальное создание продукта")
    # 2. Создание категории
    c = Category("Категория", "Описание")
    assert c.name == "Категория"
    print("✅ Создание категории")
    
    # 3. Добавление продукта в категорию
    c.add_product(p)
    assert len(c.products) == 1
    print("✅ Добавление продукта в категорию")
    
    # 4. Расчет средней цены
    avg = c.calculate_average_price()
    assert avg == 100.0
    print("✅ Расчет средней цены")
    # 5. Пустая категория
    empty = Category("Пустая", "Нет товаров")
    assert empty.calculate_average_price() == 0.0
    print("✅ Средняя цена пустой категории")
    
    return True

def test_exceptions():
    """Тесты исключений."""
    from models import Product, Category
    
    # 1. Исключение при quantity=0
    try:
        Product("Тест", "Описание", 100, 0)
        print("❌ Должно было быть исключение для quantity=0")
        return False
    except ValueError:
        print("✅ Исключение при quantity=0")
    # 2. Исключение при отрицательном quantity
    try:
        Product("Тест", "Описание", 100, -1)
        print("❌ Должно было быть исключение для quantity=-1")
        return False
    except ValueError:
        print("✅ Исключение при quantity=-1")
    
    # 3. Исключение при добавлении не-продукта
    cat = Category("Тест", "Тест")
    try:
        cat.add_product("строка")
        print("❌ Должно было быть исключение для не-продукта")
        return False
    except TypeError:
        print("✅ Исключение при добавлении не-продукта")
    return True

def main():
    """Основная функция."""
    print("="*60)
    print("ПРОСТЕЙШИЕ ТЕСТЫ ПРОЕКТА")
    print("="*60)
    
    results = []
    try:
        results.append(test_basics())
    except Exception as e:
        print(f"❌ Ошибка в базовых тестах: {e}")
        results.append(False)
    
    try:
        results.append(test_exceptions())
    except Exception as e:
        print(f"❌ Ошибка в тестах исключений: {e}")
        results.append(False)
    print("="*60)
    print(f"Всего тестов: {len(results)}")
    print(f"Пройдено: {sum(results)}")
    
    if all(results):
        print("✅ ВСЕ ТЕСТЫ ПРОЙДЕНЫ!")
    else:
        print("❌ ЕСТЬ НЕПРОЙДЕННЫЕ ТЕСТЫ")
    print("="*60)

if __name__ == "__main__":
    main()
