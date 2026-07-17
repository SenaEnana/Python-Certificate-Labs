def dfs_n_queens(n):
    if n < 1:
        return []
    
    solutions = []
    stack = [[]]
    
    while stack:
        current_state = stack.pop()
        current_row = len(current_state)
        
