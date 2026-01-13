"""
Тесты для основного модуля main.py
"""

import sys
import os
import io
from contextlib import redirect_stdout

# Добавляем путь к src в PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.main import main, load_and_print_json_data


def test_main_output():
    """Тест вывода основной программы."""
    # Сохраняем текущие счетчики
    from src.models import Category

    original_category_count = Category.category_count
    original_product_count = Category.product_count

    # Захватываем вывод программы
    f = io.StringIO()
    with redirect_stdout(f):
        main()

    output = f.getvalue()

    # Проверяем, что вывод содержит ожидаемые строки
    assert "ИНФОРМАЦИЯ О МАГАЗИНЕ" in output
    assert "Смартфоны" in output
    assert "Аксессуары" in output
    assert "Всего категорий в магазине:" in output
    assert "Всего уникальных товаров в магазине:" in output
    # Восстанавливаем счетчики
    Category.category_count = original_category_count
    Category.product_count = original_product_count


def test_main_is_callable():
    """Тест, что main() можно вызвать без ошибок."""
    try:
        # Временно отключаем вывод
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()

        main()

        # Восстанавливаем stdout
        sys.stdout = old_stdout
        assert True
    except Exception as e:
        # Восстанавливаем stdout в случае ошибки
        sys.stdout = old_stdout
        assert False, f"main() вызвал исключение: {e}"


def test_load_and_print_json_data():
    """Тест функции load_and_print_json_data."""
    try:
        f = io.StringIO()
        with redirect_stdout(f):
            load_and_print_json_data()

        output = f.getvalue()
        # Функция должна либо найти файл, либо сообщить, что не нашла
        assert True  # Главное - не упала
    except Exception as e:
        assert False, f"load_and_print_json_data вызвал исключение: {e}"
