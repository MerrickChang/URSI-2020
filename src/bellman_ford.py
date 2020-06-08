import random
class BellmanFord:
    def __init__(self):
        pass
    @staticmethod
    def _edges_w_virtual(stn, virtual_edges = []): #generator; allows access of all edges including virtual edges for purposes of Bellman Ford
        """
        Generator for iterating through all edges in the graph in situations where virtual edges are necessary for use of an algorithm

        Parameters
        ----------
        stn: STN
            The target stn
        virtual_edges: Iterable[(int, int, int)]
            Iterable that yields the representation of the virtual edge
        
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

        Parameters
        ----------
        stn: STN
            The target stn
        
        Yields
        ------
        edge: (int, int, int)
            A tuple representing one real or virtual edge in the graph.
        """
        length = len(stn.successor_edges)
        for index in range(length):
            yield (length, index, 0)
    @staticmethod
    def _relax(u,v,delta,dist):
        """
        Helper method to make Bellman-Ford implementations somewhat more readable

        Parameters
        ----------
        u: int
            Index of the starting vertex of the edge
        v: int
            Index of the stoping vertex of the edge
        delta: int
            The edge wieght
        dist: List[int]
            The array of distances to be relaxed
        
        Effects
        -------
        Relaxes distance values stored in dist accordingly

        Returns
        -------
        True if the edge was relaxed. False if the edge was not relaxed
        """
        alt = dist[u] + delta
        if alt < dist[v]:
            dist[v] = alt
            return True
        return False
    @staticmethod
    def merrick_bellman_ford(stn, source = False):
        """
        Implements the Bellman-Ford Algorithm

        Parameters
        ----------
        stn: STN
            The target stn
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
                BellmanFord._relax(u,v,delta,dist)
        for u, v, delta in BellmanFord._edges_w_virtual(stn, virtual_edges = virt):
            if dist[u] + delta < dist[v]:
                return False
        return dist
    @staticmethod
    def bannister_eppstein(stn, source = False): #WIP based on https://arxiv.org/pdf/1111.5414.pdf
        """Implements the Bannister-Eppstein's improvement of Yen's optimization of the Bellman-Ford Algorithm

        Parameters
        ----------
        stn: STN
            The target stn
        source: bool, str
            Specifies the source node.
            If no source node is specified, it is assumed that the algorithm is being used for Johnson's algorithm and virtual node is generated.
        
        Returns
        -------
        dist: List[int]
            A list of integers representing the distance from the source node"""
        length = len(stn.names_dict)
        source_successor_edges = []
        source_index = length
        if not source:
            source_successor_edges = [(x, 0) for x in range(length)]
            length += 1
        else:
            source_index = stn.names_dict[source]
            source_successor_edges = stn.successor_edges[source_index]
        dist = [float('inf') for x in range(length)]
        dist[source_index] = 0
        C = [source_index]
        #Create an ordering for the nodes. Put the source first, create a random ordering for the other nodes.
        random_order = list(range(length))
        random_order.pop(source_index)
        random.shuffle(random_order)
        random_order.insert(0, source_index)
        #Partition the edges (i,j) into sets G+ and G- where i<j and i>j respectively, where i and j are the indexes of the vertexes of the edge in the ordering
        G_minus = [[] for edge_list in stn.successor_edges]
        G_plus = [[] for edge_list in stn.successor_edges]
        for u, edge_list in enumerate(stn.successor_edges):
            for i, edge in enumerate(edge_list):
                if u < edge[0]:
                    G_plus[u].append(i)
                elif u > edge[0]:
                    G_minus[u].append(i)
        while len(C) != 0:
            has_changed = [False for x in range(length)]
            #For each vertex in order, relax the edges G+
            if source_index in C:
                for edge_index in G_plus[source_index]:
                    v,delta = stn.successor_edges[source_index][edge_index]
                    has_changed[v] = BellmanFord._relax(source_index,v,delta,dist)
            for u in random_order[1:]:
                if u in C or has_changed[u]:
                    for edge_index in G_plus[u]:
                            v,delta = stn.successor_edges[u][edge_index]
                            has_changed[v] = BellmanFord._relax(u,v,delta,dist)
            #For each vertex in reverse order, relax the edge in G- 
            for u in random_order[:0:-1]:
                if u in C or has_changed[u]:
                    for edge_index in G_minus[u]:
                            v,delta = stn.successor_edges[u][edge_index]
                            has_changed[v] = BellmanFord._relax(u,v,delta,dist)
            if source_index in C or has_changed[u]:
                for edge_index in G_minus[source_index]:
                    v,delta = stn.successor_edges[source_index][edge_index]
                    has_changed[v] = BellmanFord._relax(source_index,v,delta,dist)
            #Set C to include only the vertices that have had their distance values changed
            C = []
            for u,_ in enumerate(has_changed):
                if _:
                    C.append(u)
        for u, v, delta in BellmanFord._edges_w_virtual(stn, virtual_edges = BellmanFord._virtual_edges_johnson(stn) if not source else []):
            if dist[u] + delta < dist[v]:
                return False
        return dist
