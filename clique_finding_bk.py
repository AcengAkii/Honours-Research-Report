'''
bron-kerbosch algorithm

inputs: a node, followed by a list of its adjacent nodes.
format of input: dictionary, where each node is the key.

'step': counts the number of operations taken to find a solution
'''

class MaximalCliquesFinder:
    def __init__(self, graph): #initialisation, of the adj_mat as self
        self.graph = graph
        self.maximal_cliques = []

    def find_cliques(self): 
        nodes = list(self.graph.keys())
        self._extend([], nodes, []) #--compsub[], candidates, not[], this line creates a new set of nodes to evaluate.

    def _extend(self, compsub, candidates, not_set,k): #looping through new versions comp/cand/not, k-order of complete subgraph desired.
        step = 0 
        if not candidates and not not_set: #if both 'candidate' and 'not' are empty compsub is a maximul clique
            step += 1
            self.maximal_cliques.append(compsub)
            return

        # Branch and bound: Choose a pivot
        pivot = candidates[0] if candidates else not_set[0] #1st element in candidate chosen
        #pivot = max(candidates, key=lambda node: len(self.graph[node])) #element with highest degree chosen.
        
        # Iterate through candidates not connected to the pivot
        for candidate in candidates[:]:
            step += 1
            if candidate in self.graph[pivot]:
                continue
            
            # New sets for recursion
            new_compsub = compsub + [candidate]
            new_candidates = [v for v in candidates if v in self.graph[candidate]]
            new_not_set = [v for v in not_set if v in self.graph[candidate]]

            # Recursive call to extend compsub
            self._extend(new_compsub, new_candidates, new_not_set)

            # Move candidate to not_set
            candidates.remove(candidate)
            not_set.append(candidate)

            if len(compsub) >= k: # stop when k-clique/l-set is found.
                break 

    def print_cliques(self): #prints the list of cliques
        for clique in self.maximal_cliques: 
            print(clique)
            
    def list_of_cliques(self): #Returns the list of cliques
        a = list(self.maximal_cliques)
        return a