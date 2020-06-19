from .test import Test
from ..algorithms.shortest_path.floyd_warshall import FloydWarshall
import random

class FloydWarshallTest(Test):
    def __init__(self, samples):
        super().__init__(samples)

    def test(self):
        for network in self.networks:
            print(FloydWarshall.merrick_floyd_warshall(network))
