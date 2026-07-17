# Implement the N-Queens Algorithm
# The N-Queens problem asks you to place N queens on an N×N chessboard so that no two queens attack 
# each other (no two share a row, column, or diagonal).

# For example, if there is a 4x4 board, one valid arrangement is:

# Example Code
# [1, 3, 0, 2]
# That means that in row 0, the queen is placed in column 1; in row 1, the queen is placed in column 3; in row 2, 
# the queen is placed in column 0; and in row 3, the queen is placed in column 2.

# Visually, this arrangement looks like:

# Example Code
# . Q . .
# . . . Q
# Q . . .
# . . Q .
# Where Q represents a queen and . represents an empty square.

# In this lab, you will implement the N-Queens problem solver using the depth-first search approach.

# Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

# User Stories:

# You should have a function named dfs_n_queens.
# The function should accept exactly one argument: an integer n.
# If n is less than 1, the function should return an empty list ([]).
# The function should return a list of solutions; each solution is itself a list of length n, where the element at 
# index i is the column index (0-based) of the queen in row i.
