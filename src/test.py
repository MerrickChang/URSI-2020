from file_reader import FileReader
from stn import STN
from bellman_ford import BellmanFord
from dispatchability  import Dispatchability
from johnson import Johnson
from floyd_warshall import FloydWarshall
from dispatch import Dispatch
for test in ["../sample.stn", "../sample2.stn", "../sample3.stn"]:
    reader = FileReader()
    network =reader.read_file(test)
    Dispatch.fast_dispatch(network)
    try:
        Dispatchability.greedy_execute(network, "Z")
    except AssertionError as e:
        print(e)
