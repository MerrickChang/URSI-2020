from ..algorithms.path_consist.ppc import PartialPathConsistency
from ..algorithms.cordality.triangulation import Triangulation
from ..algorithms.shortest_path.johnson import Johnson
from .test import Test
import copy

class PPCTest(Test):
    def __init__(self, samples):
        super().__init__(samples, consistent=True)

    def test(self):
        for network in self.networks:
            print("=================================================")
            prime = copy.deepcopy(network)
            print(Johnson.merrick_johnson(prime))
            if Triangulation.naive(prime, list(range(network.length))):
                PartialPathConsistency.convert_to_PPC(prime)
                print(Johnson.merrick_johnson(prime))
            else:
                print(False)
            PartialPathConsistency.P3C(network, list(range(network.length)))
            print(Johnson.merrick_johnson(network))
