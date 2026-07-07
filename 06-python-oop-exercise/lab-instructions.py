# Build a Game Character Stats Tracker
# In this lab, you'll build a game character stats tracker. The program will allow you to create a character with specific attributes, update those attributes, and retrieve the current stats of the character.

# Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

# User Stories:

# Create a class named GameCharacter that represents a game character and manages character stats.

# When instantiated, a new GameCharacter object should have the following attributes:

# _name set to the string given at the moment of the instantiation.
# _health set to 100.
# _mana set to 50.
# _level set to 1.
# Create a name property for read-only access to the character's name.

# For the health property:

# Define a getter that returns the current health.
# Define a setter that prevents health from being set below 0, and caps the health at 100.
# For the mana property:

# Define a getter that returns the current mana.
# Define a setter that prevents mana from being set below 0, and caps the mana at 50.
# Create a getter for level to return the character's current level.

# Define a method named level_up that:

# Increases the character's level by 1.
# Resets health to 100 and mana to 50 using their corresponding property setters.
# Prints a message in the form of <name> leveled up to <level>! (where <name> and <level> should be replaced by the character's name and new level, respectively).
# Define a __str__ method that returns a formatted string including:

# The character's name.
# The character's level.
# The character's current health.
# The character's current mana.
# For example, a character named Kratos, right after the instantiation, should be represented as the following:

# Name: Kratos
# Level: 1
# Health: 100
# Mana: 50
# Usage example
# hero = GameCharacter('Kratos') # Creates a new character named Kratos
# print(hero)  # Displays the character's stats

# hero.health -= 30  # Decreases health by 30
# hero.mana -= 10    # Decreases mana by 10
# print(hero)  # Displays the updated stats

# hero.level_up()  # Levels up the character
# print(hero)  # Displays the stats after leveling up
# Tests:
# Waiting:1. You should have a GameCharacter class.
# Waiting:2. You should have an __init__ method in the GameCharacter class.
# Waiting:3. The __init__ method should have two parameters, with the first being self.
# Waiting:4. You should set self._name to the string given at the moment of instantiation inside the __init__ method.
# Waiting:5. You should assign 100 to self._health inside the __init__ method.
# Waiting:6. You should assign 50 to self._mana inside the __init__ method.
# Waiting:7. You should assign 1 to self._level inside the __init__ method.
# Waiting:8. You should have a name method in the GameCharacter class.
# Waiting:9. The name method should have only one parameter, self.
# Waiting:10. You should return self._name in the name method.
# Waiting:11. The name method should have a @property decorator.
# Waiting:12. You should have a health method in the GameCharacter class.
# Waiting:13. The health method should have only one parameter, self.
# Waiting:14. You should return self._health in the health method.
# Waiting:15. The health method should have a @property decorator.
# Waiting:16. You should create a health setter method.
# Waiting:17. The health setter method should have a @health.setter decorator.
# Waiting:18. The health setter method should have two parameters, with the first being self.
# Waiting:19. You should set self._health to 0 if the value given to the health setter is less than 0.
# Waiting:20. You should set self._health to 100 if the value given to the health setter is greater than 100.
# Waiting:21. You should set self._health to the value given to the health setter when the value is between 0 and 100.
# Waiting:22. You should have a mana method in the GameCharacter class.
# Waiting:23. The mana method should have only one parameter, self.
# Waiting:24. You should return self._mana in the mana method.
# Waiting:25. The mana method should have a @property decorator.
# Waiting:26. You should create a mana setter method.
# Waiting:27. The mana setter method should have a @mana.setter decorator.
# Waiting:28. The mana setter method should have two parameters, with the first being self.
# Waiting:29. You should set self._mana to 0 if the value given to the mana setter is less than 0.
# Waiting:30. You should set self._mana to 50 if the value given to the mana setter is greater than 50.
# Waiting:31. You should set self._mana to the value given to the mana setter if the value is between 0 and 50.
# Waiting:32. You should have a level method in the GameCharacter class.
# Waiting:33. The level method should have only one parameter, self.
# Waiting:34. You should return self._level in the level method.
# Waiting:35. The level method should have a @property decorator.
# Waiting:36. You should have a level_up method in the GameCharacter class.
# Waiting:37. The level_up method should have only one parameter, self.
# Waiting:38. You should increase self._level by 1 in the level_up method.
# Waiting:39. You should set self.health to 100 in the level_up method.
# Waiting:40. You should set self.mana to 50 in the level_up method.
# Waiting:41. The level_up method should print <name> leveled up to <level>! (where <name> and <level> should be replaced by the character's name and new level, respectively).
# Waiting:42. You should have a __str__ method in the GameCharacter class.
# Waiting:43. The __str__ method should have only one parameter, self.
# Waiting:44. Your __str__ method should return a string with the character's stats using the provided format.