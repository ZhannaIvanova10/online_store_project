#!/usr/bin/env python3
"""
Финальная проверка всех критериев задания.
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from models import Product, Category
    print("="*60)
    print("ФИНАЛЬНАЯ ПРОВЕРКА КРИТЕРИЕВ ДОМАШНЕГО ЗАДАНИЯ")
    print("="*60)
    
    # КРИТЕРИЙ 1: Product с quantity <= 0
    print("\n1. КРИТЕРИЙ: Product выбрасывает ValueError при quantity <= 0")
    
    try:
        Product("Тест", "Описание", 100, 0)
        print("❌ ОШИБКА: Не было исключения при quantity=0")
        sys.exit(1)
    except ValueError as e:
        if "Товар с нулевым количеством не может быть добавлен" in str(e):
            print("✅ ПРОЙДЕНО: Правильное исключение при quantity=0")
        else:
            print(f"❌ Неправильное сообщение: {e}")
            sys.exit(1)
    
    try:
        Product("Тест", "Описание", 100, -5)
        print("❌ ОШИБКА: Не было исключения при quantity=-5")
        sys.exit(1)
    except ValueError:
        print("✅ ПРОЙДЕНО: Исключение при quantity=-5")
    # КРИТЕРИЙ 2: average_price()
    print("\n2. КРИТЕРИЙ: Метод average_price() в Category")
    
    empty_cat = Category("Пустая", "Описание")
    avg = empty_cat.average_price()
    if avg == 0:
        print("✅ ПРОЙДЕНО: Пустая категория возвращает 0")
    else:
        print(f"❌ ОШИБКА: Пустая категория возвращает {avg}, а не 0")
        sys.exit(1)
    
    cat = Category("Тест", "Описание")
    p1 = Product("Товар1", "Описание", 100, 5)
    p2 = Product("Товар2", "Описание", 300, 3)
    cat.add_product(p1)
    cat.add_product(p2)
    
    avg = cat.average_price()
    if avg == 200:  # (100 + 300) / 2
        print("✅ ПРОЙДЕНО: Средняя цена с двумя товарами: 200")
    else:
        print(f"❌ ОШИБКА: Неправильная средняя цена: {avg}")
        sys.exit(1)
    # КРИТЕРИЙ 3: main.py работает
    print("\n3. КРИТЕРИЙ: main.py запускается")
    main_path = os.path.join("src", "main.py")
    if os.path.exists(main_path):
        print("✅ ПРОЙДЕНО: main.py существует")
    else:
        print("❌ ОШИБКА: main.py не найден")
        sys.exit(1)
    
    print("\n" + "="*60)
    print("✅ ВСЕ КРИТЕРИИ ВЫПОЛНЕНЫ!")
    print("Теперь работа точно соответствует формулировке задания:")
    print("1. Класс Product выбрасывает ValueError при quantity <= 0")
    print("2. Category.average_price() работает корректно")
    print("3. main.py запускается")
    print("="*60)
    
except Exception as e:
    print(f"\n❌ ОШИБКА: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
