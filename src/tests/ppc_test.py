from ..algorithms.path_consist.ppc import PartialPathConsistency
from ..algorithms.cordality.triangulation import Triangulation
from .test import Test
import copy

class PPCTest(Test):
    def __init__(self, samples):
        super().__init__(samples)

    def test(self):
        for network in self.networks:
            print("=================================================")
            prime = copy.deepcopy(network)
            if Triangulation.TY(prime, list(range(network.length))):
                print(PartialPathConsistency.convert_to_PPC(prime))
            else:
                print(False)
            print(PartialPathConsistency.P3C(network, list(range(network.length))))
