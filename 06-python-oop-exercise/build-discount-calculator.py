from abc import ABC, abstractmethod

class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'{self.name} - ${self.price}'

class DiscountStrategy(ABC):
    @abstractmethod
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        pass

    @abstractmethod
    def apply_discount(self, product: Product) -> float:
        pass

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: int) -> None:
        self.percent = percent
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        if self.percent <= 70:
            return True
        else:
            return False    
product = Product('Wireless Mouse', 50.0)
print(product)