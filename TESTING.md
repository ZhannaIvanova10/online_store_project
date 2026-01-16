# Инструкция по тестированию
## 🧪 Запуск тестов

### 1. Минимальные тесты (основные критерии):
```bash
python -m pytest test_minimal.py -v
python -m pytest test_complete.py -v
python -m pytest test_additional.py -v
python -m pytest test_*.py -v
cd src && python -m pytest ../test_*.py --cov=. --cov-report=term
