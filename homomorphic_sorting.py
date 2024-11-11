import time
import numpy as np
import graph_drawing as dr
from collections import defaultdict
import pandas as pd


def diagonal_list(matrix): # Returns elements on the diagonal of a matrix as a list.
    a = []
    n = len(matrix)
    for i in range(n):
        a.append(matrix[i][i])
    return a


def group_matrices(matrices,yes_no_to_visual):
    steps = 0 
    """
    llist - the list of non-homomorphics matrices
    keys - key to identify the unique graps
    step - counts the number of 
    """

    groups = defaultdict(list)
    llist = []
    keeys = []
    
    start_time = time.time()
    # for idx, matrix in enumerate(matrices):
    for matrix in matrices:
        steps +=1
        n = len(matrix)
        matrixp = np.array(matrix)
        matrix_powers = []
        
        for i in range(2, n+1):
            steps +=1
            AA = np.linalg.matrix_power(matrixp, i)
            di = tuple(sorted(diagonal_list(AA.tolist())))
            matrix_powers.append(di)
        
        flattened_list = [item for sublist in matrix_powers for item in sublist]
        ky = (tuple(flattened_list))
        groups[ky].append(matrix)
        
    
    # print("\nGrouping completed. Processing results:")
    for key, group in groups.items():
        steps +=1
        A = np.array(group)
        llist.append(A[0].tolist())
        keeys.append(key)

        if yes_no_to_visual == True:
            print(f"Group with key {key}:")
            print(f"Representative matrix:\n{A[0]}")
            print(f"Number of matrices in this group: {len(group)}")
            print("-" * 40)
            p2 = len(group)
            for matrix in group:
                # Print each matrix
                for row in matrix:
                    print(row)
        
                # Create a DataFrame for the matrix and its visualization
                df = pd.DataFrame({
                    'Adjacency_Matrix': [matrix],  # Adjacency matrices
                    'Graph_Image_1': [dr.draw_graph_1color(matrix, "red")],  # First set of graph images
                    'Degree_sequence': [ao.tuple_to_image(key)]
                })
        
                image_cols = ["Graph_Image_1", 'Degree_sequence']
        
                # Print information
                print(f" {steps}/{p2}  AND  n = {n}")
        
                # Call generalized table results function
                ao.table_results_GENERAL(df, 'Adjacency_Matrix', image_cols)
        
                # Increment count1 within the group
                steps += 1
                print("\n--- Matrix End ---\n")
        
    end_time = time.time() # to measure the end time
    number_of_unique_graphs = len(llist)
    print(number_of_unique_graphs)
    
    runtime = end_time-start_time
    
    return llist, keeys, number_of_unique_graphs, runtime,steps








