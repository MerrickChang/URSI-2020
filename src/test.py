from file_reader import FileReader
from stn import STN
from bellman_ford import BellmanFord

for test in ["../sample.stn", "../sample2.stn", "../sample3.stn"]:
    reader = FileReader(test)
    reader.read_file()
    network = reader.network
    print(BellmanFord.merrick_bellman_ford(network, list(network.names_dict.keys())[0]))
    print(BellmanFord.bannister_eppstein(network, list(network.names_dict.keys())[0]))
