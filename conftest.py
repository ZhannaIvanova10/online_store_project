"""
Конфигурация pytest для проекта.
Добавляет src в путь импорта.
"""
import sys
import os

# Добавляем src в путь Python
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
