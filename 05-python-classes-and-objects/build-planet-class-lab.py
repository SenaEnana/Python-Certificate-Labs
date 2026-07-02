#1 You should create a class named Planet.
class Planet:
    def __init__(self, name, planet_type, star):
        # 1. Type validation (Raise TypeError if any argument is not a string)
        if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
            raise TypeError("name, planet type, and star must be strings")
        
        # 2. Value validation (Raise ValueError if any string is empty)
        # Note: We strip whitespace just in case, but an empty check like == "" or not value works.
        if name == "" or planet_type == "" or star == "":
            raise ValueError("name, planet_type, and star must be non-empty strings")