import abc
import random


class Player(abc.ABC):
    """An abstract class representing a game player."""

    def __init__(self) -> None:
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        # Select a random move from the available moves
        selected_move = random.choice(self.moves)

        # Update the position by adding the selected move coordinates
        new_x = self.position[0] + selected_move[0]
        new_y = self.position[1] + selected_move[1]
        self.position = (new_x, new_y)