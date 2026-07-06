class Employee:
    def __init__(self, name, level):
        if not isinstance(name, str) or not isinstance(level, str):
            raise TypeError("'name' and 'level' attribute must be of type 'str'.")        
        self._name = name
        self._level = level
        
    def __str__(self):
        return f'{self.name}: {self.level}'

    def __repr__(self):
        return f"Employee('{self.name}', '{self.level}')"

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level

charlie_brown = Employee('Charlie Brown', 'trainee')
print(charlie_brown)
