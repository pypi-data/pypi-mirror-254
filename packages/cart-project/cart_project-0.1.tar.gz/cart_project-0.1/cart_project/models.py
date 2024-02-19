# Item
# Cart
class Item:
    """
    Товари для роботи магазину

    :param name: Назва товару
    :param description: str
    :param price: Ціна товару
    :type name: str
    :type description: Опис товару
    :type price: float
    """
    def __init__(self,
                 description:str,
                 name: str,
                 price:float):
        self.name = name
        self.description = description
        self.price = price

    def show(self):
        """
        Метод відображення інформації про товар
        """
        print(f"""Назва товару: {self.name}
Опис товару: {self.description}
Ціна товару: {self.price}""")

class Cart:
    """
    Корзина для магазину

    :param items: Товари у корзині
    :type items: list
    """
    def __init__(self):
        self.items = []
    def get_count(self):
        """
        Метод вираховує кількість товарів у корзині
        :return: Повертаємо кількість товарів
        :rtype: int
        """
        return len(self.items)
    def get_price(self):
        """
        Метод вираховує загальну ціну товарів у корзині

        :return: Повертаємо ціну товарів
        :rtype: int|float
        """
        price = 0
        for item in self.items:
            price +=item.price     