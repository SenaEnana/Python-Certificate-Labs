# Questions

# 1 What is the difference between a single underscore and a double underscore?

# A single underscore and a double underscore are treated the same way by Python.

# A single underscore makes attributes completely private, while a double underscore makes them protected.

# A single underscore prevents direct access, while a double underscore allows direct access.

# A single underscore is just a convention, while a double underscore triggers name mangling.////correct

# 2 What is name mangling?

# A process in which Python converts all attributes into methods for easier access.

# A process in which Python deletes attributes with a single underscore to keep them hidden.

# A process in which Python changes __attribute into _ClassName__attribute to avoid accidental overriding in subclasses.////correct

# A process in which Python encrypts private data to make it inaccessible from outside the class.

#3 What happens when you don't prefix attributes in a parent and child classes with a double underscore?

# Both classes keep their own separate copies of the attribute without interfering with each other.

# The child class completely overrides the parent class attribute, and the parent's data is lost.////correct

# The parent class attributes become read-only and cannot be changed by the child class.

# Python raises an error because attributes must always be prefixed with a double underscore.