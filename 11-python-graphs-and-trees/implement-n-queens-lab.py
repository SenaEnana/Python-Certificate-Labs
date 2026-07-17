def dfs_n_queens(n):
    if n < 1:
        return []
    
    solutions = []
    stack = [[]]
    
    while stack:
        current_state = stack.pop()
        current_row = len(current_state)

        if current_row == n:
            solutions.append(current_state)
            continue
            
        for col in range(n - 1, -1, -1):
            is_valid = True
