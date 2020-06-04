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

    def dijkstra(self, src, reweighting = lemma:):
        """
        Calculates the shortest path using Dijkstra's algorithm
        Parameters
        ----------
        src : str, int
            The node dijkstra's algorithm uses to find the shortest path from.
            You could provide the index of the node or the name of the node and
            the algorithm should recognize which one you have entered
        
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
            u, u_idx = heapq.heappop(min_heap)
            for successor_idx, weight in self.successor_edges[u_idx]:
                if (distances[u_idx] + weight < distances[successor_idx]):
                    distances[successor_idx] = distances[u_idx] + weight
                    heapq.heappush(min_heap, distances[successor_idx])

        return distances

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
        bellmanford_distances = self.bellman_ford(source = False)
        
        for node_idx, list_of_edges in enumerate(self.successor_edges):
            for successor_idx, weight in list_of_edges:
                self.successor_edges[node_idx][1] = (weight + bellmanford_distances[node_idx] - bellmanford_distances[successor_idx])

        for node_idx in range(self.length):
            distance_matrix[node_idx] = self.dijkstra(node_idx)
        return distance_matrix
    
    def floyd_warshall(self):
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
    def bellman_ford(self, source = False):
        length = len(self.names_dict)
        virt = []
        source_index = length
        if not source:
            virt = self._virtual_edges_johnson(self)
            length += 1
        else:
            source_index = names_dict[source_index]
        dist = [float('inf') for x in range(length)]
        for n in range(length):
            for u, v, delta in self._edges_w_virtual(virtual_edges = virt):
                if dist[u] + delta < dist[v]:
                    dist[v] = dist[u] + delta
        for u, v, delta in self._edges_w_virtual(virtual_edges = virt):
            if dist[u] + delta >= dist[v]:
                return False
        return dist
    def _edges_w_virtual(self, virtual_edges = []): #generator; allows access of all edges including virtual edges for purposes of Bellman Ford
        for u, edge_list in enumerate(self.successor_edges):
            for v, delta in edge_list:
                yield (u, v, delta)
        for u, v, delta in virtual_edges:
            yield (u, v, delta)
    def _virtual_edges_johnson(self): #generator of virtual edges for johnson's algorithm
        for index in range(len(self.successor_edges)):
            yield (len(self.successor_edges), index, 0)
