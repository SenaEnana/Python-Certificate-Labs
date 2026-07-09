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


        # Append the new position to the path tracking list
        self.path.append(self.position)

        return self.position
    
    @abc.abstractmethod
    def level_up(self) -> None:
        pass

class Pawn(Player):
    """A concrete implementation of Player representing a Pawn."""

    def __init__(self) -> None:
        super().__init__()
        self.moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def level_up(self) -> None:
        diagonal_moves = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        self.moves.extend(diagonal_moves)