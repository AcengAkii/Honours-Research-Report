import numpy as np
import function_bron_kerbosch_clique_finder as bk
import function_matrix_to_edge_connection as mx
import function_complement_graph as cm
import adjacency as aj
import function_drawing as dr
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display, HTML
import Algorithm_outputs_at_each_step_visualisation as ao
import time

def Rams(k, l):
    step = 0
    start_rams = time.time()
    k = k
    l = l
    n = 1  # Start the search at 1 nodes and increment until conditions are met.
    all_graphs_meet_condition = False
    
    if l == 1 or k == 1:
        step += 1
        all_graphs_meet_condition = True

    while not all_graphs_meet_condition:
        step += 1
        # Step 1: Build the adjacency matrices
        graphs = aj.all_adj_matrix(n)
        
        print(f"for order = {n}")
        
        p1 = len(graphs)
        print(f"Number of graphs to check = {p1}")
        
        # Step 2: Initialize a list to track which graphs meet the condition
        these_graphs_meet_condition_list = []
        
        count1 = 1
        
        # Step 3: Iterate over each graph and check for conditions
        for graph in graphs:
            step += 1
            
            # Step 4: Find the complement graph for l-set
            complement_graph = cm.complement_graphs(graph)
            
            graph1 = graph
            c_graph1 = complement_graph
            
            # Step 5: Convert to dictionary format for processing
            k_graph = mx.adj_mat_dict(graph1)
            l_graph = mx.adj_mat_dict(complement_graph)
            
            # Step 6: Find maximal cliques in both k_graph and l_graph
            clique_set_k = bk.MaximalCliquesFinder(k_graph)
            clique_set_k.find_cliques()
            clique_list_k = clique_set_k.list_of_cliques()
            
            clique_set_l = bk.MaximalCliquesFinder(l_graph)
            clique_set_l.find_cliques()
            clique_list_l = clique_set_l.list_of_cliques()
            
            # Step 7: Find the largest cliques in both k_graph and l_graph
            k_max = max(clique_list_k, key=len)
            l_max = max(clique_list_l, key=len)
            length_k = len(k_max)
            length_l = len(l_max)
            
            # Step 8: Check if the graph meets at least one condition
            if length_k < k and length_l < l:
                step += 1
                graphs = []
                m = np.array(graph)
                print(f'ADJ_mat for graph that fails to meet the condition {m}')
                
                df = pd.DataFrame({
                    'Adjacency_Matrix': [graph],
                    'Graph_Image': [dr.draw_graph(graph)],
                    'Graph_Image_1': [dr.draw_graph_1color(graph, "red")],
                    'Graph_Image_2': [dr.draw_graph_1color(complement_graph, "blue")]
                })
                
                Images = ['Graph_Image', 'Graph_Image_1', 'Graph_Image_2']
                ao.table_results_GENERAL(df, 'Adjacency_Matrix', Images)
                
                n += 1
                print("---------------------------")
                break  # Exit the inner loop to restart with a new graph size
            elif length_k >= k or length_l >= l:
                step += 1
                # If the condition is met, mark this graph as successful
                these_graphs_meet_condition_list.append(1)

        # If all graphs meet at least one condition, we have found the Ramsey number
        if len(these_graphs_meet_condition_list) == len(graphs):
            step += 1
            all_graphs_meet_condition = True
            print(f"All graphs have a clique of size k = {k} or an indp set of size l = {l}")
            print("---------------------------")
        else:
            step += 1
            continue

        end_rams = time.time()
        run_rams = end_rams - start_rams
        
        print(f"The Ramsey number is = {n}")
        
    return n, run_rams, step

