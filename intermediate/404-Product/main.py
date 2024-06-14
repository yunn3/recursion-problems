class Product:

    def __init__(self, title: str, price: float) -> None:
        self.title = title
        self.price = price


product1 = Product("shampoo", 10)
product2 = Product("conditioner", 5)

print(product1.title)
print(product1.price)
print(product2.title)
print(product2.price)
