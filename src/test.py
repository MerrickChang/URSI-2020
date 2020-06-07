from file_reader import FileReader
from stn import STN
from floyd_warshall import FloydWarshall
from johnson import Johnson

for test in ["../sample.stn", "../sample2.stn", "../sample3.stn"]:
    reader = FileReader(test)
    reader.read_file()
    network = reader.network
    print(FloydWarshall.merrick_floyd_warshall(network))
    print(Johnson.merrick_johnson(network))
