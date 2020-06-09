from dijkstra import Dijkstra
from bellman_ford import BellmanFord
class Johnson:
    def __init__(self):
        pass
    @staticmethod
    def merrick_johnson(stn):
        """
        Calculates the shortest path using Johnson's algorithm
        ---------------------------------------------------------------------
        Inputs:
            stn, the STN to which the algorithm is applied
        
        Output:
            dist, A 2-D list representing the distance matrix of the STN
        ---------------------------------------------------------------------
        """
        distance_matrix = [[] for x in range(stn.length)]
        # Use bellman ford that takes a node not in the graph
        b_dist = BellmanFord.merrick_bellman_ford(stn, source = False)
        if not b_dist:
            return False
        reweighted_edges =  [[(v,(weight + b_dist[u] - b_dist[v]))
                                                       for v, weight in edge_list]
                                                       for u, edge_list in enumerate(stn.successor_edges)]
        for u in range(len(stn.names_dict)):
            distance_matrix[u] = Dijkstra.merrick_dijkstra(stn, src = u, reweights = reweighted_edges)
        for u in range(len(distance_matrix)):
            for v in range(len(distance_matrix)):
                distance_matrix[u][v] += b_dist[v] - b_dist[u]
        return distance_matrix
