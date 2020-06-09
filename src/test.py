from file_reader import FileReader
from stn import STN
from bellman_ford import BellmanFord
from dispatchability  import Dispatchability
from johnson import Johnson
from floyd_warshall import FloydWarshall
for test in ["../sample_dispatchable.stn"]:
    reader = FileReader()
    network =reader.read_file(test)
    try:
        Dispatchability.greedy_execute(network, "Z")
    except AssertionError as e:
        print(e)
