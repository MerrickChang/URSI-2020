from src.algorithms.incremental import IncrementalAlgorithms
from .test import Test
from src.algorithms.floyd_warshall import FloydWarshall
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
            print(IncrementalAlgorithms.propagation(network, D, constraint = (u,v,delta)))
            print(IncrementalAlgorithms.naive(network, D, constraint = (u,v,delta)))

        
