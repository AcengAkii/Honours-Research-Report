import networkx as nx 
import matplotlib.pyplot as plt
import math
import matplotlib.patches as patches
import numpy as np

def circular_layout(n): 
    '''
    n - number of nodes
    '''
    pos = {}
    if n == 2:     # Special case for 2 nodes - place them on the positive and negative x-axis
        pos[1] = (1, 0)  # First node on positive x-axis
        pos[2] = (-1, 0) # Second node on negative x-axis
    else:
        for i in range(1, n + 1):
            if i == 1:
                pos[i] = (1, 0)  # Fix the first node on the positive x-axis
            else:
                # Distribute the remaining nodes equidistantly around the circle
                angle = 2 * math.pi * (i - 1) / n
                pos[i] = (math.cos(angle), math.sin(angle)) 
    return pos

def draw_graph(adj_matrix, colour,nodesize,edgewidth, complement):
    """
    adj_matrix - a single adjacency matrix as a list of lists.
    colour - colour you wish to draw the edges in.
    nodesize - size of the nodes
    edgewith- thickness of the edges
    complement - input true to draw the complement graph or false if not
    """
    n = len(adj_matrix)

    G = nx.Graph() #empty graph
    G.add_nodes_from(range(1, n + 1))    # Add nodes, indexed from 1 to n.

    for i in range(n):     # Add edges for the graph (G)
        for j in range(i + 1, n):
            if adj_matrix[i][j] == 1:
                G.add_edge(i + 1, j + 1)  
        
    pos = circular_layout(n)
    
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('none')  # Set figure background to transparent
    ax.set_facecolor('none')         # Set plot (axes) background to transparent
    
    # Visualize the graph
    nx.draw(G, pos, edge_color=colour, node_size=nodesize, width=3, with_labels=True, ax=ax)
    plt.axis('equal')  # Equal aspect ratio ensures that circles look circular.
    plt.show()

    if complement == True:
        GC = nx.Graph()
        GC.add_nodes_from(range(1, n + 1))
        
        for p in range(n): # Add edges for the complement graph (G2) 
            for q in range(p + 1, n):
                if adj_matrix[p][q] == 0:
                    GC.add_edge(p + 1, q + 1)  # Shift by +1

        pos2 = circular_layout(n)
        fig, ax = plt.subplots()
        fig.patch.set_facecolor('none')  # Set figure background to transparent
        ax.set_facecolor('none')         # Set plot (axes) background to transparent
    
        # Visualize the graph
        nx.draw(GC, pos2, edge_color=colour, node_size=nodesize, width=3, with_labels=True, ax=ax)
        plt.axis('equal')  # Equal aspect ratio ensures that circles look circular.
        plt.show()
        



def draw_graph_cliques(adj_matrix, clique_nodes,colour, nodesize, edgewidth):
    """ 
    parameters:
    adj_matrix - adjacency matrix as a list of lists
    clique_nodes - 
    colour - colour of the clique you wish to highlight
    nodesize - size of the nodes
    edgewidth - thickness of edges
    """
    # Create graph and add all nodes
    G = nx.Graph()
    n = len(adj_matrix)
    G.add_nodes_from(range(n))  # Add all nodes to the graph

    # Add edges for the clique
    G.add_edges_from((i, j) for i in clique_nodes for j in clique_nodes if adj_matrix[i][j])

    # Position nodes in a circular layout
    pos = circular_layout(n)

    # Draw the entire graph with all nodes
    nx.draw(G, pos, edge_color='lightgray', node_size = nodesize , width= edgewidth, with_labels=True)

    clique_edges = [(i, j) for i in clique_nodes for j in clique_nodes if adj_matrix[i][j]]
    nx.draw_networkx_edges(G, pos, edgelist=clique_edges, node_size = nodesize,edge_color=colour, width=edgewidth)

    plt.axis('equal')  # Equal aspect ratio ensures that circles look circular.
    plt.show()
