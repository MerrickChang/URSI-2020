import heapq
class Dijkstra:
    def __init__(self):
        pass


    
    @staticmethod
    def merrick_dijkstra(stn, src, reweights = False):
            """
            Calculates the shortest path using Dijkstra's algorithm

            Inputs:
                src, an int or a string representing the node dijkstra's algorithm uses to find the shortest path from.
                    You could provide the index of the node or the name of the node and the algorithm should recognize which one you have entered
                reweights, a boolean or list that specifies if reweighted edges are to be used or not.
                        If so, it represents the new edges. If not, it is simply false

            Outputs: 
                distances, a list of integers representing the shortest distances to each node from the src node
            """
            distances = [float("inf") for i in range(stn.length)]

            if type(src) == str:
                src_idx = stn.names_dict[src]
            else:
                src_idx = src

            distances[src_idx] = 0
            min_heap = []
            heapq.heappush(min_heap, (distances[src_idx], src_idx))
            edges = []
            if reweights:
                edges = reweights
            else:
                edges = stn.successor_edges
            while min_heap:
                dist_u, u = heapq.heappop(min_heap)
                for v, weight in edges[u]:
                    alt = distances[u] + weight
                    if (alt < distances[v]):
                        distances[v] = alt
                        heapq.heappush(min_heap, (distances[v], v))

            return distances
