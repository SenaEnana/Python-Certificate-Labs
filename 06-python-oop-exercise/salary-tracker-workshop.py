class Employee:
    def __init__(self, name, level):
        self._name = name
        self._level = level

    def __str__(self):
        return f'{self.name}: {self.level}'

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level

charlie_brown = Employee('Charlie Brown', 'trainee')
print(charlie_brown)
print(charlie_brown.name)
print(charlie_brown.level)
