class Rectangle:
    """A class representing a rectangle shape."""

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
    def set_width(self, width: int) -> None:
        self.width = width
    def set_height(self, height: int) -> None:
        self.height = height
    def get_area(self) -> int:
        return self.width * self.height
    def get_perimeter(self) -> int:
        return 2 * (self.width + self.height)
    def get_diagonal(self) -> float:
        # Calculates diagonal using the Pythagorean theorem: (width² + height²)**0.5
        return (self.width**2 + self.height**2) ** 0.5
    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        # Creates a row of '*' with a newline, repeated 'height' times
        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, shape: "Rectangle") -> int:
        # Calculates how many times the passed shape fits completely (no rotation)
        cols_fit = self.width // shape.width
        rows_fit = self.height // shape.height
        return cols_fit * rows_fit

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    """A class representing a square shape, inheriting from Rectangle."""

    def __init__(self, side: int) -> None:
        # A square has equal width and height initialized by its side length
        super().__init__(side, side)

















# Congratulations. Your code passes.
# Build a Polygon Area Calculator
# Completed

