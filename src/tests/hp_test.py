from .test import Test
from ..algorithms.shortest_path.potential import Potential

class HPTest(Test):
    def __init__(self, samples):
        super().__init__(samples)

    def test(self):
        for network in self.networks:
            print(Potential.hunsberger_posenato(network))
