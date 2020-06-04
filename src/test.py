from file_reader.py import FileReader
from stn.py import STN

for test in ["../sample.stn", "../sample2.stn", "../sample3.stn"]:
    reader = FileReader(test)
    reader.read_file()
    network = reader.network
    print(network.floyd_warshall())
    print(network.johnson())
