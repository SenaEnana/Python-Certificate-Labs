import abc
import random

class Player(abc.ABC):
    """An abstract class representing a game player."""

    def __init__(self) -> None:
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]