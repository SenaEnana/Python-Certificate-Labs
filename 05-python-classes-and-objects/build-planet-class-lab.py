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
        # 3. The Planet class should have an orbit method that returns a string in the format {name} is orbiting around {star}....
        self.name = name
        self.planet_type = planet_type
        self.star = star

# 4. The Planet class should have a __str__ method that returns a string in the format Planet: {name} | Type: {planet_type} | Star: {star}.

    def orbit(self) -> str:
        # Returns string in the exact format required
        return f"{self.name} is orbiting around {self.star}..."

    def __str__(self) -> str:
        # Returns the string representation of the object
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"


# --- Instance Creation and Testing ---
# 5. You should create three instances of the Planet class named planet_1, planet_2, and planet_3.
# 6. You should print each planet object to see the __str__ method output.
# 7. You should call the orbit method on each planet object and print the result.

# Creating three instances of the Planet class
planet_1 = Planet("Earth", "Terrestrial", "The Sun")
planet_2 = Planet("Jupiter", "Gas Giant", "The Sun")
planet_3 = Planet("Kepler-186f", "Super-Earth", "Kepler-186")

# Printing each planet object to see the __str__ method output
print(planet_1)
print(planet_2)
print(planet_3)

print("-" * 40) # Visual separator

# Calling the orbit method on each planet object and printing the result
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())