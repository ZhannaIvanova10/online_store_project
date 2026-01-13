class Product:
    """
    Класс для представления товара в магазине.
    """

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """
    Класс для представления категории товаров.
    """

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)


def load_categories_from_json(file_path: str):
    """
    Загружает категории и товары из JSON-файла.

    Args:
        file_path (str): Путь к JSON-файлу

    Returns:
        list: Список объектов Category
    """
    import json

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories = []

    for category_data in data:
        products = []
        for product_data in category_data["products"]:
            product = Product(
                name=product_data["name"],
                description=product_data["description"],
                price=product_data["price"],
                quantity=product_data["quantity"],
            )
            products.append(product)

        category = Category(
            name=category_data["name"],
            description=category_data["description"],
            products=products,
        )
        categories.append(category)

    return categories
