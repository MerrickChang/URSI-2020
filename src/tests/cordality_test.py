from ..algorithms.path_consist.dpc_dispatch  import DPCDispatch
from ..algorithms.path_consist.dpc import DirectedPathConsistency
from .test import Test

class CordalityTest(Test):
    def __init__(self, samples):
        super().__init__(samples)

    def test(self):
        for network in self.networks:
            print(DPCDispatch.dpc_dispatch(DirectedPathConsistency.convert_to_DPC(network,  range(network.length)), range(network.length)))
