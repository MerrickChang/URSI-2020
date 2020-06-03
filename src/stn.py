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
        print(dist)
        for i in n:
            for j in n:
                for k in n:
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        print(dist)
        for x in n:
            if dist[x][x] < 0:
                return False
        return dist
    
