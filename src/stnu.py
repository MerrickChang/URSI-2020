import heapq

'''
CONTRACT FOR STNU CLASS
Represents a Simple Temporal Network with Uncertainity. Consists of a
constructor and methods implementing the Dijkstra and Johnson's algorithms.
CLASS FIELDS
1) names_dict => A dictionary that has node names as keys and node indices as
                 values.
2) successor_edges => A list of lists of successor edges.
3) length => number of nodes in the STNU.
'''


class STNU:

    '''
    CONTRACT FOR __INIT__ METHOD
    Constructor for a Simple Temporal Network
    It initialises the fields as the following:
    names_dict = {}
    successor_edges = []
    length = 0
    '''

    def __init__(self):
        self.names_dict = {}
        self.successor_edges = []
        self.length = 0

    '''
    CONTRACT FOR DIJKSTRA METHOD
    Implements the Dijkstra algorithm.
    INPUT
    src => A node that already exists in the STNU.
    OUTPUT
    distances => An array representing the shortest distances to each node from
                 the src.
    '''

    def dijkstra(self, src):
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

    '''
    CONTRACT FOR JOHNSON METHOD
    Implements the johnson algorithm.
    INPUT
    src => An arbitrary node that does not exist in the STNU.
    OUTPUT
    distance_matrix => A 2x2 array representing the shortest distances between
                       all the nodes.
    '''

    def johnson(self, src):
        distance_matrix = [[] for x in range(self.length)]
        # Use bellman ford that takes a node not in the graph
        bellmanford_distances = self.bellmanford(src)
        for node_idx, list_of_edges in enumerate(self.successor_edges):
            for successor_idx, weight in list_of_edges:
                self.successor_edges[node_idx][1] = (weight
                  + bellmanford_distances[node_idx]
                  - bellmanford_distances[successor_idx])
        for node_idx in range(self.length):
            distance_matrix[node_idx] = self.dijkstra(node_idx)
        return distance_matrix
