#!/usr/bin/env python3
"""Скрипт для проверки всех критериев проекта."""
import subprocess
import sys
import os

def run_command(cmd, description):
    """Запускает команду и выводит результат."""
    print(f"\n{'='*60}")
    print(f"Проверка: {description}")
    print(f"Команда: {cmd}")
    print('='*60)
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Успешно")
            if result.stdout.strip():
                # Ограничим вывод до 500 символов
                output = result.stdout[:500]
                if len(result.stdout) > 500:
                    output += "..."
                print(f"Вывод:\n{output}")
        else:
            print("❌ Ошибка")
            print(f"Код возврата: {result.returncode}")
            if result.stderr:
                error_output = result.stderr[:500]
                if len(result.stderr) > 500:
                    error_output += "..."
                print(f"Ошибка:\n{error_output}")
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Исключение: {e}")
        return False

def main():
    """Основная функция проверки."""
    print("🚀 ПРОВЕРКА ПРОЕКТА 'ИНТЕРНЕТ-МАГАЗИН'")
    print("="*60)
    
    checks = []
    
    # 1. Проверка стиля кода
    checks.append(run_command("python -m flake8 src/", "Стиль кода (flake8)"))
    
    # 2. Запуск программы
    checks.append(run_command("python -m src.main", "Запуск программы"))
    
    # 3. Запуск тестов
    checks.append(run_command("python -m pytest tests/ -q", "Запуск всех тестов"))
    
    # 4. Проверка покрытия
    checks.append(run_command("python -m pytest tests/ --cov=src --cov-report=term", "Покрытие тестами"))
    
    # 5. Итог
    print(f"\n{'='*60}")
    print("ИТОГОВЫЙ РЕЗУЛЬТАТ:")
    print(f"Всего проверок: {len(checks)}")
    print(f"Успешно: {sum(checks)}")
    print(f"Провалено: {len(checks) - sum(checks)}")
    
    if all(checks):
        print("\n🎉 ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ УСПЕШНО!")
        print("Проект готов к сдаче.")
        return 0
    else:
        print("\n⚠️ ЕСТЬ ПРОБЛЕМЫ!")
        print("Некоторые проверки не прошли.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
