import pytest
import json
import os
from src.models import (
    BaseProduct, Product, Smartphone, LawnGrass, 
    Category, LoggingMixin, load_categories_from_json
)

# Тестируем все методы BaseProduct
def test_base_product_full():
    p = BaseProduct("Тест", "Описание", 100, 10)
    # Проверяем все атрибуты
    assert p.name == "Тест"
    assert p.description == "Описание"
    assert p.price == 100
    assert p.quantity == 10
    # Проверяем __str__
    s = str(p)
    assert "Тест" in s
    assert "100" in s
    assert "10" in s
# Тестируем Product (наследник BaseProduct)
def test_product_inheritance():
    p = Product("Тест", "Описание", 100, 10)
    assert isinstance(p, BaseProduct)
    assert p.name == "Тест"

# Тестируем Smartphone полностью
def test_smartphone_full():
    phone = Smartphone(
        name="Телефон",
        description="Смартфон",
        price=50000,
        quantity=3,
        performance="Высокая",
        model="Model X",
        memory=128,
        color="Black"
    )
    assert phone.name == "Телефон"
    assert phone.price == 50000
    assert phone.quantity == 3
    assert phone.model == "Model X"
    assert phone.memory == 128
    assert phone.color == "Black"
    assert phone.performance == "Высокая"
    # Проверяем __str__
    s = str(phone)
    assert "Телефон" in s
    assert "Model X" in s
    assert "128" in s
    assert "Black" in s

# Тестируем LawnGrass полностью
def test_lawn_grass_full():
    grass = LawnGrass(
        name="Трава",
        description="Газонная",
        price=300,
        quantity=50,
        country="Россия",
        germination_period="2 недели",
        color="Зеленый"
    )
    assert grass.name == "Трава"
    assert grass.price == 300
    assert grass.quantity == 50
    assert grass.country == "Россия"
    assert grass.germination_period == "2 недели"
    assert grass.color == "Зеленый"
# Тестируем Category полностью
def test_category_full():
    cat = Category("Тест", "Описание")
    assert cat.name == "Тест"
    assert cat.description == "Описание"
    assert cat.products == []
    assert cat.total_products == 0
    assert len(cat) == 0
    
    # Проверяем __str__
    s = str(cat)
    assert "Тест" in s
    
    # Проверяем average_price пустой категории
    assert cat.average_price() == 0.0
    
    # Добавляем продукт
    p = Product("Товар", "Описание", 100, 5)
    cat.add_product(p)
    
    # Проверяем после добавления
    assert cat.total_products == 1
    assert len(cat) == 1
    assert p in cat
    assert cat.average_price() == 100
    # Проверяем __contains__
    assert p in cat
    other = Product("Другой", "Описание", 200, 3)
    assert other not in cat

# Тестируем LoggingMixin
def test_logging_mixin():
    class TestClass(LoggingMixin):
        pass
    
    obj = TestClass()
    # Просто проверяем что метод существует
    assert hasattr(obj, 'log')
    
    # Можно проверить что он не падает
    try:
        obj.log("Тестовое сообщение")
        # Если не упало - хорошо
        assert True
    except:
        assert False, "Метод log должен работать"

# Тестируем edge cases для average_price
def test_average_price_edge_cases():
    cat = Category("Тест", "Описание")
    # Пустая категория
    assert cat.average_price() == 0.0
    
    # Один продукт
    p1 = Product("Товар1", "Описание", 100, 1)  # quantity должен быть > 0
    # quantity=0 вызовет ValueError, поэтому создаем с quantity=1
    p1 = Product("Товар1", "Описание", 100, 1)
    cat.add_product(p1)
    assert cat.average_price() == 100
    
    # Несколько продуктов
    p2 = Product("Товар2", "Описание", 300, 2)
    cat.add_product(p2)
    assert cat.average_price() == 200  # (100 + 300) / 2
    
    # Продукт с ценой 0
    p3 = Product("Товар3", "Описание", 0, 3)
    cat.add_product(p3)
    # Теперь (100 + 300 + 0) / 3 = 133.33
    assert cat.average_price() == pytest.approx(133.33, 0.01)
# Тестируем исключения
def test_exceptions():
    # BaseProduct с quantity=0
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        BaseProduct("Тест", "Описание", 100, 0)
    
    # BaseProduct с quantity=-1
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        BaseProduct("Тест", "Описание", 100, -1)
    
    # Category.add_product с не-продуктом
    cat = Category("Тест", "Описание")
    with pytest.raises(TypeError):
        cat.add_product("не продукт")
    
    with pytest.raises(TypeError):
        cat.add_product(None)
    
    with pytest.raises(TypeError):
        cat.add_product(123)

