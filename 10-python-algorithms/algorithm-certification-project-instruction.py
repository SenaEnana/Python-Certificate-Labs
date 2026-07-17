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
# Tests:
# Waiting:1. You should have a function named hanoi_solver.
# Waiting:2. Your hanoi_solver function should take a single argument.
# Waiting:3. Your hanoi_solver function should return a string.
# Waiting:4. hanoi_solver(2) should return [2, 1] [] []\n[2] [1] []\n[] [1] [2]\n[] [] [2, 1].
# Waiting:5. hanoi_solver(3) should return [3, 2, 1] [] []\n[3, 2] [] [1]\n[3] [2] [1]\n[3] [2, 1] []\n[] [2, 1] [3]\n[1] [2] [3]\n[1] [] [3, 2]\n[] [] [3, 2, 1].
# Waiting:6. hanoi_solver(4) should return [4, 3, 2, 1] [] []\n[4, 3, 2] [1] []\n[4, 3] [1] [2]\n[4, 3] [] [2, 1]\n[4] [3] [2, 1]\n[4, 1] [3] [2]\n[4, 1] [3, 2] []\n[4] [3, 2, 1] []\n[] [3, 2, 1] [4]\n[] [3, 2] [4, 1]\n[2] [3] [4, 1]\n[2, 1] [3] [4]\n[2, 1] [] [4, 3]\n[2] [1] [4, 3]\n[] [1] [4, 3, 2]\n[] [] [4, 3, 2, 1].
# Waiting:7. hanoi_solver(5) should return [5, 4, 3, 2, 1] [] []\n[5, 4, 3, 2] [] [1]\n[5, 4, 3] [2] [1]\n[5, 4, 3] [2, 1] []\n[5, 4] [2, 1] [3]\n[5, 4, 1] [2] [3]\n[5, 4, 1] [] [3, 2]\n[5, 4] [] [3, 2, 1]\n[5] [4] [3, 2, 1]\n[5] [4, 1] [3, 2]\n[5, 2] [4, 1] [3]\n[5, 2, 1] [4] [3]\n[5, 2, 1] [4, 3] []\n[5, 2] [4, 3] [1]\n[5] [4, 3, 2] [1]\n[5] [4, 3, 2, 1] []\n[] [4, 3, 2, 1] [5]\n[1] [4, 3, 2] [5]\n[1] [4, 3] [5, 2]\n[] [4, 3] [5, 2, 1]\n[3] [4] [5, 2, 1]\n[3] [4, 1] [5, 2]\n[3, 2] [4, 1] [5]\n[3, 2, 1] [4] [5]\n[3, 2, 1] [] [5, 4]\n[3, 2] [] [5, 4, 1]\n[3] [2] [5, 4, 1]\n[3] [2, 1] [5, 4]\n[] [2, 1] [5, 4, 3]\n[1] [2] [5, 4, 3]\n[1] [] [5, 4, 3, 2]\n[] [] [5, 4, 3, 2, 1].
# Waiting:8. hanoi_solver(n) should solve the tower of Hanoi puzzle for any positive value of n.