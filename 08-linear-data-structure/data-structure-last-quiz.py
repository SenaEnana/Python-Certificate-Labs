# Data Structures Quiz
# To pass the quiz, you must correctly answer at least 18 of the 20 questions below.

# 1.What does Big O notation describe in algorithm analysis?

# The exact runtime in seconds for a specific computer.
# How the time or space grows relative to input size (an upper bound).
# The percentage of code lines executed during a run.
# How readable the code is to other developers.

# 2.When starting an algorithmic challenge, what is the best first step?

# Write unit tests only after finishing the solution.
# Begin coding immediately to gain momentum.
# Optimize for performance before you understand the problem.
# Clarify the problem and constraints with examples and edge cases.

# 3.What is the key difference between dynamic arrays and static arrays?

# Static arrays allow duplicate values; dynamic arrays do not.
# Dynamic arrays store values of different types; static arrays cannot.
# Dynamic arrays can grow or shrink by resizing; static arrays have a fixed size.
# Dynamic arrays are faster than static arrays for every operation.

# 4.What is the amortized time complexity of appending an element to the end of a dynamic array?

# O(n log n)
# O(log n)
# O(n)
# O(1) amortized.

# 5.Why does accessing the k-th element by index in a singly linked list take O(n) time?

# The index is hashed and looked up in a table.
# Nodes are stored contiguously, so shifting is required.
# You must traverse from the head node to the k-th node one by one.
# The list must be resized before any access.

# 6.Which feature does a doubly linked list have that a singly linked list does not?

# Random access to any index in O(1) time.
# A built-in array buffer for faster iteration.
# Automatic maintenance of the list length as a constant.
# Pointers to both next and previous nodes enabling backward traversal.

# 7.Which of the following best describes a stack?

# A circular buffer with constant-time random access.
# Last In, First Out (LIFO) with push and pop at the top.
# First In, First Out (FIFO) with removals at the front.
# A structure where any element can be removed in O(1) time.

# 8.Which operation removes the element at the front of a queue?

# dequeue
# push
# pop
# peek

# 9.What is the typical average-case time complexity to look up a value by key in a hash map?

# O(log n) due to binary search within buckets.
# O(n log n) because keys are sorted during insertion.
# O(1) on average with a good hash function and low load factor.
# O(n) because all keys must be scanned sequentially.

# 10.Which guarantee is provided by a set data structure?

# Elements are stored in sorted order by default.
# It stores only unique elements (no duplicates).
# Duplicate values are allowed and kept together.
# Elements are indexed by their insertion position.

# 11.In a dynamic array, what is the worst-case time complexity of inserting an element at index i (not at the end)?

# O(1)
# O(log n)
# O(n)
# O(1) amortized

# 12.What is the time complexity of inserting a new node at the head of a singly linked list?

# O(log n)
# O(1)
# O(n)
# O(n log n)

# 13.Which operation is used to remove an element from a stack?

# dequeue
# pop
# push
# Insert at bottom.

# 14.Which of the following best describes a queue?

# Random access to any index in O(1) time.
# Last In, First Out (LIFO) with removals at the top.
# First In, First Out (FIFO) with enqueue at the back and dequeue at the front.
# Elements are always kept in sorted order automatically.

# 15.What is a hash collision in a hash map?

# When two different keys produce the same hash index.
# When the map runs out of memory and must be resized.
# When a key maps to multiple distinct values by design.
# When two identical keys are stored in different buckets.

# 16.Why do hash maps resize (rehash) as they grow?

# To sort keys in ascending order for faster iteration.
# To keep the load factor low so that average operations remain O(1).
# To avoid triggering the language's garbage collector.
# To compress values and reduce memory fragmentation.

# 17.Which statement about sets is true?

# Sets preserve insertion order by definition.
# Membership tests are typically O(1) on average.
# Set membership tests are O(n log n) on average.
# Sets allow duplicate elements and keep counts.

# 18.Which time complexity grows faster than O(n log n) as n becomes large?

# O(n^2)
# O(log n)
# O(1)
# O(n)

# 19.After implementing a brute-force solution, what is a good next step?

# Discard tests and rewrite the solution from scratch.
# Analyze its time/space complexity and optimize identified bottlenecks.
# Micro-optimize constant factors before measuring.
# Avoid considering edge cases to keep the code simple.

# 20.What does space complexity measure?

# How memory usage grows relative to input size.
# How many CPU cores a program uses.
# The length of a program in lines of code.
# How long a program takes to compile.



# ///////////////////////////////////////////////////
# Here are the correct answers for Data Structures Quiz:

#1 Answer: How the time or space grows relative to input size (an upper bound).

#2 Answer: Clarify the problem and constraints with examples and edge cases.

#3 Answer: Dynamic arrays can grow or shrink by resizing; static arrays have a fixed size.

#4 Answer: O(1) amortized.

#5 Answer: You must traverse from the head node to the k-th node one by one.

#6 Answer: Pointers to both next and previous nodes enabling backward traversal.

#7 Answer: Last In, First Out (LIFO) with push and pop at the top.

#8 Answer: dequeue

# What is the typical average-case time complexity to look up a value by key in a hash map?

#9 Answer: O(1) on average with a good hash function and low load factor.

# Which guarantee is provided by a set data structure?

#10 Answer: It stores only unique elements (no duplicates).

# In a dynamic array, what is the worst-case time complexity of inserting an element at index i (not at the end)?

#11 Answer: O(n)

# What is the time complexity of inserting a new node at the head of a singly linked list?

#12 Answer: O(1)

# Which operation is used to remove an element from a stack?

#13 Answer: pop

# Which of the following best describes a queue?

#14 Answer: First In, First Out (FIFO) with enqueue at the back and dequeue at the front.

# What is a hash collision in a hash map?

#15 Answer: When two different keys produce the same hash index.

# Why do hash maps resize (rehash) as they grow?

#16 Answer: To keep the load factor low so that average operations remain O(1).

# Which statement about sets is true?

#17 Answer: Membership tests are typically O(1) on average.

# Which time complexity grows faster than O(n log n) as n becomes large?

#18 Answer: O(n^2)

# After implementing a brute-force solution, what is a good next step?

#19 Answer: Analyze its time/space complexity and optimize identified bottlenecks.

# What does space complexity measure?

#20 Answer: How memory usage grows relative to input size.