# Тестируем load_categories_from_json с разными сценариями
def test_load_json_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_categories_from_json("несуществующий_файл.json")
def test_load_json_invalid(tmp_path):
    # Создаем невалидный JSON
    test_file = tmp_path / "test.json"
    test_file.write_text("{ это не json }", encoding='utf-8')
    
    with pytest.raises(json.JSONDecodeError):
        load_categories_from_json(str(test_file))

def test_load_json_valid(tmp_path):
    # Создаем валидный JSON
    test_data = [
        {
            "name": "Категория1",
            "description": "Описание1",
            "products": [
                {
                    "name": "Товар1",
                    "description": "Описание товара1",
                    "price": 100.0,
                    "quantity": 5
                },
                {
                    "name": "Товар2",
                    "description": "Описание товара2",
                    "price": 200.0,
                    "quantity": 3
                }
            ]
        },
        {
            "name": "Категория2",
            "description": "Описание2",
            "products": []
        }
    ]
    
    test_file = tmp_path / "test.json"
    test_file.write_text(json.dumps(test_data), encoding='utf-8')
    
    categories = load_categories_from_json(str(test_file))
    assert len(categories) == 2
    
    cat1 = categories[0]
    assert cat1.name == "Категория1"
    assert cat1.total_products == 2
    assert cat1.average_price() == 150.0  # (100 + 200) / 2
    cat2 = categories[1]
    assert cat2.name == "Категория2"
    assert cat2.total_products == 0
    assert cat2.average_price() == 0.0

def test_load_json_missing_fields(tmp_path):
    # JSON с отсутствующими полями
    test_data = [
        {
            "name": "Категория",
            # Нет description - должно использоваться значение по умолчанию
            "products": [
                {
                    "name": "Товар",
                    # Нет description у товара
                    "price": 100,
                    "quantity": 5
                }
            ]
        }
    ]
    test_file = tmp_path / "test.json"
    test_file.write_text(json.dumps(test_data), encoding='utf-8')
    
    categories = load_categories_from_json(str(test_file))
    assert len(categories) == 1
    assert categories[0].description == ""  # Пустая строка по умолчанию
    assert categories[0].total_products == 1
    assert categories[0].products[0].description == ""  # Пустая строка по умолчанию

def test_load_json_zero_quantity_product(tmp_path):
    # JSON с товаром quantity=0 - должно вызывать ValueError
    test_data = [
        {
            "name": "Категория",
            "description": "Описание",
            "products": [
                {
                    "name": "Товар",
                    "description": "Описание",
                    "price": 100,
                    "quantity": 0  # Это вызовет ValueError!
                }
            ]
        }
    ]
    test_file = tmp_path / "test.json"
    test_file.write_text(json.dumps(test_data), encoding='utf-8')
    
    # Загрузка должна пройти (обработка исключения внутри функции)
    categories = load_categories_from_json(str(test_file))
    # Товар с quantity=0 не должен быть добавлен
    assert categories[0].total_products == 0

# Тестируем test_data.json который уже есть
def test_existing_test_data():
    if os.path.exists("test_data.json"):
        categories = load_categories_from_json("test_data.json")
        # Просто проверяем что не падает
        assert isinstance(categories, list)
        for cat in categories:
            assert isinstance(cat, Category)
            assert hasattr(cat, 'name')
            assert hasattr(cat, 'products')

# Тестируем что все классы могут быть созданы
def test_all_classes_instantiable():
    # BaseProduct
    bp = BaseProduct("BP", "Desc", 100, 1)
    assert bp is not None
    # Product
    p = Product("P", "Desc", 100, 1)
    assert p is not None
    
    # Smartphone
    sp = Smartphone("SP", "Desc", 100, 1, "Perf", "Model", 128, "Black")
    assert sp is not None
    
    # LawnGrass
    lg = LawnGrass("LG", "Desc", 100, 1, "Country", "Period", "Green")
    assert lg is not None
    
    # Category
    cat = Category("Cat", "Desc")
    assert cat is not None
    
    # LoggingMixin через наследника
    class TestMixin(LoggingMixin):
        pass
    tm = TestMixin()
    assert tm is not None
