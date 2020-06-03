class STN:
    def __init__(self):
        self.names_dict = {}
        self.successor_edges = []
    def floyd_warshall(self):
        print(self.names_dict)
        dist = [[float('inf') for y in range(len(self.names_dict))] for x in range(len(self.names_dict))]
        for i, edge_list in enumerate(self.successor_edges):
            for edge in edge_list:
                dist[i][self.names_dict[edge[0]]] = edge[1]
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
            for u, edge in enumerate(self._edges_w_virtual(virtual_edges = virt)):
                v = self.name_list[edge[0]]
                if dist[u] + edge[1] < dist[v]:
                    dist[v] = dist[u] + edge[1]
        for u, edge in enumerate(self._edges_w_virtual(virtual_edges = virt)):
            if dist[u] + edge[1] >= edge[0]:
                return False
        return dist
    def _edges_w_virtual(self, virtual_edges = []): #generator; allows access of all edges including virtual edges for purposes of Bellman Ford
        for edge_list in self.successor_edges:
            for edge in edge_list:
                yield edge
        for edge in virtual_edges:
            yield edge
    def _virtual_edges_johnson(self): #generator of virtual edges for johnson's algorithm
        for name in names_dict:
            yield (name, 0)
