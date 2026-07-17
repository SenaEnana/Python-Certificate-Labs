def dfs_n_queens(n):
    # 1. Base case: if n is less than 1, return an empty list
    if n < 1:
        return []
    
    solutions = []
 