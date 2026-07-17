def dfs_n_queens(n):
    # 1. Base case: if n is less than 1, return an empty list
    if n < 1:
        return []
    
    solutions = []
    # The stack will store tuples representing our search state:
    # (current_board_configuration)
    # An empty list [] means no queens have been placed yet.
    stack = [[]]
    
