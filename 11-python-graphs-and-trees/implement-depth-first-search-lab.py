def dfs(matrix, start_node):

    stack = [start_node]

    visited = []

    while stack:

        current = stack.pop()

        if current not in visited:
            visited.append(current)

            for neighbor in range(len(matrix)):
                if matrix[current][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)
                    
    return visited