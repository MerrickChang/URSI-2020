from .test import Test
from ..algorithms.shortest_path.johnson import Johnson
import random

class JohnsonTest(Test):
    def __init__(self, samples):
        super().__init__(samples)

    def test(self):
        for network in self.networks:
            print(Johnson.merrick_johnson(network))
