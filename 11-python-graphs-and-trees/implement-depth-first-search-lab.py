def dfs(matrix, start_node):
    # Initialize the stack with the starting node
    stack = [start_node]
    # Keep track of visited nodes to prevent infinite loops and track reachability
    visited = []
    
    # Continue processing as long as there are nodes in the stack
    while stack:
        # Pop the last element added to the stack (LIFO principle)
        current = stack.pop()
        
        # If the node has not been visited yet, mark it as visited
        if current not in visited:
            visited.append(current)
            
            # Find neighbors from the adjacency matrix
            # Loop through all nodes in the graph
            for neighbor in range(len(matrix)):
                # If there is an edge (matrix value is 1) and neighbor isn't visited
                if matrix[current][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)
