# Build an Adjacency List to Matrix Converter
# In this lab, you will build a function that converts an adjacency list representation of a 
# graph into an adjacency matrix. An adjacency list is a dictionary where each key represents a node, 
# and the corresponding value is a list of nodes that the key node is connected to. 
# An adjacency matrix is a 2D array where the entry at position [i][j] is 1 if there's an edge from node i to node j, and 0 otherwise.

# For example, given the adjacency list:

# Example Code
# {
#     0: [1, 2],
#     1: [2],
#     2: [0, 3],
#     3: [2]
# }
# The corresponding adjacency matrix would be:

# Example Code
# [
#     [0, 1, 1, 0],
#     [0, 0, 1, 0],
#     [1, 0, 0, 1],
#     [0, 0, 1, 0]
# ]
# Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

# User Stories:

# You should define a function named adjacency_list_to_matrix to convert an adjacency list to an adjacency matrix.
# The function should take a dictionary representing the adjacency list of an unweighted (either undirected or directed) graph as its argument.
# The function should:
# Convert the adjacency list to an adjacency matrix.
# Print each row in the adjacency matrix.
# Return the adjacency matrix.
# For example, adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]}) should print:

# Example Code
# [0, 0, 1, 0]
# [0, 0, 1, 1]
# [1, 1, 0, 1]
# [0, 1, 1, 0]
# and return [[0, 0, 1, 0], [0, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]].

# Tests:
# Waiting:1. You should define a function named adjacency_list_to_matrix.
# Waiting:2. The adjacency_list_to_matrix function should have one parameter.
# Waiting:3. The function should correctly determine the number of nodes from the adjacency list.
# Waiting:4. The function should correctly set matrix values to 1 for existing edges.
# Waiting:5. The function should print each row of the matrix.
# Waiting:6. The function should return the adjacency matrix.
# Waiting:7. When given the adjacency list {0: [1, 2], 1: [2], 2: [0, 3], 3: [2]}, the function should return 
# [[0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 1], [0, 0, 1, 0]].
# Waiting:8. When given the adjacency list {0: [1], 1: [0]}, the function should return [[0, 1], [1, 0]].
# Waiting:9. When given the adjacency list {0: [], 1: [], 2: []}, the function should return [[0, 0, 0], [0, 0, 0], [0, 0, 0]].

# Tests:
# Passed:1. You should define a function named adjacency_list_to_matrix.
# Passed:2. The adjacency_list_to_matrix function should have one parameter.
# Passed:3. The function should correctly determine the number of nodes from the adjacency list.
# Passed:4. The function should correctly set matrix values to 1 for existing edges.
# Passed:5. The function should print each row of the matrix.
# Passed:6. The function should return the adjacency matrix.
# Passed:7. When given the adjacency list {0: [1, 2], 1: [2], 2: [0, 3], 3: [2]}, the function should return 
# [[0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 1], [0, 0, 1, 0]].
# Passed:8. When given the adjacency list {0: [1], 1: [0]}, the function should return [[0, 1], [1, 0]].
# Passed:9. When given the adjacency list {0: [], 1: [], 2: []}, the function should return 
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]].