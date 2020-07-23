from src.tests.consistency_test import ConsistencyTest

test = ConsistencyTest(verbose = True, logfile = "verify.txt", read_to_console=True)
# test.add_random_consistent_stns(10,6,8,0.7,-10,10)
# test.run()

from src.networks.random_stn import RandomSTN
from src.networks.write_stn import write_stn

names = []
for x in range(4):
    stn = RandomSTN().merrick_consistent_stn(min_no_of_nodes = 20, max_no_of_nodes = 20, edge_prob = 0.4, min_weight = -20, max_weight = 20)
    name = "twentynode"+str(x)
    names.append("sample_stns/" + name + ".stn")
    write_stn(stn, name)
for x in range(4):
    stn = RandomSTN().merrick_consistent_stn(min_no_of_nodes = 40, max_no_of_nodes = 40, edge_prob = 0.4, min_weight = -20, max_weight = 20)
    name = "fourtynode"+str(x)
    names.append("sample_stns/" + name + ".stn")
    write_stn(stn, name)
for x in range(4):
    stn = RandomSTN().merrick_consistent_stn(min_no_of_nodes = 60, max_no_of_nodes = 60, edge_prob = 0.4, min_weight = -20, max_weight = 20)
    name = "sixtynode"+str(x)
    names.append("sample_stns/" + name + ".stn")
    write_stn(stn, name)
test.add_stns_from_files(names)
test.run()
