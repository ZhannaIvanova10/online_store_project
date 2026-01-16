"""
Тесты для основного модуля.
"""

import sys
import os
import io
import contextlib

# Добавляем путь к src в PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.main import main, demonstrate_exceptions, create_sample_data, print_store_info


class TestMain:
    """Тесты для основного модуля."""

    def test_main_output(self, capsys):
        """Проверяем, что main.py выводит ожидаемый текст."""
        main()
        captured = capsys.readouterr()
        output = captured.out
        
        # Проверяем, что вывод содержит ожидаемые строки
        assert "ОНОЛАЙН-МАГАЗИН: Демонстрация обработки исключений" in output
        assert "Категория: Электроника" in output
        assert "ДЕМОНСТРАЦИЯ ОБРАБОТКИ ИСКЛЮЧЕНИЙ" in output
    def test_create_sample_data(self):
        """Тест создания примерных данных."""
        store = create_sample_data()
        assert store.name == "Электроника"
        assert len(store.products) == 3  # Ноутбук, мышь, смартфон

    def test_demonstrate_exceptions(self, capsys):
        """Тест демонстрации исключений."""
        store = create_sample_data()
        demonstrate_exceptions(store)
        captured = capsys.readouterr()
        output = captured.out
        
        assert "Попытка создать товар с quantity = 0:" in output
        assert "Попытка добавить строку вместо продукта:" in output
        assert "Средняя цена пустой категории:" in output

    def test_print_store_info(self, capsys):
        """Тест вывода информации о магазине."""
        store = create_sample_data()
        print_store_info(store)
        captured = capsys.readouterr()
        output = captured.out
        assert "Категория: Электроника" in output
        assert "Количество товаров в категории: 3" in output
        assert "Товары в категории:" in output
        assert "Средняя цена товаров:" in output
