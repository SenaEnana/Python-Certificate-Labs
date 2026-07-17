def adjacency_list_to_matrix(adj_list):
    # 1. Determine the number of nodes
    # The number of nodes is equal to the number of keys in the adjacency list
    num_nodes = len(adj_list)
    
    # 2. Initialize the matrix with all 0s (size num_nodes x num_nodes)
    matrix = [[0] * num_nodes for _ in range(num_nodes)]
