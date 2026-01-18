# ДЗ 3: Обработка исключений
## Описание
Проект для домашнего задания №3 по обработке исключений в интернет-магазине.

## Структура

.
├── src/models.py # Основные классы Product, Category
├── tests/test_models_exceptions.py # Тесты для ДЗ 3
├── main.py # Демонстрация работы
├── requirements.txt # Зависимости
├── ОТЧЕТ_ДЗ3.md # Отчет о выполнении
└── htmlcov/ # Отчет о покрытии (генерируется)

## Установка
```bash
pip install -r requirements.txt
Запуск тестов
python -m pytest tests/
Запуск демонстрации
python main.py
Генерация отчета о покрытии
python -m pytest tests/ --cov=src --cov-report=html
Выполненные критерии
✅ Критерий 1: Инициализация Product с нулевым количеством

✅ Критерий 2: Метод calculate_average_price() в Category

✅ Критерий 3: Тестирование (11 тестов, покрытие >75%)

✅ Дополнительное задание: ZeroQuantityError и try/except/else/finally
