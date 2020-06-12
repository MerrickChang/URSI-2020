from src.networks.file_reader import FileReader
from src.networks.stn import STN
from src.algorithms.bellman_ford import BellmanFord
from src.algorithms.dispatchability  import Dispatchability
from src.algorithms.johnson import Johnson
from src.algorithms.floyd_warshall import FloydWarshall
from src.algorithms.dispatch import Dispatch

class DispatchabilityTest:
    @staticmethod
    def test():
        for test in ["../../sample.stn", "../../sample2.stn", "../../sample3.stn"]:
            reader = FileReader()
            network =reader.read_file(test)
            Dispatch.fast_dispatch(network)
            try:
                Dispatchability.greedy_execute(network, "Z")
            except AssertionError as e:
                print(e)
