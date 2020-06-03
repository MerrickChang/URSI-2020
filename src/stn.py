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
        heapq.heappush(min_heap, src_idx)
        while min_heap:
            u = heapq.heappop(min_heap)
            for successor_idx, weight in successor_edges[u]:
                distances[successor_idx] = min(distances[successor_idx], distances[u] + weight)
        return distances
