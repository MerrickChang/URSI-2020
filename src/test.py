from stn import STN
from file_reader import FileReader

reader = FileReader("../sample2.stn")
reader.read_file()
STN  = reader.network
print(STN.floyd_warshall())
