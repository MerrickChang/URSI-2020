from ..algorithms.dispatchability  import Dispatchability
from ..algorithms.dispatch import Dispatch
from .test import Test

class DispatchabilityTest(Test):
    def __init__(self, samples):
        super().__init__(samples)

    def test(self):
        for network in self.networks:
            Dispatch.convert_to_dispatchable(network)
            try:
                Dispatchability.greedy_execute(network, 0)
            except AssertionError as e:
                print(e)
