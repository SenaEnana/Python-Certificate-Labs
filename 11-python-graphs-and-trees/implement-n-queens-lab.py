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
            
        # Try placing a queen in every column of the current row
        # To match standard DFS order (left-to-right processing), we push onto the stack 
        # in reverse order (from column n-1 down to 0)
        for col in range(n - 1, -1, -1):
           pass