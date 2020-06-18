##===================================
##File: johnson.py
##Author: Merrick Chang
##Date: May 2020
##===================================


from .dijkstra import Dijkstra
from .bellman_ford import BellmanFord


class Johnson:
    """
    The Johnson class implements various static methods associated with Johnson's algorithm.
    """


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
        reweighted_edges =  [dict([(v,(weight + b_dist[u] - b_dist[v]))
                                                       for v, weight in edge_list.items()])
                                                       for u, edge_list in enumerate(stn.successor_edges)]
        for u in range(len(stn.names_dict)):
            distance_matrix[u] = Dijkstra.merrick_dijkstra(stn, src = u, reweights = reweighted_edges)
        for u in range(len(distance_matrix)):
            for v in range(len(distance_matrix)):
                distance_matrix[u][v] += b_dist[v] - b_dist[u]
        return distance_matrix

    @staticmethod
    def johnson(network):
        """
        Calculates the shortest path using Johnson's algorithm
        Parameters
        ----------
        src : str, int
            An arbitrary node that does not exist in the STN.
        Returns
        -------
        distance_matrix : List[List[int]]
            A 2-D list representing the shortest distances between all the nodes
        """
        distance_matrix = [[] for x in range(network.length)]

        potential_function = BellmanFord.bellman_ford_wrapper(network)

        if not potential_function:
            return False

        for node_idx in range(network.length):
            distance_matrix[node_idx] = Dijkstra.dijkstra(
                network, node_idx, potential_function=potential_function)

        for src_idx, distance_list in enumerate(distance_matrix):
            for successor_idx, weight in enumerate(distance_list):
                distance_matrix[src_idx][successor_idx] = weight + \
                    potential_function[successor_idx] - \
                    potential_function[src_idx]


        if network.dist_up_to_date:
            network.dist_up_to_date = False

        network.distance_matrix = distance_matrix
        return distance_matrix
