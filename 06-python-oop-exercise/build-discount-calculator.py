class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price
    def __str__(self) -> str:
        return f'{self.name} - ${self.price}'