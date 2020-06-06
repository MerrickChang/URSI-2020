class BellmanFord:
    def __init__(self):
        pass
    @staticmethod
    def _edges_w_virtual(stn, virtual_edges = []): #generator; allows access of all edges including virtual edges for purposes of Bellman Ford
        """
        Generator for iterating through all edges in the graph in situations where virtual edges are necessary for use of an algorithm
        
        Yields
        ------
        edge : (int, int, int)
            A tuple representing one real or virtual edge in the graph.
        """
        for u, edge_list in enumerate(stn.successor_edges):
            for v, delta in edge_list:
                yield (u, v, delta)
        for u, v, delta in virtual_edges:
            yield (u, v, delta)
    @staticmethod
    def _virtual_edges_johnson(stn): #generator of virtual edges for johnson's algorithm
        """
        Generator for virtual edges for the purposes of Johnson's algorithm

        Yields
        ------
        edge: (int, int, int)
            A tuple representing one real or virtual edge in the graph.
        """
        length = len(stn.successor_edges)
        for index in range(length):
            yield (length, index, 0)
    @staticmethod
    def merrick_bellman_ford(stn, source = False):
        """
        Implements the Bellman-Ford Algorithm

        Parameters
        ----------
        source: bool, str
            Specifies the source node.
            If no source node is specified, it is assumed that the algorithm is being used for Johnson's algorithm and virtual node is generated.
        
        Returns
        -------
        dist: List[int]
            A list of integers representing the distance from the source node

        """
        length = len(stn.names_dict)
        virt = []
        source_index = length
        if not source:
            virt = BellmanFord._virtual_edges_johnson(stn)
            length += 1
        else:
            source_index = stn.names_dict[source]
        dist = [float('inf') for x in range(length)]
        dist[source_index] = 0
        for n in range(length):
            for u, v, delta in BellmanFord._edges_w_virtual(stn, virtual_edges = virt):
                alt = dist[u] + delta
                if alt < dist[v]:
                    dist[v] = alt
        for u, v, delta in BellmanFord._edges_w_virtual(stn, virtual_edges = virt):
            if dist[u] + delta < dist[v]:
                return False
        return dist
    
