from ..algorithms.dispatchability  import Dispatchability
from ..algorithms.dispatch import Dispatch
from .test import Test

class DispatchabilityTest(Test):
    def __init__(self, samples):
        super().__init__(samples)

    def test(self):
        for network in self.networks:
            converted = Dispatch.convert_to_dispatchable(network)
            print(converted)
            for n in converted.names_dict:
                try:
                    Dispatchability.greedy_execute(converted, n)
                except AssertionError as e:
                    print(e)
