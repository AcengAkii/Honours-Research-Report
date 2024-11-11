import numpy as np
"""
Create adjacency matrices

input: size of matrix
output: adjacency matrices as list of lists
"""
def all_adj_matrix(n):
    # Calculate the number of edges in a complete graph with n vertices
    number_of_edges = n * (n - 1) // 2  # Use integer division
    
    number_of_graphs = 2**(number_of_edges)
    
    # Construct all possible adjacency matrices
    lists_of_graph_strings = []
    for i in range(number_of_graphs):
        p = format(i, f'0{number_of_edges}b')
        lists_of_graph_strings.append(p)

    adjmat = []  # List of adjacency matrices

    for k in range(len(lists_of_graph_strings)):
        
        v = lists_of_graph_strings[k]
        A = np.zeros((n, n), dtype=int)  # Initialize an n x n matrix of zeros

        # Fill the upper triangle of the matrix
        idx = 0
        for i in range(n):
            for j in range(i + 1, n):
                A[i][j] = int(v[idx])  # Convert string to int
                idx += 1

        # Reflect about the diagonal to make the matrix symmetric
        for i in range(n):
            for j in range(i + 1, n):
                A[j][i] = A[i][j]

        adjmat.append(A.tolist())  # Convert numpy array to list of lists

    return adjmat