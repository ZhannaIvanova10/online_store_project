#!/usr/bin/env python3
"""Запуск всех тестов."""
import sys
import os
import pytest

# Добавляем текущую директорию в путь
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Запускаем pytest
if __name__ == "__main__":
    exit_code = pytest.main(["-v", "--cov=src", "--cov-report=term-missing", "tests/"])
    sys.exit(exit_code)
