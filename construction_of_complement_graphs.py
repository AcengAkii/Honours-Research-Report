import numpy as np
"""
constructing the complement graphs:
inputs: an adjacency matrix as a list of lists
"""
def complement_graphs(adj_mat): #pass through a single adjacency matrics
    n = len(adj_mat)
    a = np.zeros((n,n)).tolist()
    
    for i in range(n):
        for j in range(n):
            if i != j:
                if adj_mat[i][j] == 1:
                    a[i][j] = 0
                elif adj_mat[i][j] == 0:
                    a[i][j] = 1
            else:
                a[i][j] = 0     
    return a