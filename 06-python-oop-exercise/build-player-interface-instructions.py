# Build a Player Interface

# Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.
# User Stories:
# You should define an abstract class named Player that inherits from the abc.ABC class.
# The Player class should have an __init__ method that sets:
# The moves attribute to an empty list.
# The position attribute to (0, 0).
# The path attribute to a list containing the initial position.
# The Player class should have a method named make_move that:
# Uses random.choice to get a random move from the moves attribute (defined in the concrete class).
# Adds the values from the selected move to the current position and updates the position attribute.
# Appends the new position tuple to the path attribute.
# Returns the new position.
# The Player class should have an abstract method named level_up to be implemented in concrete classes.
# You should define a Pawn class that inherits from the Player class.
# The Pawn class should use super() to call the parent's __init__ method and then set the moves attribute to a list of tuples representing x, y coordinates.

# Each coordinate tuple should represent a movement of 1 unit in the following directions: up, down, left, right.
# The Pawn class should implement a concrete level_up method by adding more moves to the moves attribute. The added moves should represent the four diagonal movements (for example, 1 unit down plus 1 unit left).
# Note: Standard library modules should be imported without using aliases. Tests related to the Player class will fail until the Pawn class becomes instantiable.

# Tests:
# Passed:1. You should have a class named Player.
# Passed:2. The Player class should inherit from the ABC class of the abc module.
# Passed:3. The Player class should have an __init__ method.
# Passed:4. The Player's __init__ method should have a single parameter self.
# Passed:5. The Player's __init__ method should set self.moves to an empty list.
# Passed:6. The Player's __init__ method should set self.position to (0, 0).
# Passed:7. The Player's __init__ method should set self.path to a list containing the initial position.
# Passed:8. The Player class should have a make_move method.
# Passed:9. The Player's make_move method should have a single parameter self.
# Passed:10. The Player's make_move method should use random.choice to get a random move from the moves attribute.
# Passed:11. The Player's make_move method should update the position attribute by adding to it the coordinates of the randomly selected move.
# Passed:12. The Player's make_move method should append the new position tuple to the path attribute.
# Passed:13. The Player's make_move method should return the updated position attribute.
# Passed:14. The Player class should have a level_up method.
# Passed:15. The Player's level_up method should have a single parameter self.
# Passed:16. The Player's level_up method should be an abstract method.
# Passed:17. The Player class should be an abstract class.
# Passed:18. You should have a class named Pawn.
# Passed:19. The Pawn class should inherit from the Player class.
# Passed:20. The Pawn class should have an __init__ method.
# Passed:21. The Pawn's __init__ method should have a single parameter self.
# Passed:22. The Pawn's __init__ method should call the parent's __init__ with using the super function.
# Passed:23. The Pawn's __init__ method should set the moves attribute to a list of tuples representing x, y coordinates, where each coordinate tuple represents a movement of 1 unit in the following directions: up, down, left, right.
# Passed:24. The Pawn class should have a level_up method.
# Passed:25. The Pawn's level_up method should add the four diagonal movement of 1 unit to the moves attribute.