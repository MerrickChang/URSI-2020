from ..algorithms.incremental.matrix_update import DistanceMatrixUpdate
from .test import Test
from ..algorithms.shortest_path.floyd_warshall import FloydWarshall
import random

class IncrementalTest(Test):
    def __init__(self, samples):
        super().__init__(samples)

    def test(self):
        for network in self.networks:
            u,v,delta = random.choice([(u,v,delta)
                                        for u, edge_list in enumerate(network.successor_edges)
                                        for v, delta in edge_list.items()])
            print(FloydWarshall.merrick_floyd_warshall(network))
            network.successor_edges[u].pop(v)
            D = FloydWarshall.merrick_floyd_warshall(network)
            #network.successor_edges[u][v] = delta
            print(u,v,delta)
            print(DistanceMatrixUpdate.propagation(network, D, constraint = (u,v,delta)))
            print(DistanceMatrixUpdate.naive(network, D, constraint = (u,v,delta)))
            network.successor_edges[u][v] = delta
    def test2(self):
        for network in self.networks:
            print("Second Test")
            sample = random.sample([(u,v,delta)
                                        for u, edge_list in enumerate(network.successor_edges)
                                        for v, delta in edge_list.items()], 5)
            print(FloydWarshall.merrick_floyd_warshall(network))
            for u,v,delta in sample:
                network.successor_edges[u].pop(v)
            D_1 = FloydWarshall.merrick_floyd_warshall(network)
            D_2 = D_1
            for u,v,delta in sample:
                network.successor_edges[u][v] = delta
                D_1 = DistanceMatrixUpdate.propagation(network, D_1, constraint = (u,v,delta))
                D_2 = DistanceMatrixUpdate.naive(network, D_2, constraint = (u,v,delta))
            print(D_1)
            print(D_2)
