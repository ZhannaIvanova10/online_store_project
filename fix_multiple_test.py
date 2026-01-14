import os

filepath = 'tests/test_magic_methods.py'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Найдем и заменим проблемный тест полностью
old_test = '''def test_product_add_multiple():
    """Тест сложения нескольких товаров."""
    products = [
        Product(f"Товар {i}", "Описание", 100 * i, i)
        for i in range(1, 6)  # 5 товаров
    ]
    
    # Суммируем вручную
    manual_sum = sum(p.price * p.quantity for p in products)
    
    # Для нескольких товаров нужно суммировать попарно
    # product1 + product2 дает число, затем число + product3 не работает
    # Вместо этого используем другой подход:
    total = 0
    for i in range(len(products) - 1):
        for j in range(i + 1, len(products)):
            # Суммируем все попарные суммы
            total += products[i] + products[j]
    # Это не то же самое, что сумма всех произведений
    # Для теста просто проверяем что попарное сложение работает
    # Основная проверка в test_product_add
    assert True'''

new_test = '''def test_product_add_multiple():
    """Тест сложения нескольких товаров."""
    products = [
        Product(f"Товар {i}", "Описание", 100 * i, i)
        for i in range(1, 6)  # 5 товаров
    ]
    
    # Суммируем вручную
    manual_sum = sum(p.price * p.quantity for p in products)
    
    # Правильный способ сложения нескольких товаров:
    # Нужно явно получать стоимость каждого продукта и складывать их
    total = 0
    for product in products:
        # Получаем стоимость каждого товара через его __add__ метод с 0
        total += product.price * product.quantity
    
    # Проверяем, что сумма равна ручной
    assert total == manual_sum, f"Ожидалось {manual_sum}, получено {total}"
    # Дополнительная проверка: попарное сложение работает корректно
    # Складываем первые два товара
    sum_first_two = products[0] + products[1]
    expected_sum = products[0].price * products[0].quantity + products[1].price * products[1].quantity
    assert sum_first_two == expected_sum, f"Попарное сложение не работает: ожидалось {expected_sum}, получено {sum_first_two}"'''

content = content.replace(old_test, new_test)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ test_product_add_multiple исправлен")
