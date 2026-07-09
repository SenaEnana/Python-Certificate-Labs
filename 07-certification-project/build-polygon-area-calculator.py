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





















# Congratulations. Your code passes.
# Build a Polygon Area Calculator
# Completed

