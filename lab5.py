# Написати програму алгоритмічною мовою Python згідно з завданням,
# отриманим від викладача за табл. 1. Додайте відповідні конструктори,
# деструктори, функції доступу та виведення інформації на екран.
# У методі main продемонструйте роботу класів.

# Створити клас Flower (height, size, color, price, quantity, deliveryRate)
# та клас FlowerShop, що містить в асортименті набір квітів. Створіть клас
# Bouquet, у який можна додавати будь-яку кількість квітів та дозвольте
# підрахувати його вартість. Реалізуйте методи виведення топу найдорожчих
# квітів в магазині та додавання, видалення з магазину.


class Flower:
    def __init__(self, height, size, color, price, quantity, delivery_rate):
        self.height = height
        self.size = size
        self.color = color
        self.price = price
        self.quantity = quantity
        self.delivery_rate = delivery_rate

    @staticmethod
    def _non_negative(value):
        if value < 0:
            raise ValueError(f"Must be non-negative, got {value}")
        return value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = self._non_negative(value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = self._non_negative(value)

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = self._non_negative(value)

    @property
    def delivery_rate(self):
        return self._delivery_rate

    @delivery_rate.setter
    def delivery_rate(self, value):
        self._delivery_rate = self._non_negative(value)

    def __str__(self):
        return (f"{self.color} flower, {self.size} size, {self.height} cm. "
                f"In stock: {self.quantity}. "
                f"Price: ${self.price} + ${self.delivery_rate} delivery")

    def __repr__(self):
        return (f"Flower(height={self.height}, size={self.size!r}, "
                f"color={self.color!r}, price={self.price}, "
                f"quantity={self.quantity}, "
                f"delivery_rate={self.delivery_rate})")

    def __del__(self):
        print("Flower destructed.")


class FlowerShop:
    distributor = "Some flowers distributor"

    def __init__(self, flowers=None):
        self._flowers = list(flowers) if flowers else []
        FlowerShop.distributor = "Another flowers distributor"

    @classmethod
    def get_distributor(cls):
        return cls.distributor

    @property
    def flowers(self):
        return list(self._flowers)

    def __str__(self):
        body = "\n".join(f"  - {f}" for f in self._flowers) or "  (empty)"
        return f"Flower shop assortment:\n{body}"

    def add_flower(self, flower):
        if not isinstance(flower, Flower):
            raise TypeError("Only Flower instances can be added")
        self._flowers.append(flower)

    def remove_flower(self, flower):
        self._flowers.remove(flower)

    def get_top_expensive(self, n=3):
        if n < 1:
            raise ValueError("n must be >= 1")
        return sorted(self._flowers, key=lambda f: f.price, reverse=True)[:n]

    def print_top_expensive(self, n=3):
        print(f"Top {n} most expensive flowers:")
        for flower in self.get_top_expensive(n):
            print(flower)

    def __del__(self):
        print("Flower shop destructed")


class Bouquet:
    def __init__(self, flowers=None):
        self._flowers = list(flowers) if flowers else []

    def add_flower(self, flower):
        if not isinstance(flower, Flower):
            raise TypeError("Only Flower instances can be added")
        self._flowers.append(flower)

    def get_net_price(self):
        return sum(f.price for f in self._flowers)

    def get_full_price(self):
        return sum(f.price + f.delivery_rate for f in self._flowers)

    def __str__(self):
        body = "\n".join(f"  - {f}" for f in self._flowers) or "  (empty)"
        return f"Bouquet:\n{body}"

    def __del__(self):
        print("Bouquet destructed")


def main():
    rose = Flower(30, "medium", "red", 3, 10, 1)
    peony = Flower(20, "large", "pink", 12, 5, 2)
    lily = Flower(45, "medium", "white", 8, 6, 2)
    shop = FlowerShop([rose, peony, lily])

    tulip = Flower(60, "small", "yellow", 7, 4, 1)
    shop.add_flower(tulip)
    print(shop)

    print()
    shop.print_top_expensive(3)

    print()
    bouquet = Bouquet([rose, peony])
    bouquet.add_flower(lily)
    bouquet.add_flower(rose)
    print(bouquet)
    print(f"Net price: ${bouquet.get_net_price()}")
    print(f"Total with delivery: ${bouquet.get_full_price()}")

    print()
    shop.remove_flower(tulip)
    print("After removing the tulip:")
    print(shop)

    print()
    try:
        Flower(-5, "small", "red", 3, 1, 1)
    except ValueError as e:
        print(f"Rejected: {e}")

    print()
    temp = Flower(10, "small", "blue", 1, 1, 0)
    del temp


if __name__ == "__main__":
    main()
