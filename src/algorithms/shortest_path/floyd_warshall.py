
##===================================
##File: floyd_warshall.py
##Author: Merrick Chang
##Date: May 2020
##===================================

class FloydWarshall:
    """
    The FloydWarshall class implements static methods associated with the Floyd-Warhall algorithm.
    """

    @staticmethod
    def merrick_floyd_warshall(stn):
        """
        Calculates the distance matrix using the Floyd-Warshall algorithm
        ---------------------------------------------------------------------
        Inputs:
            stn, the STN to which the algorithm is applied

        Output:
            dist, A 2-D list representing the distance matrix of the STN
        ---------------------------------------------------------------------
        """
        n = range(len(stn.names_dict))
        dist = [[float('inf') for y in n] for x in n]
        for u, edge_list in enumerate(stn.successor_edges):
            for v, weight in edge_list.items():
                dist[u][v] = weight
        for x in n:
            dist[x][x] = 0
        for k in n:
            for i in n:
                for j in n:
                    alt = dist[i][k] + dist[k][j]
                    if dist[i][j] > alt:
                        dist[i][j] = alt
        for x in n:
            if dist[x][x] < 0:
                return False
        return dist
    @staticmethod
    def floyd_warshall(network):
        """
        -------------------------------------------------------------------------
        A static method that calculates the shortest distances between all nodes.
        -------------------------------------------------------------------------
        Parameters
        ----------
        network: STN
            The simple temporal network the algorithm is going to be run on.
        Returns
        -------
        distance_matrix: int[][]
            A NxN array representing the shortest distances between all nodes.
        """
        length = network.length
        distance_matrix = [[float("inf") for i in range(length)]
                           for j in range(length)]

        # ??
        # Initialize matrix entries to match the edges in the network
        for node_idx, edge_dict in enumerate(network.successor_edges):
            for successor_node_idx, weight in edge_dict.items():
                distance_matrix[node_idx][successor_node_idx] = weight

            # Note:  This is optional... it can be useful to have
            # values > 0 here (they would indicate that length of
            # shortest loop containing a given node)

            # we could run a bfs here to add the length of the shortest
            # loop... shouldnt affect time complexity.... if we are
            # worried about it we could run the dfs before the for loop
            # and store the results in an array
            distance_matrix[node_idx][node_idx] = 0

        for i in range(length):
            for j in range(length):
                for k in range(length):
                    distance_matrix[i][j] = min(
                        distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])

        for node_idx in range(length):
            if distance_matrix[node_idx][node_idx] < 0:
                return False

        if network.dist_up_to_date:
            network.dist_up_to_date = False

        network.distance_matrix = distance_matrix
        return distance_matrix
