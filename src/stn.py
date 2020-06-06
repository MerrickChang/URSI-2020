import heapq


class STN:
    """
    A class to represent a Simple Temporal Network.
    ...
    Attributes
    ----------
    names_dict : dict[name: index]
        A dictionary that maps the name of the node to its index
    successor_edges : List[List[tuples]]
        A list of list of successor edges. The list at index i of this attribute is
        the list of edges of the i-th node. Each edge is represented by a tuple - the
        first element of the tuple is the j-th node that the i-th node is connected to
        and the second element is the weight/distance between the i-th and j-th nodes
    length : int
        number of nodes in the STN
    Methods
    -------
    floyd_warshall()
        describe
    bellman_ford()
        describe
    dijkstra(src)
        Calculates the shortest path array from src using
        Dijkstra's algorithm
    johnson(src)
        Calculates the shortest path matrix between every node
        using Johnson's algorithm
    """

    def __init__(self):
        """
        Constructor for a Simple Temporal Network
        Parameters
        ----------
            names_dict : dict[name: index]
                A dictionary that maps the name of the node to its index
            successor_edges : List[List[tuples]]
                A list of list of successor edges. The list at index i of this attribute is
                the list of edges of the i-th node. Each edge is represented by a tuple - the
                first element of the tuple is the j-th node that the i-th node is connected to
                and the second element is the weight/distance between the i-th and j-th nodes
            length : int
                number of nodes in the STN
        Returns
        -------
        None
        """
        self.names_dict = {}
        self.successor_edges = []
        self.length = 0

##    def dijkstra(self, src, reweights = False):
##        """
##        Calculates the shortest path using Dijkstra's algorithm
##        Parameters
##        ----------
##        src : str, int
##            The node dijkstra's algorithm uses to find the shortest path from.
##            You could provide the index of the node or the name of the node and
##            the algorithm should recognize which one you have entered
##        reweighted_edges: bool, List[List[(int,int)]]
##            Specifies if reweighted edges are to be used or not. If so, takes new edges
##        
##        Returns
##        -------
##        distances : List[int]
##            A list representing the shortest distances to each node from the
##            src node
##        """
##        distances = [float("inf") for i in range(self.length)]
##
##        if type(src) == str:
##            src_idx = self.names_dict[src]
##        else:
##            src_idx = src
##
##        distances[src_idx] = 0
##        min_heap = []
##        heapq.heappush(min_heap, (distances[src_idx], src_idx))
##        edges = []
##        if reweights:
##            edges = reweights
##        else:
##            edges = self.successor_edges
##        while min_heap:
##            dist_u, u = heapq.heappop(min_heap)
##            for v, weight in edges[u]:
##                alt = distances[u] + weight
##                if (alt < distances[v]):
##                    distances[v] = alt
##                    heapq.heappush(min_heap, (distances[v], v))
##
##        return distances
    
##    def _edges_w_virtual(self, virtual_edges = []): #generator; allows access of all edges including virtual edges for purposes of Bellman Ford
##        """
##        Generator for iterating through all edges in the graph in situations where virtual edges are necessary for use of an algorithm
##        
##        Yields
##        ------
##        edge : (int, int, int)
##            A tuple representing one real or virtual edge in the graph.
##        """
##        for u, edge_list in enumerate(self.successor_edges):
##            for v, delta in edge_list:
##                yield (u, v, delta)
##        for u, v, delta in virtual_edges:
##            yield (u, v, delta)
##    def _virtual_edges_johnson(self): #generator of virtual edges for johnson's algorithm
##        """
##        Generator for virtual edges for the purposes of Johnson's algorithm
##
##        Yields
##        ------
##        edge: (int, int, int)
##            A tuple representing one real or virtual edge in the graph.
##        """
##        for index in range(len(self.successor_edges)):
##            yield (len(self.successor_edges), index, 0)
##    def bellman_ford(self, source = False):
##        """
##        Implements the Bellman-Ford Algorithm
##
##        Parameters
##        ----------
##        source: bool, str
##            Specifies the source node.
##            If no source node is specified, it is assumed that the algorithm is being used for Johnson's algorithm and virtual node is generated.
##        
##        Returns
##        -------
##        dist: List[int]
##            A list of integers representing the distance from the source node
##
##        """
##        length = len(self.names_dict)
##        virt = []
##        source_index = length
##        if not source:
##            virt = self._virtual_edges_johnson()
##            length += 1
##        else:
##            source_index = names_dict[source]
##        dist = [float('inf') for x in range(length)]
##        dist[source_index] = 0
##        for n in range(length):
##            for u, v, delta in self._edges_w_virtual(virtual_edges = virt):
##                alt = dist[u] + delta
##                if alt < dist[v]:
##                    dist[v] = alt
##        for u, v, delta in self._edges_w_virtual(virtual_edges = virt):
##            if dist[u] + delta < dist[v]:
##                return False
##        return dist
##    def johnson(self):
##        """
##        Calculates the shortest path using Johnson's algorithm
##        Returns
##        -------
##        distance_matrix : List[List[int]]
##            A 2-D list representing the shortest distances between all the nodes
##        """
##        distance_matrix = [[] for x in range(self.length)]
##        # Use bellman ford that takes a node not in the graph
##        b_dist = self.bellman_ford(source = False)
##        if not b_dist:
##            return False
##        reweighted_edges =  [[(v,(weight + b_dist[u] - b_dist[v]))
##                                                       for v, weight in edge_list]
##                                                       for u, edge_list in enumerate(self.successor_edges)]
##        for u in range(len(self.names_dict)):
##            distance_matrix[u] = self.dijkstra(u, reweights = reweighted_edges)
##        for u in range(len(distance_matrix)):
##            for v in range(len(distance_matrix)):
##                distance_matrix[u][v] += b_dist[v] - b_dist[u]
##        return distance_matrix
    
##    def floyd_warshall(self):
##        """
##        Calculates the distance matrix using the Floyd-Warshall algorithm
##        
##        Returns
##        -------
##        dist : List[List[int]]
##            A 2-D lists representing the distance matrix of the STN
##        """
##        dist = [[float('inf') for y in range(len(self.names_dict))] for x in range(len(self.names_dict))]
##        for u, edge_list in enumerate(self.successor_edges):
##            for v, weight in edge_list:
##                dist[u][v] = weight
##        for x in range(len(self.names_dict)):
##            dist[x][x] = 0
##        for k in range(len(self.names_dict)):
##            for i in range(len(self.names_dict)):
##                for j in range(len(self.names_dict)):
##                    alt = dist[i][k] + dist[k][j]
##                    if dist[i][j] > alt:
##                        dist[i][j] = alt
##        for x in range(len(self.names_dict)):
##            if dist[x][x] < 0:
##                return False
##        return dist
