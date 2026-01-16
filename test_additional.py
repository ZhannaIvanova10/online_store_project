import pytest
from src.models import Smartphone, LawnGrass, Category

def test_smartphone_creation():
    """Тест создания смартфона."""
    phone = Smartphone(
        name="iPhone",
        description="Смартфон",
        price=99999,
        quantity=5,
        performance="Высокая",
        model="15 Pro",
        memory=256,
        color="Black"
    )
    assert phone.name == "iPhone"
    assert phone.model == "15 Pro"
    assert phone.memory == 256
    assert phone.color == "Black"
def test_smartphone_str():
    """Тест строкового представления смартфона."""
    phone = Smartphone(
        name="iPhone",
        description="Смартфон",
        price=99999,
        quantity=5,
        performance="Высокая",
        model="15 Pro",
        memory=256,
        color="Black"
    )
    assert "iPhone" in str(phone)
    assert "15 Pro" in str(phone)
    assert "256" in str(phone)

def test_lawn_grass_creation():
    """Тест создания газонной травы."""
    grass = LawnGrass(
        name="Трава",
        description="Газонная трава",
        price=500,
        quantity=100,
        country="Россия",
        germination_period="14 дней",
        color="Зеленый"
    )
    assert grass.name == "Трава"
    assert grass.country == "Россия"
    assert grass.germination_period == "14 дней"
    assert grass.color == "Зеленый"

def test_category_add_smartphone():
    """Тест добавления смартфона в категорию."""
    cat = Category("Электроника", "Техника")
    phone = Smartphone(
        name="iPhone",
        description="Смартфон",
        price=99999,
        quantity=5,
        performance="Высокая",
        model="15 Pro",
        memory=256,
        color="Black"
    )
    cat.add_product(phone)
    assert cat.total_products == 1
    assert phone in cat.products
def test_category_add_lawn_grass():
    """Тест добавления газонной травы в категорию."""
    cat = Category("Сад", "Товары для сада")
    grass = LawnGrass(
        name="Трава",
        description="Газонная трава",
        price=500,
        quantity=100,
        country="Россия",
        germination_period="14 дней",
        color="Зеленый"
    )
    cat.add_product(grass)
    assert cat.total_products == 1
    assert grass in cat.products

def test_logging_mixin():
    """Тест миксина логирования."""
    from src.models import LoggingMixin
    class TestClass(LoggingMixin):
        pass
    
    obj = TestClass()
    # Проверяем что метод log существует
    assert hasattr(obj, 'log')
    assert callable(obj.log)
