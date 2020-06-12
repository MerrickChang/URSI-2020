class FloydWarshall:
    def __init__(stn):
        pass
    @staticmethod
    def merrick_floyd_warshall(stn):
        """
        Calculates the distance matrix using the Floyd-Warshall algorithm
        ---------------------------------------------------------------------
        Inputs:
            stn, the STN to which the algorithm is applied
        
        Output:
            dist, A 2-D list representing the distance matrix of the STN
        ---------------------------------------------------------------------
        """
        n = range(len(stn.names_dict))
        dist = [[float('inf') for y in n] for x in n]
        for u, edge_list in enumerate(stn.successor_edges):
            for v, weight in edge_list.items():
                dist[u][v] = weight
        for x in n:
            dist[x][x] = 0
        for k in n:
            for i in n:
                for j in n:
                    alt = dist[i][k] + dist[k][j]
                    if dist[i][j] > alt:
                        dist[i][j] = alt
        for x in n:
            if dist[x][x] < 0:
                return False
        return dist
    
