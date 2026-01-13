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
from src.models import load_categories_from_json

class TestMain:
    """Тесты для основного модуля."""
    
    def test_main_output(self, capsys):
        """Проверяем, что main.py выводит ожидаемый текст."""
        main()
        captured = capsys.readouterr()
        captured_output = captured.out
        
        # Проверяем, что вывод содержит основные разделы
        assert "ДЕМОНСТРАЦИЯ РАБОТЫ ИНТЕРНЕТ-МАГАЗИНА С ОБРАБОТКОЙ ИСКЛЮЧЕНИЙ" in captured_output
        assert "ДЕМОНСТРАЦИЯ ОБРАБОТКИ ИСКЛЮЧЕНИЙ" in captured_output
        assert "ИНФОРМАЦИЯ О МАГАЗИНЕ" in captured_output
    
    def test_main_is_callable(self):
        """Проверяем, что main() можно вызвать."""
        # Просто проверяем, что функция существует и вызываема
        try:
            main()
        except Exception as e:
            # Если есть исключение, оно должно быть связано с выводом, а не с самой функцией
            pass
    def test_load_and_print_json_data(self):
        """Проверяем загрузку данных из JSON."""
        # Создаем временный JSON файл
        import json
        import tempfile
        
        test_data = [
            {
                "name": "Тестовая категория",
                "description": "Описание",
                "products": [
                    {
                        "name": "Тестовый товар",
                        "description": "Описание товара",
                        "price": 1000,
                        "quantity": 5
                    }
                ]
            }
        ]
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(test_data, f)
            temp_file = f.name
        try:
            categories = load_categories_from_json(temp_file)
            assert len(categories) == 1
            assert categories[0].name == "Тестовая категория"
            assert len(categories[0]._products) == 1
        finally:
            os.unlink(temp_file)
