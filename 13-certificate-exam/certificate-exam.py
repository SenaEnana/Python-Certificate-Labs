# 1 Which of the following are immutable data types in Python?

# float, int, list

# dict, set, tuple

# float, str, set

# int, str, tuple" 

# 2 What is the result of running print('2025/07/' + 25)?

# ConcatenationError

# TypeError

# 20250725

# 2025/07/25

# 3 string = 'freeCodeCamp'print(string[::-1])

# What is the value of string after running the code above?

# freeCodeCamp

# reeCodeCamp

# pmaCedoCeerf

# freeCodeCam 

# 4 Which of the following is NOT a valid variable name?

# valid-name

# _valid_name

# valid_name2

# ValidName

# 5 Context

# my_list = [3.99, '42', True]

# my_new_list = [int(i) for i in my_list]print(my_new_list)

# What is the result of running the code above?

# [3.99, 42, True]

# TypeError

# [3, 42, 1]

# [4, 42, 1] 

# 6 Which of the following is true about dictionary keys?

# They must be strings.

# They must be unique and immutable.

# They cannot be boolean values.

# They must be inserted in alphabetical order.

# 7 What is the basic syntax for importing a module in Python?

# import module_name

# include module_name

# require module_name

# load module_name

# 8 How do you import specific functions from a module?

# from module_name import function_name

# from module_name require function_name

# import function_name from module_name

# require function_name from module_name

# 9 What happens when you try to modify a character in a string directly?

# Nothing, the string remains unchanged because strings are immutable.

# You get a TypeError because strings are immutable.

# The modification succeeds.

# A new string is created and replaces the old string. 

# 10 Which of the following equals list(range(35, 15, -5))?

# [35, 30, 25, 20]

# [15, 20, 25, 30]

# [35, 30, 25, 20, 15]

# [20, 25, 30, 35]

# 11 Do dictionaries preserve the order of insertion?

# Only sometimes.

# Only if specified when creating the dictionary.

# Only in recent Python versions.

# No, never.

# 12 Context

# try:

# number = int(x)

# result = 10 / numberexcept ValueError:

# print('Invalid number.')except ZeroDivisionError:

# print("Can't divide by zero.")else:

# print('Success.')finally:

# print('Done.')

# What is the result of running the code above if x = False?

# Can't divide by zero.

# Success.

# Done.

# Can't divide by zero.

# Done.

# Invalid number.

# Done. 

# 12 What is the difference between a class and an object?

# Classes store data, objects define behavior.

# A class is the template or blueprint, and an object is what is created using that template.

# An object is a template or blueprint, and a class is an instance created using that template.

# There is no difference. 

# 13 What is the default value returned by a function?

# Null

# False

# None

# An empty string

# 14 programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')

# i = programming_languages.index('Python', 3)

# What is the value of i?

# (3, 6, 8)

# 6

# 3

# 5 
 
# 15 What is the result of evaluating set('lane') == set('anneal')?

# False

# SyntaxError

# True

# TypeError

# 16 What is the result of the division between two integers?

# An integer

# A float

# A complex number

# A boolean

# 17 Which of the following is a key characteristic of an algorithm?

# It must always use recursion.

# It guarantees the fastest possible solution to a problem.

# It is always written in a programming language.

# It cannot continue indefinitely.

# 18 Which of the following is the correct Big O notation for an algorithm that takes 20n² + 15n + 7 operations to be completed?

# O(20n²)

# O(n²)

# O(20n² + 15n)

# O(n² + n) 

# 19 Which of the following is a key characteristic of a stack?

# It stores elements in contiguous memory locations like an array.

# Elements can only be added or removed from the top of the stack.

# It allows for simultaneous access and modification of its elements.

# It follows the First-In, First-Out (FIFO) principle, where the first element added is the first to be removed. 

# 20 Which of the following best describes the Binary Search algorithm?

# It is a search algorithm that works on sorted data and reduces the search space by half with each comparison.

# It sorts the array after each comparison to locate the target.

# It is a search algorithm that checks each element sequentially from the beginning until it finds the target.

# It is a sorting method that splits the array recursively and merges the elements in order. 

# 21 What is the primary benefit of using dynamic programming over naive recursive approaches?

# It works faster on all types of problems.

# It always produces more accurate results than recursion.

# It eliminates redundant calculations by storing and reusing subproblem solutions.

# It can solve problems that recursion cannot solve. 

# 22 What type of problems benefit most from dynamic programming optimization?

# Problems with overlapping subproblems and optimal substructure.

# Problems that can only be solved iteratively.

# Problems that involve network communication.

# Problems that require sorting large datasets. 

# 23 What is the main difference between single underscore and double underscore prefixed attributes in Python?

# Single underscore makes attributes faster to access than double underscore.

# Single underscore is for methods only, double underscore is for attributes only.

# Single underscore is a convention for internal use, while double underscore triggers name mangling.

# There's no difference, both prevent direct access from outside the class equally. 

# 24 What decorator is used to create a getter in Python?

# @attribute

# @property

# @getter

# @get

# 25 What happens if you try to instantiate an abstract class or a concrete class that doesn't implement all abstract methods?

# Python raises a TypeError preventing instantiation.

# The abstract methods are automatically implemented with default behavior.

# The instance is created but the abstract methods return None.

# A warning is displayed but the instance is still created. 

# 26 Context

# class Person:

# def __init__(self, name):

# self._name = name

# Which of the following is the correct way to define a setter for the _name attribute?

# def name(self, new_name):

# self.name = new_name

# @name.setter

# def name(self, new_name):

# self.name = new_name

# @property

# def name(self, new_name):

# self.name = new_name

# @name.setter

# def name(self, new_name):

# self._name = new_name 

# 27 Context

# Which of the following best describes inheritance-based polymorphism in object-oriented programming?

# It allows a class to merge the attributes and behaviors of several unrelated parent classes into one.

# It makes subclasses automatically inherit and use all parent methods exactly as they were defined.

# It allows subclasses to provide different implementations of methods defined in a parent class.

# It requires every subclass to fully replicate the structure and behavior of its parent class. 

# 28 What is the key requirement for binary search to work properly?

# The list must be stored in a specific data structure.

# The list must be sorted in ascending order.

# The list must contain unique elements only.

# The list must contain only positive numbers

# 29 In the divide and conquer approach used by merge sort, what is the base case?

# When the recursion depth reaches a maximum.

# When the list has exactly two elements.

# When the list has one element or is empty.

# When the list is already sorted. 

# 30 If an algorithm has time complexity O(n³), what does that mean?

# Its running time increases linearly with input size.

# Its running time grows proportionally to the cube of the input size.

# Its running time is constant, regardless of input size.

# Its running time roughly triples for every extra input element.

31

#you can upload and view the exam questions if you are curious also with this am waiting for my certification for the result! thank you!