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
            for row_idx, col_idx in enumerate(current_state):
                # 1. Same column check: col_idx == col
                # 2. Diagonal checks: distance in rows equals distance in columns
                if col_idx == col or abs(col_idx - col) == abs(row_idx - current_row):
                    is_valid = False
                    break
                    
