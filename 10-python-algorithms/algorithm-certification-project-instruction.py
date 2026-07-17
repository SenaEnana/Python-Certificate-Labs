# Implement the Tower of Hanoi Algorithm
# In this lab, you will solve the mathematical puzzle known as the Tower of Hanoi. 
# The puzzle consists of three rods and a number of disks of different diameters.

# sequence of moves required to solve a 3-disks tower of Hanoi puzzle
# The puzzle starts with the disks piled up on the first rod, in decreasing size, with the smallest disk on top and the largest disk on the bottom.

# The goal of the Tower of Hanoi puzzle is moving all the disks to the last rod. To do that, you must follow three simple rules:

# You can move only top-most disks.
# You can move only one disk at a time.
# You cannot place larger disks on top of smaller ones.
# Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

# User Stories:

# You should have a function named hanoi_solver that takes an integer representing the total number of disks of the puzzle as the argument.
# The hanoi_solver function should solve the puzzle following the given rules in 2n - 1 moves, where n is the total number of disks.
# The hanoi_solver function should return a string with all the moves taken to solve the puzzle, including the starting arrangement, with each move on a new line. Rods should be represented as lists of integers, (the smallest disk is represented by the number 1) with each rod separated by a space. For example, hanoi_solver(3) should return the following:
# [3, 2, 1] [] []
# [3, 2] [] [1]
# [3] [2] [1]
# [3] [2, 1] []
# [] [2, 1] [3]
# [1] [2] [3]
# [1] [] [3, 2]
# [] [] [3, 2, 1]
