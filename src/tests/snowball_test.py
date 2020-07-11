from .test import Test
from ..algorithms.shortest_path.johnson import Johnson
from ..algorithms.shortest_path.snowball import Snowball
import random

class SnowballTest(Test):
    def __init__(self, samples):
        super().__init__(samples, consistent = True)

    def test(self):
        for network in self.networks:
            print(Johnson.merrick_johnson(network))
            print(Snowball.snowball(network, list(range(network.length))))
