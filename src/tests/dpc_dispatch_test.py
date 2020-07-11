from ..algorithms.path_consist.dpc_dispatch import DPCDispatch
from ..algorithms.path_consist.dpc import DirectedPathConsistency
from ..algorithms.dispatchability import Dispatchability
from .test import Test
import copy

class DPCDispatchTest(Test):
    def __init__(self, samples):
        super().__init__(samples)

    def test(self):
        for network in self.networks:
            if DirectedPathConsistency.convert_to_DPC(network, range(network.length)):
                solution = DPCDispatch.dpc_dispatch(network, range(network.length))
                if solution:
                    print(solution)
                    print(Dispatchability._check_solution(network, solution))
                else:
                    print("Error")
