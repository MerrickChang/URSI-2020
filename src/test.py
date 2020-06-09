from file_reader import FileReader
from stn import STN
from bellman_ford import BellmanFord
from dispatchability  import Dispatchability
from johnson import Johnson
from floyd_warshall import FloydWarshall
for test in ["../sample.stn", "../sample2.stn", "../sample3.stn"]:
    reader = FileReader()
    network =reader.read_file(test)
    print(Johnson.merrick_johnson(network))
    print(FloydWarshall.merrick_floyd_warshall(network))
    print(BellmanFord.merrick_bellman_ford(network, list(network.names_dict.keys())[0]))
    print(BellmanFord.bannister_eppstein(network, list(network.names_dict.keys())[0]))
    try:
        Dispatchability.greedy_execute(list(network.names_dict.keys())[0])
    except:
        print("Error")
