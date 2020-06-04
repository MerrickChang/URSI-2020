import heapq

class STN:

    def __init__(self):
        self.names_dict = {}
        self.successor_edges = []
        self.length = 0

    def dijkstra(self, src):
        distances = [float("inf") for i in range(self.length)]
        src_idx = self.names_dict[src]
        distances[src_idx] = 0
        min_heap = []
        heapq.heappush(min_heap, distances[src_idx])
        while min_heap:
            u = heapq.heappop(min_heap)
            for successor_idx, weight in self.successor_edges[u]:
                if (distances[u] + weight < distances[successor_idx]):
                    distances[successor_idx] = distances[u] + weight
                    heapq.heappush(min_heap, distances[successor_idx])
                #distances[successor_idx] = min(distances[successor_idx], distances[u] + weight)
        return distances

    def johnson(self, src):
        distance_matrix = [[] for x in range(self.length)]
        #Use bellman ford that takes a node not in the graph
        bellmanford_distances = self.bellmanford(src)
        for idx, list in enumerate(self.successor_edges):
            for successor_idx, weight in list:
                weight = weight + bellmanfedord_distances[idx] - bellmanford_distances[successor_idx]
        for node_name in self.names_dict.keys():
            node_idx = self.names_dict[node_name]
            distance_matrix[node_idx] = self.dijkstra(node_name)
        return distance_matrix
