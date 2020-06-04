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

    def dijkstra(self, src, weighting_function = lambda u,v,delta:delta):
        """
        Calculates the shortest path using Dijkstra's algorithm
        Parameters
        ----------
        src : str, int
            The node dijkstra's algorithm uses to find the shortest path from.
            You could provide the index of the node or the name of the node and
            the algorithm should recognize which one you have entered

        weighting_function : (int, int -> int)
            A function for rewieghting the inputs for special uses, e.g. Johnson's Algorithm
        
        Returns
        -------
        distances : List[int]
            A list representing the shortest distances to each node from the
            src node
        """
        distances = [float("inf") for i in range(self.length)]

        if type(src) == str:
            src_idx = self.names_dict[src]
        else:
            src_idx = src

        distances[src_idx] = 0
        min_heap = []
        heapq.heappush(min_heap, (distances[src_idx], src_idx))

        while min_heap:
            dist_u, u = heapq.heappop(min_heap)
            for v, weight in self.successor_edges[u_idx]:
                if (distances[u] + weighting_function(u,v,weight) < distances[v]):
                    distances[v] = distances[u] + weighting_function(u, v, weight)
                    heapq.heappush(min_heap, (distances[v], v))

        return distances
    
    def _edges_w_virtual(self, virtual_edges = []): #generator; allows access of all edges including virtual edges for purposes of Bellman Ford
        """
        Generator for iterating through all edges in the graph in situations where virtual edges are necessary for use of an algorithm
        
        Yields
        ------
        edge : (int, int, int)
            A tuple representing one real or virtual edge in the graph.
        """
        for u, edge_list in enumerate(self.successor_edges):
            for v, delta in edge_list:
                yield (u, v, delta)
        for u, v, delta in virtual_edges:
            yield (u, v, delta)
    def _virtual_edges_johnson(self): #generator of virtual edges for johnson's algorithm
        """
        Generator for virtual edges for the purposes of Johnson's algorithm

        Yields
        ------
        edge: (int, int, int)
            A tuple representing one real or virtual edge in the graph.
        """
        for index in range(len(self.successor_edges)):
            yield (len(self.successor_edges), index, 0)
    def bellman_ford(self, source = False):
        length = len(self.names_dict)
        virt = []
        source_index = length
        if not source:
            virt = self._virtual_edges_johnson(self)
        else:
            source_index = names_dict[source]
        dist = [float('inf') for x in range(length)]
        for n in range(length):
            for u, v, delta in self._edges_w_virtual(virtual_edges = virt):
                if dist[u] + delta < dist[v]:
                    dist[v] = dist[u] + delta
        for u, v, delta in self._edges_w_virtual(virtual_edges = virt):
            if dist[u] + delta >= dist[v]:
                return False
        return dist
    def johnson(self):
        """
        Calculates the shortest path using Johnson's algorithm
        Returns
        -------
        distance_matrix : List[List[int]]
            A 2-D list representing the shortest distances between all the nodes
        """
        distance_matrix = [[] for x in range(self.length)]
        # Use bellman ford that takes a node not in the graph
        b_dist = self.bellman_ford(source = False)

        for i in range(self.length):
            distance_matrix[node_idx] = self.dijkstra(u, weighting_function = lambda u, v, delta: delta + b_dist[u] - b_dist[v])
                                            + b_dist[v] - b_dist[u]  
        return distance_matrix
    
    def floyd_warshall(self):
        """
        Calculates the distance matrix using the Floyd-Warshall algorithm
        
        Returns
        -------
        dist : List[List[int]]
            A 2-D lists representing the distance matrix of the 
        """
        dist = [[float('inf') for y in range(len(self.names_dict))] for x in range(len(self.names_dict))]
        for i, edge_list in enumerate(self.successor_edges):
            for edge in edge_list:
        n = range(len(self.names_dict))
        for x in n:
            dist[x][x] = 0
        for i in n:
            for j in n:
                for k in n:
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        for x in n:
            if dist[x][x] < 0:
                return False
        return dist


