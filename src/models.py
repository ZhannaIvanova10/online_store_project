"""
Модуль для работы с товарами и категориями интернет-магазина.
Включает обработку исключений для работы с нулевым количеством товаров.
"""


class ZeroQuantityError(ValueError):
    """Пользовательское исключение для товаров с нулевым количеством."""
    
    def __init__(self, message="Товар с нулевым количеством не может быть добавлен"):
        super().__init__(message)


class Product:
    """Класс для представления товара в магазине."""
    
    def __init__(self, name: str, price: float, quantity: int):
        """
        Инициализация товара.
        
        Args:
            name: Название товара
            price: Цена товара
            quantity: Количество товара
        Raises:
            ZeroQuantityError: Если quantity равен 0
        """
        if quantity == 0:
            raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен")
        
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Category:
    """Класс для представления категории товаров."""
    
    def __init__(self, name: str):
        self.name = name
        self.products = []
    
    def add_product(self, product: Product):
        """
        Добавляет товар в категорию.
        
        Args:
            product: Объект класса Product для добавления
            
        Raises:
            ZeroQuantityError: Если у товара quantity равен 0
        """
        try:
            if product.quantity == 0:
                raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен")
            
            self.products.append(product)
            
        except ZeroQuantityError as e:
            print(f"Ошибка при добавлении товара: {e}")
            raise
        else:
            print(f"Товар '{product.name}' успешно добавлен в категорию '{self.name}'")
        finally:
            print(f"Обработка добавления товара '{product.name}' завершена")
    
    def calculate_average_price(self) -> float:
        """
        Рассчитывает средний ценник всех товаров в категории.
        
        Returns:
            Средняя цена товаров в категории или 0, если в категории нет товаров
        """
        if not self.products:
            return 0.0
        
        try:
            total_price = sum(product.price for product in self.products)
            average = total_price / len(self.products)
            return average
        except ZeroDivisionError:
            return 0.0
    def __str__(self):
        products_info = "\n".join(str(product) for product in self.products)
        return f"Категория: {self.name}\nТовары:\n{products_info}"
