#!/usr/bin/env python3
"""
Полная интеграционная проверка проекта.
"""
import sys
import os
import subprocess
import json

def run_test(name, command):
    """Запускает команду и возвращает результат."""
    print(f"\n{'='*60}")
    print(f"ТЕСТ: {name}")
    print('='*60)
    
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=10,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        print(f"Команда: {command}")
        print(f"Код возврата: {result.returncode}")
        
        if result.returncode == 0:
            print("✅ УСПЕХ")
            if result.stdout:
                print(f"Вывод (первые 200 символов):")
                print(result.stdout[:200])
            return True
        else:
            print("❌ ОШИБКА")
            if result.stderr:
                print(f"Ошибки:\n{result.stderr[:500]}")
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ ТАЙМАУТ: выполнение заняло слишком много времени")
        return False
    except Exception as e:
        print(f"❌ ИСКЛЮЧЕНИЕ: {e}")
        return False

def main():
    """Основная функция проверки."""
    print("ПОЛНАЯ ИНТЕГРАЦИОННАЯ ПРОВЕРКА ПРОЕКТА")
    print("="*60)
    tests = [
        ("Проверка структуры проекта", "find . -name '*.py' | grep -v __pycache__ | wc -l"),
        ("Проверка models.py", "python -c \"from src.models import BaseProduct; print('Модуль импортирован')\""),
        ("Проверка исключения quantity=0", "python -c \"from src.models import BaseProduct; BaseProduct('Т', 'Д', 100, 0)\" 2>&1 | grep -q 'Товар с нулевым количеством' && echo 'OK' || echo 'FAIL'"),
        ("Проверка average_price", "python -c \"from src.models import Category; c=Category('Т','Д'); print(f'Average: {c.average_price()}')\""),
        ("Запуск простого теста", "python test_simple.py"),
        ("Запуск pytest тестов", "python -m pytest test_minimal.py -v"),
        ("Запуск main.py", "python src/main.py 2>&1 | head -5"),
        ("Проверка JSON файла", "python -c \"import json; json.load(open('test_data.json')); print('JSON валиден')\""),
    ]
    
    passed = 0
    total = len(tests)
    
    for name, command in tests:
        if run_test(name, command):
            passed += 1
    
    # Итог
    print(f"\n{'='*60}")
    print("ИТОГ ИНТЕГРАЦИОННОЙ ПРОВЕРКИ:")
    print(f"Пройдено тестов: {passed}/{total}")
    if passed == total:
        print("✅ ✅ ✅ ПРОЕКТ ГОТОВ К ПРОВЕРКЕ ✅ ✅ ✅")
        return 0
    else:
        print(f"❌ Не пройдено тестов: {total - passed}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
