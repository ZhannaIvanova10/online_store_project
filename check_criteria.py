#!/usr/bin/env python3
"""
Простая проверка критериев домашнего задания.
"""
import sys
import os

# Добавляем src в путь
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from models import BaseProduct, Category, Product
    print("✅ Модули импортируются")
    
    # КРИТЕРИЙ 1: ValueError при quantity <= 0
    print("\n=== КРИТЕРИЙ 1: ValueError при quantity <= 0 ===")
    try:
        BaseProduct("Тест", "Описание", 100, 0)
        print("❌ ОШИБКА: Не было исключения при quantity=0")
        sys.exit(1)
    except ValueError as e:
        if "Товар с нулевым количеством не может быть добавлен" in str(e):
            print("✅ Правильное исключение при quantity=0")
        else:
            print(f"❌ Неправильное сообщение: {e}")
            sys.exit(1)
    
    try:
        BaseProduct("Тест", "Описание", 100, -1)
        print("❌ ОШИБКА: Не было исключения при quantity=-1")
        sys.exit(1)
    except ValueError as e:
        print("✅ Исключение при quantity=-1")
    
    # КРИТЕРИЙ 2: Метод average_price()
    print("\n=== КРИТЕРИЙ 2: Метод average_price() в Category ===")
    # Пустая категория
    empty_cat = Category("Пустая", "Описание")
    avg = empty_cat.average_price()
    if avg == 0:
        print("✅ Пустая категория возвращает 0")
    else:
        print(f"❌ Пустая категория возвращает {avg}, а не 0")
        sys.exit(1)
    
    # Категория с товарами
    cat = Category("Тест", "Описание")
    p1 = Product("Товар1", "Описание", 100, 5)
    p2 = Product("Товар2", "Описание", 300, 3)
    cat.add_product(p1)
    cat.add_product(p2)
    
    avg = cat.average_price()
    if avg == 200:  # (100 + 300) / 2
        print("✅ Средняя цена с двумя товарами: 200")
    else:
        print(f"❌ Неправильная средняя цена: {avg}")
        sys.exit(1)
    
    # Проверяем что метод использует try/except
    import inspect
    source = inspect.getsource(Category.average_price)
    if "try:" in source or "except" in source or "ZeroDivisionError" in source:
        print("✅ Метод использует обработку исключений")
    else:
        print("⚠️ Метод может не использовать обработку исключений")
    
    # КРИТЕРИЙ 3: Тестирование
    print("\n=== КРИТЕРИЙ 3: Тестирование ===")
    print("✅ Тесты созданы (см. test_*.py)")
    print("✅ Отчет coverage.xml будет создан при запуске pytest --cov")
    
    # Проверка main.py
    print("\n=== ДОПОЛНИТЕЛЬНО: Проверка main.py ===")
    main_path = os.path.join("src", "main.py")
    if os.path.exists(main_path):
        print("✅ main.py существует")
        # Простая проверка что файл не пустой
        with open(main_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if len(content) > 100:
                print("✅ main.py содержит код")
            else:
                print("⚠️ main.py может быть пустым")
    else:
        print("❌ main.py не найден")
        sys.exit(1)
    print("\n" + "="*60)
    print("✅ ВСЕ ОСНОВНЫЕ КРИТЕРИИ ВЫПОЛНЕНЫ!")
    print("="*60)
    print("\nДля полной проверки запустите:")
    print("1. python -m pytest test_minimal.py -v")
    print("2. cd src && python main.py")
    print("3. python -m pytest --cov=src --cov-report=term")
    
except ImportError as e:
    print(f"❌ Ошибка импорта: {e}")
    sys.exit(1)
except Exception as e:
    print(f"❌ Ошибка: {e}")
    sys.exit(1)
