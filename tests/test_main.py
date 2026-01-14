"""
Тесты для основного модуля main.py.
"""

import sys
import os
import tempfile
import json

# Добавляем путь к src в PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.main import main, create_sample_data, print_store_info, load_and_print_json_data
from io import StringIO
import contextlib
def test_main_output():
    """Тест вывода основной функции."""
    # Перенаправляем stdout
    output = StringIO()
    with contextlib.redirect_stdout(output):
        main()
    
    captured_output = output.getvalue()
    
    # Проверяем обязательные элементы вывода
    assert "ДЕМОНСТРАЦИЯ РАБОТЫ ИНТЕРНЕТ-МАГАЗИНА" in captured_output
    assert "Примерные данные:" in captured_output
    assert "ДЕМОНСТРАЦИЯ МАГИЧЕСКИХ МЕТОДОВ" in captured_output
    assert "ЗАГРУЗКА ИЗ JSON ФАЙЛА" in captured_output
    assert "Электроника" in captured_output
    assert "Книги" in captured_output
    assert "Ноутбук" in captured_output
    assert "Смартфон" in captured_output
def test_main_is_callable():
    """Тест, что main() является вызываемой функцией."""
    assert callable(main)


def test_load_and_print_json_data():
    """Тест функции load_and_print_json_data."""
    # Создаем временный JSON файл для тестирования
    test_data = [
        {
            "name": "Test Category",
            "description": "Test description",
            "products": [
                {
                    "name": "Test Product",
                    "description": "Test product description",
                    "price": 100.0,
                    "quantity": 5,
                }
            ],
        }
    ]
    temp_file = tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, encoding="utf-8"
    )
    json.dump(test_data, temp_file, ensure_ascii=False)
    temp_file.close()
    
    try:
        # Перенаправляем stdout
        output = StringIO()
        with contextlib.redirect_stdout(output):
            load_and_print_json_data(temp_file.name)
        
        captured_output = output.getvalue()
        
        # Проверяем вывод
        assert "Загрузка данных из файла" in captured_output
        assert "Test Category" in captured_output
        assert "Test description" in captured_output
        
    finally:
        if os.path.exists(temp_file.name):
            os.unlink(temp_file.name)
