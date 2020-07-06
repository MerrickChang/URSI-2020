from ..algorithms.dispatchability  import Dispatchability
from ..algorithms.dispatch import Dispatch
from .test import Test

class DispatcherTest(Test):
    def __init__(self, samples):
        super().__init__(samples)

    def test(self):
        for network in self.networks:
            for n in range(network.length):
                try:
                    for delta in network.successor_edges[n].values():
                        assert delta >= 0
                    print(network)
                    print(Dispatchability.greedy_execute(network, n))
                except AssertionError as e:
                    print(e)
